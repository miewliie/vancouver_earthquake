import unittest

from vancouver_earthquake.core.earthquake import Earthquake
from vancouver_earthquake.core.network_manager import earthquake_encoder
from main import filter_out_duplicate_earthquake
from vancouver_earthquake.storage.data_handler import read_json


class TestFilterOutDuplicateEarthquake(unittest.TestCase):

    def test_filter_out_all_duplicate_earthquake(self):
        old_earthquake: list[Earthquake] = earthquake_encoder(read_json('test/core/test_data/old_earthquake.json'))
        new_earthquake: list[Earthquake] = earthquake_encoder(read_json('test/core/test_data/new_earthquake.json'))
        expected_earthquakes = []
        earthquakes: list[Earthquake] = filter_out_duplicate_earthquake(old_eq=old_earthquake,
                                                                        new_eq=new_earthquake)
        self.assertEqual(earthquakes, expected_earthquakes)

    def test_filter_out_some_duplicate_earthquake(self):
        old_earthquake: list[Earthquake] = earthquake_encoder(read_json('test/core/test_data/old_earthquake.json'))
        new_earthquake: list[Earthquake] = earthquake_encoder(read_json(
            'test/core/test_data/some_duplicate_earthquake.json'))
        expected_earthquakes = [Earthquake(title='M 4.0 - 203 km W of Bandon, Oregon', magnitude=4,
                                           longitude=-126.8961, latitude=43.3446, time=1679892793815,
                                           detail_url='https://earthquake.usgs.gov/earthquakes/eventpage/us7000jmyr')]
        earthquakes: list[Earthquake] = filter_out_duplicate_earthquake(old_eq=old_earthquake,
                                                                        new_eq=new_earthquake)
        self.assertEqual(earthquakes, expected_earthquakes)

    def test_not_filter_out_no_duplicate_earthquake(self):
        old_earthquake: list[Earthquake] = earthquake_encoder(read_json('test/core/test_data/old_earthquake.json'))
        new_earthquake: list[Earthquake] = earthquake_encoder(read_json(
            'test/core/test_data/not_duplicate_earthquake.json'))
        expected_earthquakes = new_earthquake
        earthquakes: list[Earthquake] = filter_out_duplicate_earthquake(old_eq=old_earthquake,
                                                                        new_eq=new_earthquake)
        self.assertEqual(earthquakes, expected_earthquakes)

    def test_not_filter_out_no_old_earthquake_data(self):
        old_earthquake: list[Earthquake] = []
        new_earthquake: list[Earthquake] = earthquake_encoder(read_json('test/core/test_data/new_earthquake.json'))
        expected_earthquakes = new_earthquake
        earthquakes: list[Earthquake] = filter_out_duplicate_earthquake(old_eq=old_earthquake,
                                                                        new_eq=new_earthquake)
        self.assertEqual(earthquakes, expected_earthquakes)


if __name__ == '__main__':
    unittest.main()