import tkinter as tk

window = tk.Tk()
window.title('Icon?')
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='logo.png'))
window.bind("&lt;Button-1&gt;", lambda e: window.destroy())
window.mainloop()
