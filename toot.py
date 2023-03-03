import json
from draw.draw_earthquake import draw_earthquake_points


def read_json_output():
    with open('./outputs/earthquake.json', "r", encoding="utf-8") as output_file:
        data = json.loads(output_file.read())
        return data


def toot(name):
    print(f'Hi, {name}')


if __name__ == '__main__':

    image_path = "./assets/vancouver_base_map.png"
    output_path = "./outputs/vancouver_earthquake_map.png"

    earthquake_data = read_json_output()
    if not (earthquake_data["metadata"]["count"]) == 0:
        draw_earthquake_points(image_path, output_path, earthquake_data)
        toot('this method is for toot earthquake')
