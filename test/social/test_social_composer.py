import unittest
from unittest import mock

from vancouver_earthquake.core.earthquake import Earthquake
from vancouver_earthquake.social.social_composer import compose_message, create_map


class TestSocialComposer(unittest.TestCase):

    def test_compose_message_with_one_earthquake(self):
        expected_messages: str = 'M 3.4 - 37 km SW of Princeton, Canada : 2023-04-28 10:19:16 : Vancouver ' \
                                 'Time\n#Vancouver #VancouverEarthquake #Earthquake #EarthquakeVancouver'
        earthquakes: list[Earthquake] = [Earthquake(title='M 3.4 - 37 km SW of Princeton, Canada',
                                                    magnitude=3.4, longitude=-120.8133,
                                                    latitude=49.1893, time=1682702356267,
                                                    detail_url='https://earthquake.usgs.gov/earthquakes/eventpage'
                                                               '/us7000jwrg')]
        with mock.patch('vancouver_earthquake.social.social_composer.compose_message',
                        return_value=expected_messages):
            actual_messages = compose_message(earthquakes=earthquakes)
            self.assertEqual(actual_messages, expected_messages)

    def test_compose_message_with_multiple_earthquakes(self):
        expected_messages: str = 'M 3.4 - 37 km SW of Princeton, Canada : 2023-04-28 10:19:16 : Vancouver ' \
                                 'Time\nM 3.4 - 37 km SW of Princeton, Canada : 2023-04-28 10:19:16 : Vancouver ' \
                                 'Time\n#Vancouver #VancouverEarthquake #Earthquake #EarthquakeVancouver'
        earthquakes: list[Earthquake] = [Earthquake(title='M 3.4 - 37 km SW of Princeton, Canada',
                                                    magnitude=3.4, longitude=-120.8133,
                                                    latitude=49.1893, time=1682702356267,
                                                    detail_url='https://earthquake.usgs.gov/earthquakes/eventpage'
                                                               '/us7000jwrg')] * 2
        with mock.patch('vancouver_earthquake.social.social_composer.compose_message',
                        return_value=expected_messages):
            actual_messages = compose_message(earthquakes=earthquakes)
            self.assertEqual(actual_messages, expected_messages)

    def test_create_map(self):
        earthquakes: list[Earthquake] = [Earthquake(title='M 3.4 - 37 km SW of Princeton, Canada',
                                                    magnitude=3.4, longitude=-120.8133,
                                                    latitude=49.1893, time=1682702356267,
                                                    detail_url='https://earthquake.usgs.gov/earthquakes/eventpage'
                                                               '/us7000jwrg')] * 2
        base_image_path = '../assets/vancouver_base_map.png'
        expected_image_path = '../outputs/vancouver_earthquake_map.png'

        with mock.patch('vancouver_earthquake.social.social_composer.create_map',
                        return_value=expected_image_path), \
                mock.patch('vancouver_earthquake.social.social_composer.draw_earthquake_points',
                           return_value=expected_image_path) as mock_draw_points:
            actual_image_path = create_map(earthquakes=earthquakes)
            mock_draw_points.assert_called_once_with(base_image_path=base_image_path, output_path=expected_image_path,
                                                     earthquakes=earthquakes)
            self.assertEqual(actual_image_path, expected_image_path)


if __name__ == '__main__':
    unittest.main()
