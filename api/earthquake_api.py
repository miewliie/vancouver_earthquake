import requests
import json
from datetime import date, timedelta


START_DATE = date.today().isoformat()
END_DATE = (date.today()+timedelta(days=1)).isoformat()
# vancouver lat & long
LATITUDE = '49.246292'
LONGITUDE = '-123.116226'
MAX_RADIUS_KM = '1000'
EVENT_TYPE = 'earthquake'
MIN_MAGNITUDE = '3.0'
USGS_API = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"


def get_earthquakes():
    response = requests.get(USGS_API + '&starttime=' + START_DATE + '&endtime=' + END_DATE + '&latitude=' + LATITUDE +
                            '&longitude=' + LONGITUDE + '&maxradiuskm=' + MAX_RADIUS_KM + '&eventtype=' + EVENT_TYPE +
                            '&minmagnitude=' + MIN_MAGNITUDE)
    json_data = response.json()

    return json_data


def write_response(data):
    with open('../outputs/earthquake.json', "w", encoding="utf-8") as output_file:
        json.dump(data, output_file)
        print("success write earthquake data to outputs")


if __name__ == '__main__':
    earthquake_data = get_earthquakes()
    write_response(earthquake_data)
