import tkinter
from tkinter import messagebox


def click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        skylight.destroy()


skylight = tkinter.Tk()
skylight.title("Skylight")
button = tkinter.Button(skylight, text="Bye!", command=click)
button.place(x=10, y=10)
skylight.mainloop()
