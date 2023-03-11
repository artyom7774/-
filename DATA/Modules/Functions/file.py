import json
import sys
import os


def start():
    if os.path.exists("DATA/settings.json"):
        try:
            with open("DATA/settings.json", "r") as file:
                settings = json.load(file)

        except:
            with open("DATA/settings.json", "w") as file:
                settings = {
                    "max_number": 12
                }

                file.write(json.dumps(settings))

    else:
        with open("DATA/settings.json", "w") as file:
            settings = {
                "max_number": 12
            }

            file.write(json.dumps(settings))

    with open("DATA/items.json", "r") as file:
        try:
            marks = json.load(file)
        except:
            marks = []
            with open("DATA/items.json", "w") as file:
                file.write("[]")

    return marks, settings


def load():
    with open("DATA/items.json", "r") as file:
        marks = json.load(file)

    with open("DATA/settings.json", "r") as file:
        settings = json.load(file)

    return marks, settings


def save(marks, settings):
    with open("DATA/items.json", "w") as file:
        file.write(json.dumps(marks, indent=4))

    return marks, settings


def exit(marks, settings):
    save(marks, settings)

    sys.exit()
