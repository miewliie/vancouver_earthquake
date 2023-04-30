import os
from typing import Any

import requests
import json
from datetime import date, timedelta


START_DATE = '2023-04-10'
# START_DATE = date.today().isoformat()
END_DATE = (date.today()+timedelta(days=1)).isoformat()
# vancouver lat & long
LATITUDE = '49.246292'
LONGITUDE = '-123.116226'
MAX_RADIUS_KM = '1000'
EVENT_TYPE = 'earthquake'
MIN_MAGNITUDE = '3.0'
USGS_API = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"


def fetch_earthquakes():
    """ This function will return earthquake json data from USGS API."""

    response = requests.get(USGS_API + '&starttime=' + START_DATE + '&endtime=' + END_DATE + '&latitude=' + LATITUDE +
                            '&longitude=' + LONGITUDE + '&maxradiuskm=' + MAX_RADIUS_KM + '&eventtype=' + EVENT_TYPE +
                            '&minmagnitude=' + MIN_MAGNITUDE)
    json_data = response.json()
    return json_data







