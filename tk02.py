from tkinter import *
from tkinter import filedialog


def file():
    filedialog.askopenfilename()


root = Tk()
root.geometry('300x300')
root.title("File dialog")
root.resizable(False, False)

Button(text="File dialog", command=file).pack(fill=X)

root.mainloop()
