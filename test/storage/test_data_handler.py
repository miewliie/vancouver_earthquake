import os
import unittest
import json
from unittest import mock
from collections import namedtuple

from vancouver_earthquake.storage.data_handler import *


class TestDataHandler(unittest.TestCase):

    def test_read_json_output_json_if_content_exist(self):
        input_value: str = repr({"type": "FeatureCollection", "features": []})
        expected_value: str = repr({"type": "FeatureCollection", "features": []})
        file_path: str = 'test/storage/test_data/read_json.json'

        mock_file = mock.mock_open(read_data=json.dumps(input_value))
        with mock.patch('vancouver_earthquake.storage.data_handler.open', mock_file) as mock_open:
            actual_value = read_json(file_path=file_path)
            mock_open.assert_called_once_with(file_path, 'r', encoding='utf-8')
            self.assertEqual(expected_value, actual_value)

    def test_read_json_output_none_if_no_content(self):
        file_path: str = 'test/storage/test_data/read_json.json'
        input_data = 'Any data'
        expected_data = None
        mock_file = mock.mock_open(read_data=json.dumps(input_data))
        with mock.patch('vancouver_earthquake.storage.data_handler.open', mock_file), \
                mock.patch('vancouver_earthquake.storage.data_handler.os.path.getsize',
                           return_value=0) as mock_getsize:
            value = read_json(file_path=file_path)
            mock_getsize.assert_called_once_with(file_path)
            self.assertEqual(expected_data, value)

    def test_write_json_success_with_valid_input(self):
        earthquakes = {'type': 'FeatureCollection', 'features': []}
        file_path = 'test/storage/test_data/write_json.json'
        mock_file = mock.mock_open(read_data=json.dumps(earthquakes))
        with mock.patch('vancouver_earthquake.storage.data_handler.open', mock_file) as mock_open, \
                mock.patch('vancouver_earthquake.storage.data_handler.json.dump') as mock_dump:
            write_json(data=earthquakes, file_path=file_path)
            mock_open.assert_called_once_with(file_path, 'w', encoding='utf-8')
            mock_dump.assert_called_once_with(earthquakes, mock_open(file_path, 'w', encoding='utf-8'))

    def test_from_dict_to_earthquake(self):
        earthquakes_dict = {"properties": {"mag": 1.2, "title": "1km ENE of The Geysers, CA", "time": 1620439020,
                                           "url": "xxx"}, "geometry": {"type": "Point", "coordinates": [-120.8133,
                                                                                                        49.1893]}}

        expected_value = Earthquake(title='1km ENE of The Geysers, CA', magnitude=1.2,
                                    longitude=-120.8133, latitude=49.1893, time=1620439020, detail_url='xxx')
        with mock.patch('vancouver_earthquake.storage.data_handler.Earthquake') as mock_earthquake:
            mock_earthquake.return_value = expected_value
            actual_value = from_dict_to_earthquake(earthquakes_dict)
            self.assertEqual(actual_value, expected_value)

    def test_from_earthquake_to_dict(self):
        earthquakes = Earthquake(title='1km ENE of The Geysers, CA', magnitude=1.2,
                                 longitude=-120.8133, latitude=49.1893, time=1620439020, detail_url='xxx')
        expected_value = {"properties": {"mag": 1.2, "title": "1km ENE of The Geysers, CA", "time": 1620439020,
                                         "url": "xxx"}, "geometry": {"coordinates": [-120.8133, 49.1893]}}
        with mock.patch('vancouver_earthquake.storage.data_handler.to_dict') as mock_to_dict:
            mock_to_dict.return_value = expected_value
            actual_value = to_dict(earthquakes)
            self.assertEqual(actual_value, expected_value)

    def test_earthquake_encoder(self):
        earthquake_dict = {"features": [{"properties": {"mag": 1.2, "title": "1km ENE of The Geysers, CA",
                                                        "time": 1620439020, "url": "xxx"},
                                         "geometry": {"type": "Point", "coordinates": [-120.8133, 49.1893]}},
                                        {"properties": {"mag": 1.2, "title": "1km ENE of The Geysers, CA",
                                                        "time": 1620439020, "url": "xxx"},
                                         "geometry": {"type": "Point", "coordinates": [-120.8133, 49.1893]}}
                                        ]}
        earthquakes = [Earthquake(title='1km ENE of The Geysers, CA', magnitude=1.2,
                                  longitude=-120.8133, latitude=49.1893, time=1620439020, detail_url='xxx'),
                       Earthquake(title='1km ENE of The Geysers, CA', magnitude=1.2, longitude=-120.8133,
                                  latitude=49.1893, time=1620439020, detail_url='xxx')]
        with mock.patch('vancouver_earthquake.storage.data_handler.earthquake_encoder') as mock_earthquake_encoder:
            mock_earthquake_encoder.return_value = earthquakes
            actual_value = earthquake_encoder(earthquake_dict)
            self.assertEqual(actual_value, earthquakes)

    def test_earthquake_decoder(self):
        earthquakes = [Earthquake(title='1km ENE of The Geysers, CA', magnitude=1.2,
                                  longitude=-120.8133, latitude=49.1893, time=1620439020, detail_url='xxx'),
                       Earthquake(title='1km ENE of The Geysers, CA', magnitude=1.2, longitude=-120.8133,
                                  latitude=49.1893, time=1620439020, detail_url='xxx')]
        earthquake_dict = {"features": [{"properties": {"mag": 1.2, "time": 1620439020, "url": "xxx",
                                                        "title": "1km ENE of The Geysers, CA"},
                                         "geometry": {"coordinates": [-120.8133, 49.1893]}},
                                        {"properties": {"mag": 1.2, "time": 1620439020, "url": "xxx",
                                                        "title": "1km ENE of The Geysers, CA"},
                                         "geometry": {"coordinates": [-120.8133, 49.1893]}}
                                        ]}
        with mock.patch('vancouver_earthquake.storage.data_handler.earthquake_decoder') as mock_earthquake_decoder:
            mock_earthquake_decoder.return_value = earthquake_dict
            actual_value = earthquake_decoder(earthquakes)
            self.assertEqual(actual_value, earthquake_dict)


if __name__ == '__main__':
    unittest.main()
