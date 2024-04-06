import tkinter as tk
from tkinter import messagebox
import pyperclip

# Função para converter minutos e segundos em segundos totais
def converter_tempo():
    try:
        # Obter valores dos campos de entrada
        minutes = int(entry_minutes.get())
        seconds = int(entry_seconds.get())
        # Calcular total de segundos
        total_seconds = (minutes * 60) + seconds
        # Copiar total de segundos para a área de transferência
        pyperclip.copy(total_seconds)
        # Exibir o resultado
        label_result.config(text=f"{minutes} minutos e {seconds} segundos são {total_seconds} segundos.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números inteiros.")

# Criar a janela principal
root = tk.Tk()
root.title("Conversor MinSeg")
root.iconbitmap("C:\workspace\ConvMinSeg\convMinSeg.ico")

# Configurar o tamanho da janela
root.geometry('300x200')

# Criar e posicionar os widgets
tk.Label(root, text="Informe o número de minutos:").pack()
entry_minutes = tk.Entry(root)
entry_minutes.pack()

tk.Label(root, text="Informe o número de segundos:").pack()
entry_seconds = tk.Entry(root)
entry_seconds.pack()

button_convert = tk.Button(root, text="Converter", command=converter_tempo)
button_convert.pack()

label_result = tk.Label(root, text="")
label_result.pack()

button_close = tk.Button(root, text="Fechar", command=root.destroy)
button_close.pack()

# Iniciar o loop principal da interface gráfica
root.mainloop()
