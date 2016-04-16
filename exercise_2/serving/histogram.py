import psycopg2
import sys

if len(sys.argv) == 2:
    passed = sys.argv[1]
    try:
        lower, upper = passed.split(",")
    except:
        sys.exit("Oops! Please try again, I need two words with a comma in the middle!")

    upper = int(upper)
    lower = int(lower)

    if lower > upper:
        print "Swapping upper and lower bounds..."
        temp = lower
        lower = upper
        upper = temp

    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
    cur = conn.cursor()

    sql = "SELECT * FROM tweetwordcount WHERE count BETWEEN %s AND %s ORDER BY count DESC;" % (str(lower), str(upper))
    cur.execute(sql)
    records = cur.fetchall()
    for rec in records:
        print str(rec[0]) + ": "+ str(rec[1])

    conn.commit()
    conn.close()

else:
    print "Oops! Please try again with two valid numbers with a comma in the middle. Maybe you added an extra space?"
