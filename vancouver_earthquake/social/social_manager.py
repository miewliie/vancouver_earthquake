from vancouver_earthquake.core.earthquake import Earthquake
from vancouver_earthquake.social.social_composer import compose_message, create_map
from vancouver_earthquake.social.toot import send_new_toot, MastodonError
from vancouver_earthquake.social.tweet import send_new_tweet

""" This module provides functions to handle social media."""


def social_manager(earthquakes: list[Earthquake]):
    """ This function will manage the social media. """
    image_path: str = create_map(earthquakes=earthquakes)
    message: str = compose_message(earthquakes=earthquakes)

    print(image_path, ' ', message)
    try:
        send_new_toot(message=message, image_path=image_path)
    except MastodonError:
        pass
    try:
        send_new_tweet(message=message, image_path=image_path)
    except Exception:
        pass