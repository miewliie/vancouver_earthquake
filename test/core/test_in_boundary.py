import unittest

from vancouver_earthquake.core.earthquake import Earthquake
from vancouver_earthquake.core.network_manager import earthquake_encoder
from vancouver_earthquake.main import in_boundary
from vancouver_earthquake.storage.data_handler import read_json


class TestInBoundary(unittest.TestCase):

    def test_filter_out_some_not_in_boundary(self):
        earthquake_json = read_json('test/core/test_data/get_earthquake_data.json')
        expected_earthquakes = [Earthquake(title='M 3.4 - 37 km SW of Princeton, Canada', magnitude=3.4,
                                           longitude=-120.8133, latitude=49.1893, time=1682702356267,
                                           detail_url='https://earthquake.usgs.gov/earthquakes/eventpage/us7000jwrg'),
                                Earthquake(title='M 4.3 - 205 km SW of Port McNeill, Canada', magnitude=4.3,
                                           longitude=-128.8899, latitude=49.1534, time=1681930591548,
                                           detail_url='https://earthquake.usgs.gov/earthquakes/eventpage/us6000k5kt'),
                                Earthquake(title='M 4.2 - 256 km W of Tofino, Canada', magnitude=4.2,
                                           longitude=-129.36, latitude=48.7804, time=1681487345553,
                                           detail_url='https://earthquake.usgs.gov/earthquakes/eventpage/us6000k4hp')]

        earthquakes: list[Earthquake] = in_boundary(earthquake_encoder(earthquake_json))
        self.assertEqual(earthquakes, expected_earthquakes)

    def test_filter_out_all_not_in_boundary(self):
        earthquake_json = read_json('test/core/test_data/not_in_boundary_earthquakes.json')
        expected_earthquakes = []
        earthquakes: list[Earthquake] = in_boundary(earthquake_encoder(earthquake_json))
        self.assertEqual(earthquakes, expected_earthquakes)

    def test_no_filter_out_if_empty_earthquake(self):
        earthquake_json = read_json('test/core/test_data/empty_earthquake_data.json')
        expected_earthquakes = []
        earthquakes: list[Earthquake] = in_boundary(earthquake_encoder(earthquake_json))
        self.assertEqual(earthquakes, expected_earthquakes)


if __name__ == '__main__':
    unittest.main()
