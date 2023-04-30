import os
from mastodon import Mastodon, MastodonError

USER = os.getenv('ACCOUNT_EMAIL')
PASSWORD = os.getenv('PASSWORD')
MASTODON_SERVER = os.getenv('MASTODON_SERVER')

""" This module provides functions to toot earthquake status and map."""


def connect_to_mastodon():
    """ Create a connection to mastodon server. """

    Mastodon.create_app(
        'pytooterapp',
        api_base_url=MASTODON_SERVER,
        to_file='../../pytooter_clientcred.secret'
    )

    mastodon: Mastodon = Mastodon(client_id='pytooter_clientcred.secret',)
    mastodon.log_in(
        USER,
        PASSWORD)
    return mastodon


def send_new_toot(message: str, image_path: str):
    """ Toot Earthquake status and Earthquake recent map. """

    mastodon: Mastodon = connect_to_mastodon()

    image_id = mastodon.media_post(image_path)
    post_dict = mastodon.status_post(status=message, in_reply_to_id=None, media_ids=image_id)
    print("post id: ", post_dict.id)


