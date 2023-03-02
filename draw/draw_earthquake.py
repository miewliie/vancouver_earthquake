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


def convert_lat_to_y_pixel(image_height: float, latitude: float):
    range_of_y = TOP - BOTTOM
    norm_value = latitude - BOTTOM
    pct_of_y = norm_value / range_of_y
    yp = image_height - (pct_of_y * image_height)
    return yp

