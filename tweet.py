import os
import tweepy
from earthquake.earthquake import get_earthquake_title, get_earthquake_info


TW_BEARER_TOKEN = os.getenv('TW_BEARER_TOKEN')
TW_API_KEY = os.getenv('TW_API_KEY')
TW_API_KEY_SECRET = os.getenv('TW_API_KEY_SECRET')

TW_USER_ACCESS_TOKEN = os.getenv('TW_USER_ACCESS_TOKEN')
TW_USER_ACCESS_TOKEN_SECRET = os.getenv('TW_USER_ACCESS_TOKEN_SECRET')


def send_new_status_for(earthquake_title: str):
    """ Tweet Earthquake status. """

    client = tweepy.Client(bearer_token=TW_BEARER_TOKEN, consumer_key=TW_API_KEY, consumer_secret=TW_API_KEY_SECRET,
                           access_token=TW_USER_ACCESS_TOKEN, access_token_secret=TW_USER_ACCESS_TOKEN_SECRET,)

    response = client.create_tweet(text=earthquake_title)
    print(response)


if __name__ == '__main__':

    earthquake_data = get_earthquake_info()
    earthquake_info = get_earthquake_title()

    if not len(earthquake_data) == 0 and not len(earthquake_info) == 0:
        send_new_status_for(earthquake_info)
        print(earthquake_info)
    else:
        print("No earthquake")
