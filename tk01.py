from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo


def error():
    showerror(message="Error")


def warning():
    showwarning(message="Warning")


def info():
    showinfo(message="Info")


root = Tk()
root.geometry('100x100')
root.title("Show error, warning, info")
root.resizable(False, False)

Button(text="Error", command=error).pack(fill=X)
Button(text="Warning", command=warning).pack(fill=X)
Button(text="Info", command=info).pack(fill=X)

root.mainloop()
