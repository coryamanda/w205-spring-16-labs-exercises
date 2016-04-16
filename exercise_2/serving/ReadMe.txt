The serving directory contains two Python scripts for interacting with the parsed tweet data:

finalresults.py
- When a single word is passed as an argument, the output is the number of times that word appeared in the tweet stream. Note that all tweets are converted to upper case when stored, so the query should also be upper case.
- When multiple words are passed as arguments, the output is the number of times each word appeared in the tweet stream.
- When no words are passed as arguments, the output is the full list of words in the database and their corresponding counts.

histogram.py
- This function accepts two numbers separated by a comma. More than one argument will prompt an explanatory message. The output is a list of all the words whose counts are within the range specified by the numbers. The order of the numbers does not matter.