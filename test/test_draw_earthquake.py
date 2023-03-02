import unittest
from draw.draw_earthquake import convert_lon_to_x_pixel, convert_lat_to_y_pixel


class TestDrawEarthquake(unittest.TestCase):

    def test_convert_lon_to_x_pixel(self):
        im_width = 1672
        longitude = -123.1207

        x_pixel = convert_lon_to_x_pixel(im_width, longitude)
        self.assertEqual(836.0, x_pixel)

    def test_convert_lat_to_y_pixel(self):
        im_height = 1280
        latitude = 49.2827

        y_pixel = convert_lat_to_y_pixel(im_height, latitude)
        self.assertEqual(640.0, y_pixel)


if __name__ == '__main__':
    unittest.main()
