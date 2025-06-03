import tkinter as tk
from tkinter import messagebox
# import serial  # Descomente se for usar comunicação serial

# Porta e baudrate do Arduino
# arduino = serial.Serial('COM3', 9600)

class ArduinoSimulator:
    def __init__(self, master):
        self.master = master
        master.title("Interface Arduino - LEDs e Display")

        # Estado do botão
        self.botao_estado = False

        # Botão para simular pinoChave
        self.botao = tk.Button(master, text="Pressionar Botão", command=self.toggle_botao)
        self.botao.pack(pady=10)

        # Indicadores LEDs
        self.led_vermelho = tk.Label(master, text="LED Vermelho", bg="gray", width=20)
        self.led_vermelho.pack()

        self.led_amarelo = tk.Label(master, text="LED Amarelo", bg="gray", width=20)
        self.led_amarelo.pack()

        self.led_verde = tk.Label(master, text="LED Verde", bg="gray", width=20)
        self.led_verde.pack()

        # Indicador do Buzzer
        self.buzzer = tk.Label(master, text="Buzzer", bg="gray", width=20)
        self.buzzer.pack(pady=10)

        # Display 7 segmentos
        self.display = tk.Label(master, text="00", font=("Courier", 44))
        self.display.pack(pady=20)

    def toggle_botao(self):
        self.botao_estado = not self.botao_estado
        self.update_interface()
        # Se for usar serial:
        # comando = '1' if self.botao_estado else '0'
        # arduino.write(comando.encode())

    def update_interface(self):
        if self.botao_estado:
            # Botão pressionado
            self.led_verde.config(bg="gray")
            self.led_vermelho.config(bg="red")
            self.led_amarelo.config(bg="gray")
            self.buzzer.config(bg="gray")
            self.display.config(text="99")
        else:
            # Botão solto
            self.led_verde.config(bg="green")
            self.led_vermelho.config(bg="gray")
            self.led_amarelo.config(bg="gray")
            self.buzzer.config(bg="yellow")
            self.display.config(text="00")

# Execução da interface
root = tk.Tk()
app = ArduinoSimulator(root)
root.mainloop()
