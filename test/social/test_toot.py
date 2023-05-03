import unittest
from unittest import mock
from unittest.mock import MagicMock

from vancouver_earthquake.social.toot import send_new_toot, Mastodon


class TestToot(unittest.TestCase):
    def test_send_new_toot(self):
        status: str = 'M 3.4 - 37 km SW of Princeton, Canada : 2023-04-28 10:19:16 : Vancouver ' \
                      'Time\n#Vancouver #VancouverEarthquake #Earthquake #EarthquakeVancouver'
        image_path: str = '../outputs/vancouver_earthquake_map.png'
        expected_response = 'https://mastodon.social/@vancouver_earthquake/106268106724765151'

        mastodon_mock = MagicMock(spec=Mastodon)
        mastodon_mock.media_post.return_value = {'id': '1234'}
        with mock.patch('vancouver_earthquake.social.toot.send_new_toot',
                        return_value=expected_response), \
                mock.patch(
                    'vancouver_earthquake.social.toot.connect_to_mastodon', return_value=mastodon_mock) as mock_connect_to_mastodon:
            send_new_toot(message=status, image_path=image_path)
            mastodon_mock.media_post.assert_called_once_with(media_file=image_path)
            mock_connect_to_mastodon.assert_called_once()
            mastodon_mock.status_post.assert_called_once_with(status=status, in_reply_to_id=None,
                                                              media_ids={'id': '1234'})


if __name__ == '__main__':
    unittest.main()
