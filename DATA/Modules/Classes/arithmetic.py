from DATA.Modules.Classes.delete_all import *
from functools import partial
from tkinter import *


def arithmetic_func(text, settings):
    global arithmetic_label, arithmetic_text, arithmetic_entry, arithmetic_button

    delete_all()

    arithmetic_label = Label(text="Что получить для: ", font=("Arial", 10))
    arithmetic_label.place(x=25, y=450)

    arithmetic_entry = Entry(width=29)
    arithmetic_entry.place(x=142, y=452.5)

    arithmetic_button = Button(text="Посчитать", width=12, command=partial(arithmetic_button_func, text, settings))
    arithmetic_button.place(x=330, y=448)

    arithmetic_text = Text(width=50, height=5)
    arithmetic_text.place(x=22, y=484)


def arithmetic_button_func(text, settings):
    global arithmetic_label, arithmetic_text, arithmetic_entry, arithmetic_button

    number = arithmetic_entry.get()
    arithmetic_text.delete(1.0, END)

    num = 0

    try:
        num = float(number)
    except:
        arithmetic_text.insert(1.0, "Невозможное значение.")
        return 0

    mark = text.get(1.0, END)
    mark = mark.split()
    mark = list(mark)

    i = []
    for element in mark:
        if element != " ":
            i.append(element)

    mark = i

    if len(mark) == 0:
        arithmetic_text.insert(1.0, "Отметки не обнаружены.")
        return 0

    var = 0
    for element in mark:
        var += int(element)

    var = var / len(mark)

    var = round(var, 2)

    if float(var) > float(number):
        arithmetic_text.insert(1.0, "Средний балл больше чем запрашиваемый балл.")
        return 0

    mar = []
    for element in mark:
        mar.append(int(element))

    mark = mar

    out = []

    for element in mark:
        out.append(element)

    if float(number) > float(settings["max_number"]):
        arithmetic_text.insert(1.0, "Невозможно получить.")
        return 0

    for _ in range(10):
        for i in range(settings["max_number"]):
            out.append(i + 1)

            var = 0
            for element in out:
                var += (int(element))

            var = var / len(out)

            if float(var) >= float(number):
                l = []
                for element in out:
                    l.append(int(element))

                for element in mark:
                    l.remove(element)

                for element in l:
                    arithmetic_text.insert(END, f"{element} ")
                return 0

            if i + 1 != settings["max_number"]:
                out.pop(len(out) - 1)
        i = 0

    else:
        arithmetic_text.insert(END, f"Для {number} надо получить болле 10 отметок.")
