# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "Odf1Yqx30X759l9IHDldUTU8M"
consumer_secret = "od61QkBbBIP6BAzdVUGU716oM4O57XSKlYGeCXhB0aNq37wfoo"
access_token = "943251070754672640-tPfS6k199feWr75lI9BLfivMAleR93D"
access_token_secret = "g9AtdaknzWb3w59cJI3mnu1yIaFZ3MHEpAdbq6g8KJw5v"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "Can't stop. Won't stop. Chatting! This is Tweet #%s!" %
        tweet_number)


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1