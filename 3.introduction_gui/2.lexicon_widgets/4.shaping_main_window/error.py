import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.showerror("!", "Your code does nothing!")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="Alarming message", command=question)
button.pack()
window.mainloop()
