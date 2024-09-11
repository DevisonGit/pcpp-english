import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.board = [""] * 9  # Estado do tabuleiro (lista de 9 posições)
        self.buttons = []
        self.game_over = False

        # Cria os botões do tabuleiro
        for i in range(9):
            button = tk.Button(root, text="", width=10, height=3, font=("Helvetica", 24),
                               command=lambda i=i: self.user_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        # Primeiro movimento do computador
        self.computer_move()

    def user_move(self, index):
        """Executa o movimento do jogador."""
        if not self.game_over and self.board[index] == "":
            self.board[index] = "O"
            self.buttons[index].config(text="O", fg="green")

            if self.check_winner("O"):
                self.end_game("User wins!")
            elif "" not in self.board:
                self.end_game("It's a tie!")
            else:
                self.computer_move()

    def computer_move(self):
        """Executa o movimento do computador."""
        available_moves = [i for i in range(9) if self.board[i] == ""]
        if available_moves:
            if self.board[4] == "":  # Primeiro movimento do computador no centro
                move = 4
            else:
                move = random.choice(available_moves)
            self.board[move] = "X"
            self.buttons[move].config(text="X", fg="red")

            if self.check_winner("X"):
                self.end_game("Computer wins!")
            elif "" not in self.board:
                self.end_game("It's a tie!")

    def check_winner(self, player):
        """Verifica se o jogador atual venceu."""
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
                          (0, 4, 8), (2, 4, 6)]             # Diagonais

        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] == player:
                return True
        return False

    def end_game(self, message):
        """Finaliza o jogo e exibe a mensagem do vencedor."""
        self.game_over = True
        messagebox.showinfo("Game Over", message)
        self.reset_game()

    def reset_game(self):
        """Reinicia o jogo."""
        self.board = [""] * 9
        self.game_over = False
        for button in self.buttons:
            button.config(text="")

        # O computador começa o próximo jogo
        self.computer_move()

# Cria a janela principal
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
