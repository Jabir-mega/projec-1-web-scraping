import tweepy
from tweepy import OAuthHandler, TweepyException
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API keys and tokens
X_API_KEY = os.getenv("API_KEY")
X_API_SECRET = os.getenv("API_SECRET")
X_ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Set up the authentication
auth = tweepy.OAuthHandler(X_API_KEY, X_API_SECRET)
auth.set_access_token(X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Verify authentication
try:
    user = api.verify_credentials()
    if user:
        print("Authentication successful")
        print(f"Connected as {user.screen_name}")
    else:
        print("Authentication failed")
except TweepyException as e:
    print(f"Failed to connect: {e}")

# Fetch the last tweet of a specific user
try:
    username = "HersiYussuf"
    tweets = api.user_timeline(screen_name=username, count=1, tweet_mode="extended")
    
    if tweets:
        last_tweet = tweets[0]
        print("\nLast tweet from @{}: \n{}".format(username, last_tweet.full_text))
    else:
        print(f"No tweets found for user {username}")

except TweepyException as e:
    print(f"Error fetching tweet: {e}")
