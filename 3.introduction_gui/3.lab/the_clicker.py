import tkinter as tk
import random


class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("The Clicker Game")

        self.numbers = random.sample(range(1, 1000), 25)  # Gera 25 números únicos
        self.current_number = min(self.numbers)  # Começa com o menor número gerado
        self.buttons = []
        self.timer_running = False
        self.time_elapsed = 0
        self.timer_id = None

        # Cria a grade de botões numerados
        self.create_board()

        # Label do cronômetro
        self.timer_label = tk.Label(root, text="0", font=("Helvetica", 16))
        self.timer_label.grid(row=5, column=0, columnspan=5)

    def create_board(self):
        for i in range(5):
            for j in range(5):
                num = self.numbers[i * 5 + j]
                button = tk.Button(self.root, text=str(num), width=10, height=3)
                button.grid(row=i, column=j)
                button.bind("<Button-1>", self.on_button_click)
                self.buttons.append(button)

    def on_button_click(self, event):
        if not self.timer_running:
            self.start_timer()

        button = event.widget
        number = int(button['text'])

        # Verifica se o número é o próximo na sequência
        if number == self.current_number:
            button.config(state=tk.DISABLED)  # Desabilita o botão clicado
            # Atualiza o próximo número que deve ser clicado
            self.current_number = min([int(b['text']) for b in self.buttons if b['state'] != tk.DISABLED], default=None)

            # Verifica se o jogador clicou em todos os botões corretamente
            if self.current_number is None:  # Todos os botões foram desativados
                self.stop_timer()

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def stop_timer(self):
        self.timer_running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

    def update_timer(self):
        if self.timer_running:
            self.time_elapsed += 1
            self.timer_label.config(text=str(self.time_elapsed))
            self.timer_id = self.root.after(1000, self.update_timer)  # Atualiza o cronômetro a cada 1 segundo


# Configura a janela principal
root = tk.Tk()
game = ClickerGame(root)
root.mainloop()
