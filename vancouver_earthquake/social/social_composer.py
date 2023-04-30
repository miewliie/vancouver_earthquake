from datetime import datetime
import pytz
from vancouver_earthquake.core.earthquake import Earthquake
from vancouver_earthquake.draw.draw_earthquake import draw_earthquake_points

image_path = "../assets/vancouver_base_map.png"
output_path = "../outputs/vancouver_earthquake_map.png"


def compose_message(earthquakes: list[Earthquake]) -> str:
    """ This function will compose the message for earthquake. """

    titles: list[str] = []
    for earthquake in earthquakes:
        title_date_time: list[str] = []

        second = earthquake.time / 1000
        utc_datetime = datetime.utcfromtimestamp(second)
        utc_timezone = pytz.timezone('UTC')
        localized_utc_datetime = utc_timezone.localize(utc_datetime)
        vancouver_timezone = pytz.timezone('America/Vancouver')
        vancouver_datetime = localized_utc_datetime.astimezone(vancouver_timezone)
        temp_datetime = vancouver_datetime.strftime("%Y-%m-%d %H:%M:%S")

        title_date_time.append(earthquake.title)
        title_date_time.append(str(temp_datetime))

        title_date_time.append('Vancouver Time')

        one_eq_title: str = ' : '.join(title_date_time)
        titles.append(one_eq_title)

    titles.append("#Vancouver #VancouverEarthquake #Earthquake #EarthquakeVancouver")
    title = '\n'.join(titles)
    return title


def create_map(earthquake: list[Earthquake]) -> str:
    """ This function will create the map for earthquake. """
    draw_earthquake_points(image_path=image_path, output_path=output_path, earthquake_data=earthquake)
    return output_path
