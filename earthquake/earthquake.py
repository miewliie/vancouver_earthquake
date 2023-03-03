import json


def read_json_output():
    with open('./outputs/earthquake.json', "r", encoding="utf-8") as output_file:
        data = json.loads(output_file.read())
        return data


def get_earthquake_title():
    earthquake_data = read_json_output()
    features = earthquake_data["features"]
    titles = []
    for obj in features:
        properties = obj["properties"]
        titles.append(properties["title"])
    title = '\n'.join(titles)
    print("total title char: ", len(title))
    return title



