import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")


window = tk.Tk()

main_menu = tk.Menu(window)
window.config(menu=main_menu)
sub_menu_file = tk.Menu(main_menu)
# setting the hotkey to "Alt-F"
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
sub_menu_help = tk.Menu(main_menu)
# setting the hotkey to "Alt-B"
main_menu.add_command(label="About...", command=about_app, underline=1)

window.mainloop()
