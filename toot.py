import os
from mastodon import Mastodon
from earthquake.earthquake import get_earthquake_title, get_earthquake_info
from draw.draw_earthquake import draw_earthquake_points


USER = os.getenv('ACCOUNT_EMAIL')
PASSWORD = os.getenv('PASSWORD')
MASTODON_SERVER = os.getenv('MASTODON_SERVER')


def connect_to_mastodon():
    """ Create a connection to your server. And provide account credential. """

    Mastodon.create_app(
        'pytooterapp',
        api_base_url=MASTODON_SERVER,
        to_file='pytooter_clientcred.secret'
    )

    mastodon = Mastodon(client_id='pytooter_clientcred.secret',)
    mastodon.log_in(
        USER,
        PASSWORD)
    return mastodon


def send_new_status_for(earthquake_title: str, earthquake_map_path: str):
    """ Post Earthquake status and Earthquake recent map. """

    mastodon = connect_to_mastodon()

    image_id = mastodon.media_post(earthquake_map_path)
    post_dict = mastodon.status_post(
        earthquake_title, in_reply_to_id=None, media_ids=image_id)
    print("post id: ", post_dict.id)


if __name__ == '__main__':

    image_path = "./assets/vancouver_base_map.png"
    output_path = "./outputs/vancouver_earthquake_map.png"

    earthquake_data = get_earthquake_info()
    earthquake_info = get_earthquake_title()

    if not len(earthquake_data) == 0 and not earthquake_info == 0:
        draw_earthquake_points(image_path, output_path, earthquake_data)
        send_new_status_for(earthquake_info, output_path)
