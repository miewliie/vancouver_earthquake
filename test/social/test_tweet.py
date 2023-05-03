import unittest
from unittest import mock
from unittest.mock import MagicMock

from vancouver_earthquake.social.tweet import send_new_tweet, tweepy


class TestTweet(unittest.TestCase):

    def test_send_new_tweet(self):
        status: str = 'test_status'
        image_path: str = 'test_image_path'
        expected_response = 'https://twitter.com/van_earthquake/status/123456789'

        client_mock = MagicMock(spec=tweepy.Client)

        with mock.patch('vancouver_earthquake.social.tweet.send_new_tweet'), \
                mock.patch('vancouver_earthquake.social.tweet.tweepy.OAuth1UserHandler', return_value=MagicMock()), \
                mock.patch('vancouver_earthquake.social.tweet.tweepy.Client', return_value=client_mock):
            send_new_tweet(message=status, image_path=image_path)
            client_mock.create_tweet.assert_called_once_with(text=status)


if __name__ == '__main__':
    unittest.main()
