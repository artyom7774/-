from DATA.Modules.Functions.delete import *
from tkinter import *
import json


def five(settings):
    settings["max_number"] = 5

    with open("DATA/settings.json", "w") as file:
        file.write(json.dumps(settings, indent=4))


def ten(settings):
    settings["max_number"] = 10

    with open("DATA/settings.json", "w") as file:
        file.write(json.dumps(settings, indent=4))


def twelve(settings):
    settings["max_number"] = 12

    with open("DATA/settings.json", "w") as file:
        file.write(json.dumps(settings, indent=4))


def number_1(text):
    deleted(text)

    text.insert(END, "1 ")


def number_2(text):
    deleted(text)

    text.insert(END, "2 ")


def number_3(text):
    deleted(text)

    text.insert(END, "3 ")


def number_4(text):
    deleted(text)

    text.insert(END, "4 ")


def number_5(text):
    deleted(text)

    text.insert(END, "5 ")


def number_6(text):
    deleted(text)

    text.insert(END, "6 ")


def number_7(text):
    deleted(text)

    text.insert(END, "7 ")


def number_8(text):
    deleted(text)

    text.insert(END, "8 ")


def number_9(text):
    deleted(text)

    text.insert(END, "9 ")


def number_10(text):
    deleted(text)

    text.insert(END, "10 ")


def number_11(text):
    deleted(text)

    text.insert(END, "11 ")


def number_12(text):
    deleted(text)

    text.insert(END, "12 ")
