from typing import NamedTuple

""" This module provides Earthquake data structure."""


class Earthquake(NamedTuple):
    """ Earthquake data structure. """

    title: str
    """ Earthquake title. """

    magnitude: float
    """ Earthquake magnitude. """

    longitude: float
    """ Earthquake longitude. """

    latitude: float
    """ Earthquake latitude. """

    time: int
    """ Earthquake time. """

    detail_url: str
    """ Earthquake detail url. """




