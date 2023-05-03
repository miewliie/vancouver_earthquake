import os
import json
from typing import Any

from core.earthquake import Earthquake

""" This module provides functions to handle earthquake data."""


def read_json(file_path: str):
    """ Read data from json file."""
    with open(file_path, 'r', encoding='utf-8') as output_file:
        size = os.path.getsize(file_path)
        return json.loads(output_file.read()) if size > 0 else None


def write_json(data:  dict[str, Any], file_path: str):
    """ Write data to json file."""
    with open(file_path, 'w', encoding='utf-8') as output_file:
        json.dump(data, output_file)
        print("Done write response into json file")


def from_dict_to_earthquake(dict_data: dict[str, Any]) -> Earthquake:
    """ Convert dictionary data to Earthquake object. """
    return Earthquake(
        magnitude=dict_data['properties']['mag'],
        time=dict_data['properties']['time'],
        detail_url=dict_data['properties']['url'],
        title=dict_data['properties']['title'],
        longitude=dict_data['geometry']['coordinates'][0],
        latitude=dict_data['geometry']['coordinates'][1]
    )


def to_dict(earthquake: Earthquake) -> dict[str, Any]:
    """ Convert Earthquake object to dictionary. """
    return {
        'properties': {
            'mag': earthquake.magnitude,
            'time': earthquake.time,
            'url': earthquake.detail_url,
            'title': earthquake.title
        },
        'geometry': {
            'coordinates': [earthquake.longitude, earthquake.latitude]
        }
    }


def earthquake_encoder(earthquake_data: dict[str, Any]) -> list[Earthquake]:
    """ Convert dictionary into list of Earthquake objects. """
    earthquakes_json: list[dict[str, Any]] = earthquake_data['features']
    earthquakes: list[Earthquake] = []
    for dict_obj in earthquakes_json:
        earthquakes.append(from_dict_to_earthquake(dict_data=dict_obj))
    return earthquakes


def earthquake_decoder(earthquakes: list[Earthquake]) -> dict[str, Any]:
    """ Convert list of Earthquake objects into dictionary. """
    json_list = []
    for earthquake in earthquakes:
        json_list.append(to_dict(earthquake))
    return {"features": json_list}
