import tkinter as tk
from tkinter import messagebox


# Função para avaliar a operação
def evaluate():
    try:
        # Tentar converter as entradas para float
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        # Verificar qual operação foi selecionada
        if operation.get() == 1:
            result = num1 + num2
        elif operation.get() == 2:
            result = num1 - num2
        elif operation.get() == 3:
            result = num1 * num2
        elif operation.get() == 4:
            # Proteção contra divisão por zero
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2

        # Exibir o resultado
        messagebox.showinfo("Result", f"Result: {result}")
    except ValueError:
        # Se houver erro de valor, mostrar mensagem de erro e focar no campo problemático
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        if not entry1.get().replace('.', '', 1).isdigit():
            entry1.focus_set()
        elif not entry2.get().replace('.', '', 1).isdigit():
            entry2.focus_set()
    except ZeroDivisionError as e:
        # Erro de divisão por zero
        messagebox.showerror("Math Error", str(e))
        entry2.focus_set()


# Configuração da janela principal
root = tk.Tk()
root.title("Simple Calculator")

# Entradas
entry1 = tk.Entry(root)
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = tk.Entry(root)
entry2.grid(row=0, column=2, padx=5, pady=5)

# Variável para armazenar a operação selecionada
operation = tk.IntVar(value=1)

# Botões de rádio para selecionar a operação
tk.Radiobutton(root, text="+", variable=operation, value=1).grid(row=1, column=0)
tk.Radiobutton(root, text="-", variable=operation, value=2).grid(row=1, column=1)
tk.Radiobutton(root, text="*", variable=operation, value=3).grid(row=1, column=2)
tk.Radiobutton(root, text="/", variable=operation, value=4).grid(row=1, column=3)

# Botão para avaliar
evaluate_button = tk.Button(root, text="Evaluate", command=evaluate)
evaluate_button.grid(row=2, column=0, columnspan=4, pady=10)

# Iniciar o loop da janela
root.mainloop()
