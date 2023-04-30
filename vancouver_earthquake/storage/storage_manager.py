import vancouver_earthquake.storage.data_handler as json_handler
from vancouver_earthquake.core.earthquake import Earthquake

old_path = "../outputs/old_earthquake.json"


def read_earthquake_data() -> list[Earthquake]:
    """ Get old earthquake data from previous run. """
    old_eq = json_handler.read_json(old_path)
    return json_handler.earthquake_encoder(old_eq)


def write_earthquake_data(new_eq: list[Earthquake]):
    """ Save latest earthquake data to file. """
    earthquake_json = json_handler.earthquake_decoder(new_eq)
    json_handler.write_json(earthquake_json, old_path)
