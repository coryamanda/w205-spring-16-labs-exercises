Goal of this project:
The goal of the project is to collect tweets from the Twitter stream, parse them into words, store the counts in a Postgres database, and make the results available to the user interactively through Python query scripts. The hope is to use this data to understand interesting trends on Twitter either real-time or close to real time.

How to use this application:
- Create an instance of the community AMI UCB W205 Spring Ex 2 Image and connect to it as you normally would. Attach a volume on which HDFS and Postgres are already installed and configured. (In this case, I used the volume created in Labs 2 and 3.)

- Run bash-setup.sh. This script mounts the data volume, starts Hadoop and Postgres, activates the correct Python bin so we are using 2.7, and installs psycopg2 and tweepy if needed. Next, it creates an Apache Storm project called EXTweetwordcount, clones my repo on github, and transfers the appropriate files into the new Storm project. Finally, it creates a new database and table in Postgres to store the tweets as they are parsed.

- Change directory to the new EXTweetwordcount application. (cd EXTweetwordcount)

- Update the file Twittercredentials.py with valid credentials, as these cannot be shared publicly. Save and close the file. (cd EXTweetwordcount)

- Run Storm tweetwordcount application. (sparse run)

- After the application has run for a sufficiently long period of time, use ctrl-c to exit the stream. Based on the data collected running hello-stream, the application downloads about 40 tweets per second. 

- Move to the directory where the serving scripts are stored and use them to explore the data collected. There are further instructions about these files, their arguments, and their outputs in the /serving directory. (cd ..; cd w205-spring-16-labs-exercises/serving)

