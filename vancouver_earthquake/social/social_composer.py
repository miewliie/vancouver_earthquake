from datetime import datetime
import pytz
from core.earthquake import Earthquake
from draw.draw_earthquake import draw_earthquake_points

image_path = "../assets/vancouver_base_map.png"
output_path = "../outputs/vancouver_earthquake_map.png"


def compose_message(earthquakes: list[Earthquake]) -> str:
    """ Composes the message zfor the social status update. """

    lines: list[str] = []
    for earthquake in earthquakes:
        utc_datetime: datetime = datetime.utcfromtimestamp(earthquake.time / 1000)
        vancouver_datetime = pytz.timezone('UTC').localize(utc_datetime).astimezone(pytz.timezone('America/Vancouver'))
        formatted_time: str = vancouver_datetime.strftime("%Y-%m-%d %H:%M:%S")

        message: str = f"{earthquake.title} : {formatted_time} : Vancouver Time"
        lines.append(message)

    lines.append("#Vancouver #VancouverEarthquake #Earthquake #EarthquakeVancouver")

    status_message: str = '\n'.join(lines)
    return status_message


def create_map(earthquakes: list[Earthquake]) -> str:
    """ This function will create the map for earthquake. """
    result_output_path: str = draw_earthquake_points(base_image_path=image_path, output_path=output_path, earthquakes=earthquakes)
    return result_output_path
