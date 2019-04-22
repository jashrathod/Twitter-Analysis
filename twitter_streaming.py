# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import os

# Variables that contains the user credentials to access Twitter API (Enter the required credentials)
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


# Creates necessary files for storing tweets (if not created)
def input_data_to_file(data):
    twitter_data_file = "twitter_data.txt"
    if not os.path.isfile(twitter_data_file):
        file = open(twitter_data_file, 'w')
        file.write(data)
        file.close()
    else:
        file = open(twitter_data_file, 'a')
        file.write(data)
        file.close()


# A basic listener that writes received tweets to twitter_data.txt
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        input_data_to_file(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # Handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # Filtering Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby', 'java'])
