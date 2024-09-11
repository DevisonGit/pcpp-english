import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Variável para o visor
        self.display_var = tk.StringVar()
        self.display_var.set("0")

        # Cria o visor da calculadora
        self.display = tk.Entry(root, textvariable=self.display_var, font=("Courier", 20), width=12, justify="right",
                                bd=10)
        self.display.grid(row=0, column=0, columnspan=4)

        # Cria os botões
        buttons = [
            ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
        ]

        for (text, row, col, *span) in buttons:
            button = tk.Button(root, text=text, font=("Courier", 18), width=5, height=2,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=span[0] if span else 1)

        self.reset()

    def reset(self):
        """Reseta a calculadora para o estado inicial."""
        self.current_value = "0"
        self.operator = ""
        self.first_operand = None
        self.result_shown = False
        self.update_display()

    def on_button_click(self, char):
        """Lida com cliques nos botões da calculadora."""
        if char == "C":
            self.reset()
        elif char == "±":
            self.change_sign()
        elif char == "=":
            self.calculate()
        elif char in "0123456789":
            self.append_digit(char)
        elif char == ".":
            self.add_decimal_point()
        elif char in "+-*/":
            self.set_operator(char)

    def update_display(self):
        """Atualiza o visor, mantendo no máximo 10 caracteres."""
        if len(self.current_value) > 10:
            self.display_var.set("ERROR")
        else:
            self.display_var.set(self.current_value)

    def append_digit(self, digit):
        """Adiciona um dígito ao número atual."""
        if self.result_shown:
            self.current_value = digit
            self.result_shown = False
        elif self.current_value == "0":
            self.current_value = digit
        else:
            self.current_value += digit
        self.update_display()

    def add_decimal_point(self):
        """Adiciona o ponto decimal."""
        if "." not in self.current_value:
            self.current_value += "."
        self.update_display()

    def set_operator(self, operator):
        """Define o operador e salva o primeiro operando."""
        if self.first_operand is None:
            self.first_operand = float(self.current_value)
        else:
            self.calculate()
        self.operator = operator
        self.result_shown = False
        self.current_value = "0"

    def change_sign(self):
        """Altera o sinal do número atual."""
        if self.current_value.startswith("-"):
            self.current_value = self.current_value[1:]
        else:
            self.current_value = "-" + self.current_value
        self.update_display()

    def calculate(self):
        """Realiza o cálculo baseado no operador atual."""
        if self.operator and self.first_operand is not None:
            second_operand = float(self.current_value)
            try:
                if self.operator == "+":
                    result = self.first_operand + second_operand
                elif self.operator == "-":
                    result = self.first_operand - second_operand
                elif self.operator == "*":
                    result = self.first_operand * second_operand
                elif self.operator == "/":
                    if second_operand == 0:
                        raise ZeroDivisionError
                    result = self.first_operand / second_operand

                self.current_value = str(int(result)) if result.is_integer() else str(result)
                self.first_operand = None
                self.result_shown = True
                self.update_display()

            except ZeroDivisionError:
                self.display_var.set("ERROR")
                self.reset()


# Cria a janela principal
root = tk.Tk()
calc = Calculator(root)
root.mainloop()
