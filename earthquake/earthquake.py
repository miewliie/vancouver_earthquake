import json
from datetime import datetime
import pytz

TOP = 53.7827
BOTTOM = 44.7827
LEFT = -132.2207
RIGHT = -114.0207


def read_json_output():
    with open('./outputs/earthquake.json', "r", encoding="utf-8") as output_file:
        data = json.loads(output_file.read())
        return data


def get_earthquake_info():
    earthquake_data = read_json_output()
    features = earthquake_data["features"]
    earthquake_info = []
    for obj in features:
        properties = obj["properties"]
        x_longitude = obj["geometry"]["coordinates"][0]
        y_latitude = obj["geometry"]["coordinates"][1]

        coordinates = []
        if RIGHT > x_longitude > LEFT and TOP > y_latitude > BOTTOM:
            coordinates.append(x_longitude)
            coordinates.append(y_latitude)
            coordinates.append(properties["mag"])
            earthquake_info.append(coordinates)
    return earthquake_info


def get_earthquake_title():
    earthquake_data = read_json_output()
    features = earthquake_data["features"]
    titles = []
    for obj in features:
        title_dt = []
        properties = obj["properties"]
        temp_title = properties["title"]
        x_longitude = obj["geometry"]["coordinates"][0]
        y_latitude = obj["geometry"]["coordinates"][1]

        if RIGHT > x_longitude > LEFT and TOP > y_latitude > BOTTOM:

            second = properties["time"] / 1000
            utc_datetime = datetime.utcfromtimestamp(second)

            utc_timezone = pytz.timezone('UTC')
            localized_utc_datetime = utc_timezone.localize(utc_datetime)

            vancouver_timezone = pytz.timezone('America/Vancouver')

            vancouver_datetime = localized_utc_datetime.astimezone(vancouver_timezone)
            temp_datetime = vancouver_datetime.strftime("%Y-%m-%d %H:%M:%S")

            title_dt.append(temp_title)
            title_dt.append(str(temp_datetime))
            title_dt.append('Vancouver Time')

            str_title_dt = ' : '.join(title_dt)
            titles.append(str_title_dt)

    if len(titles) > 0:
        titles.append("#Vancouver #VancouverEarthquake #Earthquake #EarthquakeVancouver")
        title = '\n'.join(titles)
        print("total title char: ", len(title))
        # print(title)
        return title
    else:
        title = titles
    return title



