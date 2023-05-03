from PIL import Image, ImageDraw

from core.earthquake import Earthquake

TOP = 53.7827
BOTTOM = 44.7827
LEFT = -132.2207
RIGHT = -114.0207

""" This module provides functions to draw earthquake points on the map."""


def convert_lon_to_x_pixel(image_width: float, longitude: float) -> float:
    """ Convert longitude to x pixel."""
    range_of_x: float = RIGHT - LEFT
    norm_value: float = longitude - LEFT
    pct_of_x: float = norm_value / range_of_x
    xp: float = pct_of_x * image_width
    return xp


def convert_lat_to_y_pixel(image_height: float, latitude: float) -> float:
    """ Convert latitude to y pixel."""
    range_of_y: float = TOP - BOTTOM
    norm_value: float = latitude - BOTTOM
    pct_of_y: float = norm_value / range_of_y
    yp: float = image_height - (pct_of_y * image_height)
    return yp


def draw_earthquake_points(base_image_path: str, output_path: str, earthquakes: list[Earthquake]) -> str:
    """ This function will draw earthquake longitude and latitude on the base map."""
    image: Image = Image.open(base_image_path).convert('RGBA')
    im_width: int = image.size[0]
    im_height: int = image.size[1]
    draw: ImageDraw = ImageDraw.Draw(image)

    for earthquake in earthquakes:
        x_longitude: float = earthquake.longitude
        y_latitude: float = earthquake.latitude
        magnitude: float = earthquake.magnitude

        lon_x_pixel: float = convert_lon_to_x_pixel(image_width=im_width, longitude=x_longitude)
        lat_y_pixel: float = convert_lat_to_y_pixel(image_height=im_height, latitude=y_latitude)

        radius: float = (magnitude / 1.01 - 0.13) * 15
        if magnitude >= 6:
            draw.ellipse((lon_x_pixel - radius, lat_y_pixel - radius, lon_x_pixel +
                          radius, lat_y_pixel + radius), fill='#9d43f7', outline='#bc81f7', width=30)
        elif magnitude >= 5:
            draw.ellipse((lon_x_pixel - radius, lat_y_pixel - radius, lon_x_pixel +
                          radius, lat_y_pixel + radius), fill='#f2111c', outline='#fa7078', width=25)
        elif magnitude >= 4:
            draw.ellipse((lon_x_pixel - radius, lat_y_pixel - radius, lon_x_pixel +
                          radius, lat_y_pixel + radius), fill='#faa125', outline='#f7ce94', width=20)
        else:
            draw.ellipse((lon_x_pixel - radius, lat_y_pixel - radius, lon_x_pixel +
                          radius, lat_y_pixel + radius), fill='#26d152', outline='#7df59b', width=20)

    image.save(output_path)
    return output_path

