#Log into EC2 instance, "Spring 2016 for Exercise 2"
mount -t ext4 /dev/xvdf #mount data volume

#Start Hadoop and Postgres
/root/start-hadoop.sh
/data/start_postgres.sh

#Activate Python 2.7 bin
source /opt/py27environment/bin/activate

#Install psycopg2 if needed
pip install psycopg2

#Install tweepy if needed
pip install tweepy
git clone https://github.com/tweepy/tweepy.git
cd tweepy
python setup.py install

#Create project
sparse quickstart EXTweetwordcount

#Clone repo, copy files into EXTweetwordcount
git clone https://github.com/coryamanda/w205-spring-16-labs-exercises.git
cp w205-spring-16-labs-exercises/exercise_2/Twittercredentials.py EXTweetwordcount/Twittercredentials.py
cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/config.json EXTweetwordcount/config.json
cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/fabfile.py EXTweetwordcount/fabfile.py
cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/project.clj EXTweetwordcount/project.clj
cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/README.md EXTweetwordcount/README.md
cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/tasks.py EXTweetwordcount/tasks.py
cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/spouts/tweets.py EXTweetwordcount/src/spouts/tweets.py
cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/spouts/__init__.py EXTweetwordcount/src/spouts/__init__.py
cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/bolts/parse.py EXTweetwordcount/src/bolts/parse.py
cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/bolts/wordcount.py EXTweetwordcount/src/bolts/wordcount.py
cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/bolts/__init__.py EXTweetwordcount/src/bolts/__init__.py
cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/topologies/tweetwordcount.clj EXTweetwordcount/topologies/tweetwordcount.clj


#Create the table in postgres
psql -U postgres -c "DROP DATABASE IF EXISTS tcount;"
psql -U postgres -c "CREATE DATABASE tcount;"
psql -U postgres -d tcount -c "DROP TABLE IF EXISTS tweetwordcount;"
psql -U postgres -d tcount -c "CREATE TABLE tweetwordcount (word TEXT, count INT);"
