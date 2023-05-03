import unittest
from unittest import mock

from vancouver_earthquake.core.earthquake import Earthquake
from vancouver_earthquake.draw.draw_earthquake import convert_lon_to_x_pixel, \
    convert_lat_to_y_pixel, draw_earthquake_points, Image, ImageDraw


class TestDrawEarthquake(unittest.TestCase):

    def test_convert_lon_to_x_pixel(self):
        im_width = 1672
        longitude = -123.1207
        expected_result = 836.0

        x_pixel = convert_lon_to_x_pixel(image_width=im_width, longitude=longitude)
        self.assertEqual(expected_result, x_pixel)

    def test_convert_lat_to_y_pixel(self):
        im_height = 1280
        latitude = 49.2827
        expected_result = 640.0

        y_pixel = convert_lat_to_y_pixel(image_height=im_height, latitude=latitude)
        self.assertEqual(expected_result, y_pixel)

    def test_draw_earthquake_points(self):
        output_path: str = "output_test/vancouver_earthquake_map.png"
        base_image_path: str = "assets/vancouver_base_map.png"
        earthquakes: list[Earthquake] = [Earthquake(title='M 3.4 - 37 km SW of Princeton, Canada',
                                                    magnitude=3.4, longitude=-120.8133,
                                                    latitude=49.1893, time=1682702356267,
                                                    detail_url='https://earthquake.usgs.gov/earthquakes/eventpage'
                                                               '/us7000jwrg')] * 2
        x: float = 836.0
        y: float = 640.0

        with mock.patch('vancouver_earthquake.draw.draw_earthquake.Image.open') as mock_open:
            mock_open.Image.convert.return_value = mock.MagicMock(spec=Image, size=(1672, 1280), mode='RGBA')
            with mock.patch('vancouver_earthquake.draw.draw_earthquake.ImageDraw.Draw') as mock_draw:
                mock_draw.ellipse.return_value = mock.MagicMock(spec=ImageDraw)
                actual_result = draw_earthquake_points(base_image_path=base_image_path,
                                                       output_path=output_path, earthquakes=earthquakes)

                mock_open.assert_called_once_with(base_image_path)
                mock_draw.assert_called_once()
                self.assertEqual(actual_result, output_path)


if __name__ == '__main__':
    unittest.main()
