from PIL import Image, ImageDraw

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


def draw_earthquake_points(image_path, output_path, earthquake_data):
    image = Image.open(image_path).convert('RGBA')
    im_width = image.size[0]
    im_height = image.size[1]
    draw = ImageDraw.Draw(image)

    features_obj = earthquake_data["features"]
    for obj in features_obj:
        properties_obj = obj["properties"]
        x_longitude = obj["geometry"]["coordinates"][0]
        y_latitude = obj["geometry"]["coordinates"][1]
        magnitude = properties_obj["mag"]

        lon_x_pixel = convert_lon_to_x_pixel(im_width, x_longitude)
        lat_y_pixel = convert_lat_to_y_pixel(im_height, y_latitude)

        radius = (magnitude / 1.01 - 0.13) * 15
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


