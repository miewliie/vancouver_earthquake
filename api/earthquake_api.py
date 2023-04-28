import os

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
    """ This function will return earthquake json data from USGS API."""

    response = requests.get(USGS_API + '&starttime=' + START_DATE + '&endtime=' + END_DATE + '&latitude=' + LATITUDE +
                            '&longitude=' + LONGITUDE + '&maxradiuskm=' + MAX_RADIUS_KM + '&eventtype=' + EVENT_TYPE +
                            '&minmagnitude=' + MIN_MAGNITUDE)
    json_data = response.json()
    return json_data


def write_json(data: object, file_path: str):
    with open(file_path, 'w', encoding='utf-8') as output_file:
        json.dump(data, output_file)
        print("Done write response into json file")


def read_json(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as output_file:
        size = os.path.getsize(file_path)
        if size > 0:
            data = json.loads(output_file.read())
        else:
            data = None
        return data


def get_duplicate_earthquake(new_earthquake, old_earthquake_path: str):
    """ This function will return the index of the duplicate data. """

    old_earthquake = read_json(old_earthquake_path)
    old_earthquake = old_earthquake['features']

    new_earthquake = new_earthquake['features']

    dup_index_list = []
    if old_earthquake and new_earthquake:
        for i in range(len(new_earthquake)):
            new_eq = new_earthquake[i]['properties']
            new_lat = new_earthquake[i]['geometry']['coordinates'][1]
            new_long = new_earthquake[i]['geometry']['coordinates'][0]

            for old_eq in old_earthquake:
                old_eq_prop = old_eq['properties']
                old_lat = old_eq['geometry']['coordinates'][1]
                old_long = old_eq['geometry']['coordinates'][0]

                if new_eq['mag'] == old_eq_prop['mag'] and new_eq['time'] == old_eq_prop['time'] and new_lat == old_lat and \
                        new_long == old_long:
                    dup_index_list.insert(0, i)
                    break
        return dup_index_list
    else:
        return dup_index_list


def filter_duplicate_earthquake(index_list: list, new_earthquake, output_path: str):
    """ Use duplication index list to remove the duplicate data out from latest response. """

    if not index_list == []:
        new_earthquake = new_earthquake['features']
        for i in range(len(index_list)):
            del new_earthquake[index_list[i]]

        write_json(new_earthquake, output_path)

    else:
        write_json(new_earthquake, output_path)


if __name__ == '__main__':
    prev_earthquake_path = '../outputs/earthquake.json'

    # get data from api
    recent_earthquake = get_earthquakes()

    if recent_earthquake:
        duplicated_list = get_duplicate_earthquake(recent_earthquake, prev_earthquake_path)
        filter_duplicate_earthquake(duplicated_list, recent_earthquake, prev_earthquake_path)
