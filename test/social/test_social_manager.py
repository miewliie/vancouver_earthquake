import unittest
from unittest import mock

from vancouver_earthquake.core.earthquake import Earthquake
from vancouver_earthquake.social.social_manager import social_manager


class TestSocialManager(unittest.TestCase):

    def test_social_manager(self):
        image_path = 'test_data/map.png'
        message = 'M 3.4 - 37 km SW of Princeton, Canada'
        earthquakes = [Earthquake(title='1km ENE of The Geysers, CA', magnitude=1.2, longitude=-120.8133,
                                  latitude=49.1893, time=1620439020, detail_url='xxx')]

        with mock.patch('vancouver_earthquake.social.social_manager.create_map',
                        return_value=image_path) as mock_create_map, \
                mock.patch('vancouver_earthquake.social.social_manager.compose_message',
                           return_value=message) as mock_compose_message, \
                mock.patch('vancouver_earthquake.social.social_manager.send_new_toot') as mock_send_new_toot, \
                mock.patch('vancouver_earthquake.social.social_manager.send_new_tweet') as mock_send_new_tweet:
            social_manager(earthquakes=earthquakes)
            mock_create_map.assert_called_once_with(earthquakes=earthquakes)
            mock_compose_message.assert_called_once_with(earthquakes=earthquakes)
            mock_send_new_toot.assert_called_once_with(message=message, image_path=image_path)
            mock_send_new_tweet.assert_called_once_with(message=message, image_path=image_path)

    def test_social_manager_exception(self):
        image_path = 'test_data/map.png'
        message = 'M 3.4 - 37 km SW of Princeton, Canada'
        earthquakes = [Earthquake(title='1km ENE of The Geysers, CA', magnitude=1.2, longitude=-120.8133,
                                  latitude=49.1893, time=1620439020, detail_url='xxx')]

        with mock.patch('vancouver_earthquake.social.social_manager.create_map',
                        return_value=image_path) as mock_create_map, \
                mock.patch('vancouver_earthquake.social.social_manager.compose_message',
                           return_value=message) as mock_compose_message, \
                mock.patch('vancouver_earthquake.social.social_manager.send_new_toot') as mock_send_new_toot, \
                mock.patch('vancouver_earthquake.social.social_manager.send_new_tweet') as mock_send_new_tweet:
            social_manager(earthquakes=earthquakes)
            mock_create_map.assert_called_once_with(earthquakes=earthquakes)
            mock_compose_message.assert_called_once_with(earthquakes=earthquakes)
            mock_send_new_toot.assert_called_once_with(message=message, image_path=image_path)
            mock_send_new_toot.side_effect = Exception('test exception')
            mock_send_new_tweet.assert_called_once_with(message=message, image_path=image_path)


if __name__ == '__main__':
    unittest.main()
