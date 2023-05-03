import unittest
from unittest import mock

from vancouver_earthquake.core.earthquake import Earthquake
from vancouver_earthquake.main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        old_path = "../outputs/old_earthquake.json"

        earthquakes: list[Earthquake] = ['test_earthquake', 'test_earthquake']

        with mock.patch('vancouver_earthquake.main.network_manager',
                        return_value=earthquakes) as mock_network_manager, \
                mock.patch('vancouver_earthquake.main.in_boundary',
                           return_value=earthquakes) as mock_in_boundary, \
                mock.patch('vancouver_earthquake.main.filter_out_duplicate_earthquake',
                           return_value=earthquakes) as mock_filter, \
                mock.patch('vancouver_earthquake.main.storage_manager',
                           return_value=earthquakes) as mock_storage_manager, \
                mock.patch('vancouver_earthquake.main.social_manager') as mock_social_manager:
            main()
            result = mock_network_manager.get_earthquake_data()
            mock_in_boundary.assert_called_once_with(earthquakes=result)
            mock_storage_manager.read_earthquake_data.assert_called_once_with(old_eq_path=old_path)
            mock_storage_manager.write_earthquake_data.assert_called_once_with(new_eq=earthquakes, old_path=old_path)
            mock_filter.filter_out_duplicate_earthquake(new_eq=earthquakes, old_eq=earthquakes)
            mock_social_manager.assert_called_once_with(earthquakes=earthquakes)


if __name__ == '__main__':
    unittest.main()
