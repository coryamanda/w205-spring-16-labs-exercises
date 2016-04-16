import psycopg2
import sys

def singleword(myword):
    sql = "SELECT count FROM tweetwordcount WHERE word='%s';" % (myword)
    cur.execute(sql)
    records = cur.fetchall()
    for rec in records:
        count = int(rec[0])
    print 'Total number of occurences of "%s": %d' % (myword, count)

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()


if len(sys.argv) == 2:
  passed_word = sys.argv[1]
  singleword(passed_word)

elif len(sys.argv) > 2:
  print "Oops! This system isn't equipped to handle more than one word at a time. But since we're here I'll do it anyway."
  all_words = sys.argv[1:]
  for passed_word in all_words:
      singleword(passed_word)

else:

  sql = "SELECT * FROM tweetwordcount ORDER by word ASC;"
  cur.execute(sql)

  records = cur.fetchall()
  for rec in records:
      print "(" + rec[0] + ", " + str(rec[1]) + "),"

conn.commit()
conn.close()
