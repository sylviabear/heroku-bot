# Dependencies
import tweepy
import json
import time
from datetime import datetime

# Twitter API Keys
consumer_key = "YScGj4M4Oe3iyJIK0X7Ou14cx"
consumer_secret = "IQeC6itNFMmedpDuyp1hrO4f1JXHBRNWuR0U8UtjYbjOF80OE6"
access_token = "983530416182255616-3cVUmtGd04By1mAuNhU2FjprvIC8HVA"
access_token_secret = "B7TBjmUw8YEIRbdl5yCwaTMabrDywIub0ckNqrZn9tZDP"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE
api.update_status(f"Hello, world! {str(datetime.now())}")
