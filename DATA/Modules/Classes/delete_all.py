from tkinter import *


def delete_all():
    global arithmetic_label, arithmetic_text, arithmetic_entry, arithmetic_button

    try:
        arithmetic_label.place_forget()
        arithmetic_entry.place_forget()
        arithmetic_button.place_forget()
        arithmetic_text.place_forget()
    except:
        pass
