import unittest
import unittest.mock as mock
from vancouver_earthquake.storage.storage_manager import read_earthquake_data, write_earthquake_data
from vancouver_earthquake.core.earthquake import Earthquake


class TestStorageManager(unittest.TestCase):

    def test_read_earthquake_data(self):
        test_path: str = 'test_path'
        test_json: str = 'test_json'
        test_earthquake: list[Earthquake] = ['test_earthquake', 'test_earthquake']

        with mock.patch('vancouver_earthquake.storage.storage_manager.json_handler.read_json',
                        return_value=test_json) as mock_read_json, \
                mock.patch('vancouver_earthquake.storage.storage_manager.json_handler.earthquake_encoder',
                           return_value=test_earthquake) as mock_encoder:
            value = read_earthquake_data(old_eq_path=test_path)
            mock_read_json.assert_called_once_with(file_path=test_path)
            mock_encoder.assert_called_once_with(test_json)
            self.assertEqual(value, test_earthquake)

    def test_write_earthquake_data(self):
        test_path: str = 'test_path'
        test_json: str = 'test_json'
        test_earthquake: list[Earthquake] = ['test_earthquake', 'test_earthquake']

        with mock.patch('vancouver_earthquake.storage.storage_manager.json_handler.earthquake_decoder',
                        return_value=test_json) as mock_decoder, \
                mock.patch('vancouver_earthquake.storage.storage_manager.json_handler.write_json') as mock_write_json:
            write_earthquake_data(new_eq=test_earthquake, old_path=test_path)
            mock_decoder.assert_called_once_with(earthquakes=test_earthquake)
            mock_write_json.assert_called_once_with(test_json, test_path)


if __name__ == '__main__':
    unittest.main()
