import tkinter as tk


class TrafficLight:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light")

        # Canvas para as luzes do semáforo
        self.canvas = tk.Canvas(root, width=100, height=260, bg='black')
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Desenha os círculos do semáforo
        self.red_light = self.canvas.create_oval(20, 20, 80, 80, fill='gray')
        self.yellow_light = self.canvas.create_oval(20, 100, 80, 160, fill='gray')
        self.green_light = self.canvas.create_oval(20, 180, 80, 240, fill='gray')

        # Fases do semáforo (Vermelho, Amarelo, Verde)
        self.phases = [
            (True, False, False),  # Apenas vermelho
            (True, True, False),  # Vermelho e amarelo
            (False, False, True),  # Apenas verde
            (False, True, False)  # Apenas amarelo
        ]
        self.current_phase = 0  # Fase inicial

        # Botão "Next" para avançar para a próxima fase
        self.next_button = tk.Button(root, text="Next", command=self.change_phase)
        self.next_button.grid(row=1, column=0)

        # Botão "Quit" para sair do programa
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.grid(row=1, column=1)

        # Atualiza as luzes para a fase inicial
        self.update_lights()

    def update_lights(self):
        """Atualiza as luzes de acordo com a fase atual."""
        red_on, yellow_on, green_on = self.phases[self.current_phase]

        self.canvas.itemconfig(self.red_light, fill='red' if red_on else 'gray')
        self.canvas.itemconfig(self.yellow_light, fill='yellow' if yellow_on else 'gray')
        self.canvas.itemconfig(self.green_light, fill='green' if green_on else 'gray')

    def change_phase(self):
        """Muda para a próxima fase e atualiza as luzes."""
        self.current_phase = (self.current_phase + 1) % len(self.phases)
        self.update_lights()


# Cria a janela principal
root = tk.Tk()
traffic_light = TrafficLight(root)
root.mainloop()
