import unittest
from unittest import mock
from vancouver_earthquake.core.earthquake_api import fetch_earthquakes


class TestEarthquakeApi(unittest.TestCase):

    def test_earthquake_api(self):
        expected_result = {'key': 'value'}

        response_mock = mock.Mock()
        with mock.patch('vancouver_earthquake.core.earthquake_api.requests.get',
                        return_value=response_mock) as mock_get:
            mock_get.return_value.json.return_value = expected_result
            result = fetch_earthquakes()
            mock_get.assert_called_once()
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()