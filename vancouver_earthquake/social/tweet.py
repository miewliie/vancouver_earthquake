import os
import tweepy

""" This module provides functions to tweet earthquake status."""

TW_BEARER_TOKEN = os.getenv('TW_BEARER_TOKEN')
TW_API_KEY = os.getenv('TW_API_KEY')
TW_API_KEY_SECRET = os.getenv('TW_API_KEY_SECRET')

TW_USER_ACCESS_TOKEN = os.getenv('TW_USER_ACCESS_TOKEN')
TW_USER_ACCESS_TOKEN_SECRET = os.getenv('TW_USER_ACCESS_TOKEN_SECRET')


def send_new_tweet(message: str, image_path: str):
    """ Tweet Earthquake status. """

    client = tweepy.Client(bearer_token=TW_BEARER_TOKEN, consumer_key=TW_API_KEY, consumer_secret=TW_API_KEY_SECRET,
                           access_token=TW_USER_ACCESS_TOKEN, access_token_secret=TW_USER_ACCESS_TOKEN_SECRET,)

    response = client.create_tweet(text=message)
    print(response)

