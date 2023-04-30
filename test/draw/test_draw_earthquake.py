import unittest
from vancouver_earthquake.draw.draw_earthquake import convert_lon_to_x_pixel, convert_lat_to_y_pixel, draw_earthquake_points
from os import path
import json


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

    def test_draw_earthquake_points(self):
        output_path = "../output_test/vancouver_earthquake_map.png"
        base_image_path = "../../assets/vancouver_base_map.png"

        with open('../test_data/lat_lon_earthquake.json', "r", encoding="utf-8") as output_file:
            earthquake_test_data = json.loads(output_file.read())

        draw_earthquake_points(base_image_path, output_path, earthquake_test_data)
        self.assertTrue(path.exists('../output_test/vancouver_earthquake_map.png'),
                        'Vancouver earthquake map is not exist in output')


if __name__ == '__main__':
    unittest.main()
