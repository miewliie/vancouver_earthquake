from core.earthquake import Earthquake
from core.earthquake_api import fetch_earthquakes
from storage.data_handler import earthquake_encoder

""" This module provides functions to get earthquake data from API."""


def get_earthquake_data() -> list[Earthquake]:
    """ Get earthquake data from API. """
    data = fetch_earthquakes()
    return earthquake_encoder(earthquake_data=data)

