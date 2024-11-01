import tweepy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

Client = tweepy.Client(bearer_token=os.getenv("BEARER_TOKEN"),
                       consumer_key=os.getenv("TWITTER_API_KEY"),
                       consumer_secret=os.getenv("TWITTER_API_KEY_SECRET"),
                       access_token=os.getenv("ACCESS_TOKEN"),
                       access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"))

Client.create_tweet(text="This is a test tweet from a secure API setup!")
print("Tweet sent successfully")