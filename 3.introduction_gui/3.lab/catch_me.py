import tkinter as tk
import random


def move_button(event):
    # Obtenha a largura e altura da janela
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    # Define o tamanho do botão
    button_width = 100
    button_height = 50

    # Calcula as novas coordenadas, certificando-se de que o botão não sai da janela
    new_x = random.randint(0, window_width - button_width)
    new_y = random.randint(0, window_height - button_height)

    # Move o botão para as novas coordenadas
    button.place(x=new_x, y=new_y)


# Configura a janela principal
window = tk.Tk()
window.geometry("500x500")

# Cria o botão e o posiciona no topo esquerdo
button = tk.Button(window, text="Catch me!")
button.place(x=0, y=0)

# Vincula o evento de mover o mouse sobre o botão à função move_button
button.bind("<Enter>", move_button)

# Inicia o loop principal da interface
window.mainloop()
