from tkinter import *


def deleted(text):
    a = ord('а')
    vars = ''.join([chr(i) for i in range(a, a + 32)])

    for _ in range(5):
        txt = text.get(1.0, END)
        for i in range(len(txt)):
            element = txt[i]

            for var in vars:
                if var == element:
                    text.delete(float(f"1.{i}"), float(f"1.{i + 1}"))
                    try:
                        text.delete(float(f"1.{i - 1}"), float(f"1.{i}"))
                    except:
                        pass
