from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt
import sys


def percentage(numer, denom):
    return 100*float(numer)/float(denom)

consumerKey = "FjcQ6IPVavu4lwhwrCUfz0vei"
consumerSecret = "PZoIJFxiVGyeqlkHSHK7NSj54RWeYyVYNdsaND4oUy37gXOyQb"
accessToken = "864887814567075840-UcRF8VtQI4ak2l2swryegECvoFKwf1d"
accessSecret = "ZUVzu7jwefMoDhlNatJhsoF09g6wPQGuD4EgA4qvgMbYo"

auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessSecret)

api = tweepy.API(auth)

searchKeyword = input("Search key: ")
numSearchTerms = int(input("Enter number of Tweets to analyze: "))

try:
    tweets = tweepy.Cursor(api.search, q=searchKeyword, lang='English').items(numSearchTerms)

    positiveCount = 0
    negativeCount = 0
    neutralCount = 0
    polarity = 0
    positivePerc = 0
    negativePerc = 0
    neutralPerc = 0

    for tweet in tweets:
        # print(tweet.text)
        analysis = TextBlob(tweet.text)
        tweetPolarity = analysis.sentiment.polarity
        polarity += tweetPolarity
        if(tweetPolarity > 0):
            positiveCount = positiveCount+1
        elif(tweetPolarity == 0):
            neutralCount = neutralCount+1
        elif(tweetPolarity < 0):
            negativeCount = negativeCount+1

    positivePerc = percentage(positiveCount, numSearchTerms)
    negativePerc = percentage(positiveCount, numSearchTerms)
    neutralPerc = percentage(positiveCount, numSearchTerms)
except tweepy.error.RateLimitError:
    print("Rate limit exceeded, try again later with less tweets!")
except tweepy.error.TweepError:
    print("Error accessing Twitter, try later!")
