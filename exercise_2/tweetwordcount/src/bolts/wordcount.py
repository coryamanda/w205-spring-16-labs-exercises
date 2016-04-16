from collections import Counter
from streamparse.bolt import Bolt
import psycopg2

class WordCounter(Bolt):

    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])
        this_count = self.counts[word]

        cur = WordCounter.conn.cursor()

        # Avoid breaking when it hits a single quote
        if "'" in word:
            word = word.replace("'", "_")

        sql = "UPDATE tweetwordcount "
        sql += "SET count=%s WHERE word='%s';" % (this_count, word)

        sql += "INSERT INTO tweetwordcount (word, count) "
        sql += "SELECT '%s', %s WHERE NOT EXISTS " % (word, this_count)
        sql += "(SELECT 1 FROM tweetwordcount WHERE word='%s');" % (word)

        cur.execute(sql)
        WordCounter.conn.commit()

        # Log the count - just to see the topology running
        try:
            self.log('%s: %d' % (word, self.counts[word]))
        except:
            pass
