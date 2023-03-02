TOP = 53.7827
BOTTOM = 44.7827
LEFT = -132.2207
RIGHT = -114.0207


def convert_lon_to_x_pixel(image_width: float, longitude: float):
    range_of_x = RIGHT - LEFT
    norm_value = longitude - LEFT
    pct_of_x = norm_value / range_of_x
    xp = pct_of_x * image_width
    return xp

