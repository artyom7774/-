from DATA.Modules.Functions.delete import deleted
from functools import partial
from tkinter import *
import json

def save(item_name, text, marks):

    deleted(text=text)

    if item_name.get() == "":
        text.delete(1.0, END)
        text.insert(1.0, "Название предмета не может быть пустым.")
        return 0

    for i in range(len(marks)):
        element = marks[i]

        if element["name"] == item_name.get():
            marks.pop(i)
            break

    mark = text.get(1.0, END)
    mark = mark.split()
    mark = list(mark)

    i = []
    for element in mark:
        if element != " ":
            i.append(element)

    mark = i

    marks.append({"name": item_name.get(), "marks": mark})

    with open("DATA/items.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(marks, indent=4))


def get(item_name, text, marks):
    deleted(text=text)

    text.delete(1.0, END)

    try:
        for i in marks:
            if i["name"] == item_name.get():
                mark = i
                break

        for element in mark["marks"]:
            if element != " ":
                text.insert(1.0, f"{element} ")

        if len(mark["marks"]) == 0:
            text.insert(1.0, f"Нет отметок.")

    except:
        text.insert(1.0, "Предмет не найден.")


def delete_text(item_name, text, marks):
    text.delete(1.0, END)


def delete_mark(item_name, text, marks):
    deleted(text=text)

    text.delete(1.0, END)

    if type(marks) != list:
        text.insert(1.0, "Предметы не найдены.")
        return 0

    for i in range(len(marks)):
        mark = marks[i]

        if mark["name"] == item_name.get():
            text.insert(1.0, f"Предмет удалён.")

            marks.pop(i)
            break
    else:
        text.insert(1.0, f"Имя предмета не найдено.")

    with open("DATA/items.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(marks, indent=4))


def check(item_name, text, marks, average):
    deleted(text=text)

    mark = text.get(1.0, END)
    mark = mark.split()
    mark = list(mark)

    i = []
    for element in mark:
        if element != " ":
            i.append(element)

    mark = i

    var = 0
    for element in mark:
        var += int(element)

    if len(mark) == 0:
        return 0

    get = var / len(mark)

    get = round(get, 2)

    average.delete(0, END)
    average.insert(END, f"{get}")
    if get != float(round(get)):
        average.insert(END, f" -> {round(get)}")
