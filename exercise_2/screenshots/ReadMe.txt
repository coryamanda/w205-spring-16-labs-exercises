The screenshots directory contains three explanatory screenshots of the tweet parsing process running.

- screenshot-hellostream.png shows my Twitter credentials interacting with the stream and downloading a portion of the tweets during a given window of time, at a rate of about 40 tweets/second.
- screenshot-twitterStream.png shows the stream in progress (note that all words are logged as upper case and additional punctuation is trimmed from the beginning and end of words)
- bar_chart.png shows a standard bar chart of the 20 most common words captured, created in Excel. Unsurprisingly, they are all function words: THE, I, YOU, A, and TO are the most common. Note that I replaced apostrophes with underscores to avoid them being read as strings, so I_M should be read as I'M.