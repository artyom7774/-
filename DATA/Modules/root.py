from DATA.Modules.Functions.number import five, ten, twelve
from DATA.Modules.Classes import arithmetic
from DATA.Modules.Functions import button
from DATA.Modules.Functions import number

from DATA.Modules.Functions.file import *
from tkinter import *

from functools import partial


def get_menu_func(marks, item_name, text, i):
    item_name.delete(0, END)
    text.delete(1.0, END)

    try:
        name = marks[i]["name"]
        mark = marks[i]["marks"]
    except IndexError:
        text.insert(1.0, "Предмет не найден.")
        return 0

    item_name.insert(0, name)
    for i in range(len(mark)):
        element = mark[i]

        text.insert(1.0, f"{element} ")


def check_keys(event: Event):
    if event.char.isalpha() or (event.state & 4 and event.keysym == "v"):
        return "break"


class Settings(object):
    def __init__(self):
        self.__last_versions = [
            "beta 0.1",
            "beta 0.2",
            "beta 0.3"
        ]
        self.__version = "build 0.1"
        self.__author = "Артём"

    def get_version(self):
        return self.__version


class Root(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        global marks, item_name, text

        start()
        marks, settings = load()

        self.wm_title("Отметки")
        self.wm_geometry("450x620+500+100")
        self.wm_resizable(width=False, height=False)
        self.wm_iconphoto(False, PhotoImage(file="DATA/icon.ico"))

        self.settings = Settings()

        # ---> Label <---

        Label(text="Название предмета: ", font=("Arial", 10)).place(x=22, y=5)
        Label(text="Средний балл: ", font=("Arial", 10)).place(x=22, y=243)
        Label(text=f"Version: {self.settings.get_version()}", font=("Arial", 10)).place(x=22, y=573)

        # ---> Entry <---

        item_name = Entry(width=45)
        item_name.place(x=150, y=7.5)

        average = Entry(width=32)
        average.place(x=120, y=245)

        # ---> Text <---

        text = Text(width=50, height=10)
        text.place(x=22, y=70)

        text.bind("<Key>", check_keys)

        # ---> Menu <---

        number_menu = Menu(tearoff=0)
        number_menu.add_command(label="5", command=partial(five, settings))
        number_menu.add_command(label="10", command=partial(ten, settings))
        number_menu.add_command(label="12", command=partial(twelve, settings))

        get_menu = Menu(tearoff=0)
        for i in range(len(marks)):
            get_menu.add_command(label=marks[i]["name"], command=partial(get_menu_func,
                                                                         marks, item_name, text, i))

        settings_menu = Menu(tearoff=0)
        settings_menu.add_cascade(label="Максимальная отметка ...", menu=number_menu)

        view_menu = Menu(tearoff=0)
        view_menu.add_command(label="Что получить для ...", command=partial(arithmetic.arithmetic_func, text, settings))

        file_menu = Menu(tearoff=0)
        file_menu.add_command(label="Save", command=partial(save, marks, settings))
        file_menu.add_command(label="Load", command=partial(load))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=partial(exit, marks, settings))

        self.main_menu = Menu(tearoff=0)
        self.main_menu.add_cascade(label="File", menu=file_menu)
        self.main_menu.add_cascade(label="View", menu=view_menu)
        self.main_menu.add_cascade(label="Get", menu=get_menu)
        self.main_menu.add_cascade(label="Settings", menu=settings_menu)

        # ---> Buttons <---

        button_save = Button(text="Сохранить", width=12, command=partial(button.save, item_name, text, marks))
        button_save.place(x=330 - 102 * 0, y=34.2)

        button_get = Button(text="Получить", width=12, command=partial(button.get, item_name, text, marks))
        button_get.place(x=330 - 102 * 1, y=34.2)

        button_delete = Button(text="Удалить", width=12, command=partial(button.delete_mark, item_name, text, marks))
        button_delete.place(x=330 - 102 * 2, y=34.2)

        button_delete_text = Button(text="Очистить", width=12, command=partial(button.delete_text, item_name, text, marks))
        button_delete_text.place(x=330 - 102 * 3, y=34.2)

        button_check = Button(text="Посчитать", width=12, command=partial(button.check, item_name, text, marks, average))
        button_check.place(x=330, y=242)

        Button(text="1", width=12, height=2, command=partial(number.number_1, text)).place(x=28 + 100 * 0, y=250 + 50 * 0 + 30)
        Button(text="2", width=12, height=2, command=partial(number.number_2, text)).place(x=28 + 100 * 1, y=250 + 50 * 0 + 30)
        Button(text="3", width=12, height=2, command=partial(number.number_3, text)).place(x=28 + 100 * 2, y=250 + 50 * 0 + 30)
        Button(text="4", width=12, height=2, command=partial(number.number_4, text)).place(x=28 + 100 * 3, y=250 + 50 * 0 + 30)
        Button(text="5", width=12, height=2, command=partial(number.number_5, text)).place(x=28 + 100 * 0, y=250 + 50 * 1 + 30)
        Button(text="6", width=12, height=2, command=partial(number.number_6, text)).place(x=28 + 100 * 1, y=250 + 50 * 1 + 30)
        Button(text="7", width=12, height=2, command=partial(number.number_7, text)).place(x=28 + 100 * 2, y=250 + 50 * 1 + 30)
        Button(text="8", width=12, height=2, command=partial(number.number_8, text)).place(x=28 + 100 * 3, y=250 + 50 * 1 + 30)
        Button(text="9", width=12, height=2, command=partial(number.number_9, text)).place(x=28 + 100 * 0, y=250 + 50 * 2 + 30)

        Button(text="10", width=12, height=2, command=partial(number.number_10, text)).place(x=28 + 100 * 1, y=250 + 50 * 2 + 30)
        Button(text="11", width=12, height=2, command=partial(number.number_11, text)).place(x=28 + 100 * 2, y=250 + 50 * 2 + 30)
        Button(text="12", width=12, height=2, command=partial(number.number_12, text)).place(x=28 + 100 * 3, y=250 + 50 * 2 + 30)

    def update(self):
        self.main_menu.delete(2)

        get_menu = Menu(tearoff=0)
        for i in range(len(marks)):
            get_menu.add_command(label=marks[i]["name"], command=partial(get_menu_func,
                                                                         marks, item_name, text, i))
