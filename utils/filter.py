import json


def load_titles():
    with open("data/keywords.json", "r") as file:
        data = json.load(file)

    return [title.lower() for title in data["titles"]]


def is_matching_job(title):
    title = title.lower()

    for keyword in load_titles():
        if keyword in title:
            return True

    return False