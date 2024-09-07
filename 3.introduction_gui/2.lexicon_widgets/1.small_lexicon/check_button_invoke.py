import tkinter as tk
from tkinter import messagebox


def count():
    global counter
    counter += 1


def show():
    messagebox.showinfo("", "counter=" + str(counter) + ",state=" + str(switch.get()))


window = tk.Tk()
switch = tk.IntVar()
counter = 0

# Botão para mostrar mensagem
button = tk.Button(window, text="Show", command=show)
button.pack()

# Checkbutton que conta as ativações
checkbutton = tk.Checkbutton(window, text="Tick", variable=switch, command=count)
checkbutton.pack()

# Simulando um clique no botão "Show" após 2 segundos
window.after(2000, button.invoke)

# Simulando um clique no Checkbutton após 4 segundos
window.after(4000, checkbutton.invoke)

window.mainloop()
