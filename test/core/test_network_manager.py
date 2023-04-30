import unittest
import unittest.mock as mock
from vancouver_earthquake.core.earthquake import Earthquake
from vancouver_earthquake.core.network_manager import get_earthquake_data
from vancouver_earthquake.storage.data_handler import read_json


class TestEarthquakeProvider(unittest.TestCase):

    def test_get_earthquake_data(self):
        earthquakes = read_json('test_data/get_earthquake_data.json')
        expected_earthquakes = [Earthquake(title='M 3.4 - 37 km SW of Princeton, Canada', magnitude=3.4,
                                           longitude=-120.8133, latitude=49.1893, time=1682702356267,
                                           detail_url='https://earthquake.usgs.gov/earthquakes/eventpage/us7000jwrg'),
                                Earthquake(title='M 4.3 - 205 km SW of Port McNeill, Canada', magnitude=4.3,
                                           longitude=-128.8899, latitude=49.1534, time=1681930591548,
                                           detail_url='https://earthquake.usgs.gov/earthquakes/eventpage/us6000k5kt'),
                                Earthquake(title='M 4.2 - 256 km W of Tofino, Canada', magnitude=4.2,
                                           longitude=-129.36, latitude=48.7804, time=1681487345553,
                                           detail_url='https://earthquake.usgs.gov/earthquakes/eventpage/us6000k4hp'),
                                Earthquake(title='M 3.0 - 23 km NW of Stanley, Idaho', magnitude=3.02,
                                           longitude=-115.172833333333, latitude=44.3515, time=1681318288600,
                                           detail_url='https://earthquake.usgs.gov/earthquakes/eventpage/mb90010333')]

        with mock.patch('vancouver_earthquake.core.earthquake_provider.fetch_earthquakes', return_value=earthquakes):
            earthquake_data = get_earthquake_data()
            self.assertEqual(earthquake_data, expected_earthquakes)

    def test_empty_earthquake_data(self):
        earthquakes = read_json('test_data/empty_earthquake_data.json')
        expected_earthquakes = []

        with mock.patch('vancouver_earthquake.core.earthquake_provider.fetch_earthquakes', return_value=earthquakes):
            earthquake_data = get_earthquake_data()
            self.assertEqual(earthquake_data, expected_earthquakes)


if __name__ == '__main__':
    unittest.main()
