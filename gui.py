import tkinter as tk

from PIL import Image, ImageTk

# Variáveis de tela:
window = tk.Tk()
window.title("Bugalha_by_gio")
window.geometry("600x800")

image = Image.open('./assets/1.jpg')
python_image = ImageTk.PhotoImage(image)

#  8 linhas
window.rowconfigure(0, weight=1) # Somatório da col do oponente
window.rowconfigure((1,2,3), weight=1) # grid do oponente
window.rowconfigure(4, weight=1)
window.rowconfigure((5,6,7), weight=1) # grid do jogador
window.rowconfigure(0, weight=1) # Somatório da col do jogador
window.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

# labels

label1 = tk.Label(window, text = "-", background="gray10", foreground="white")
label2 = tk.Label(window, text = "-", background="gray10", foreground="white")
label3 = tk.Label(window, text = "-", background="gray10", foreground="white")
label4 = tk.Label(window, text = "-", background="gray10", foreground="white")
label5 = tk.Label(window, text = "-", background="gray10", foreground="white")
label6 = tk.Label(window, text = "-", background="gray10", foreground="white")
label7 = tk.Label(window, text = "-", background="gray10", foreground="white")
label8 = tk.Label(window, text = "-", background="gray10", foreground="white")
label9 = tk.Label(window, text = "-", background="gray10", foreground="white")
# Sub-contas das colunas do oponente
label10 = tk.Label(window, text = "##", background="gray10", foreground="chocolate1")
label11 = tk.Label(window, text = "##", background="gray10", foreground="chocolate1")
label12 = tk.Label(window, text = "##", background="gray10", foreground="chocolate1")
# Divisão de tela
label13 = tk.Label(window, text = "VS", background="gray10", foreground="white")
# Sub-contas das colunas do jogador
label14 = tk.Label(window, text = "##", background="gray10", foreground="light sea green")
label15 = tk.Label(window, text = "##", background="gray10", foreground="light sea green")
label16 = tk.Label(window, text = "##", background="gray10", foreground="light sea green")
# Grid do jogador
label17 = tk.Label(window, text = "-", background="gray10", foreground="white")
label18 = tk.Label(window, text = "-", background="gray10", foreground="white")
label19 = tk.Label(window, text = "-", background="gray10", foreground="white")
label20 = tk.Label(window, text = "-", background="gray10", foreground="white")
label21 = tk.Label(window, text = "-", background="gray10", foreground="gray55")
label22 = tk.Label(window, text = "-", background="gray10", foreground="white")
label23 = tk.Label(window, text = "-", background="gray10", foreground="white")
label24 = tk.Label(window, text = "-", background="gray10", foreground="white")
label25 = tk.Label(window, text = "-", background="gray10", foreground="white")

# buttons
button1 = tk.Button(window, text = "Col 1", background="gray10", foreground="light sea green")
button2 = tk.Button(window, text = "Col 2", background="gray10", foreground="light sea green")
button3 = tk.Button(window, text = "Col 3", background="gray10", foreground="light sea green")

#image
image = tk.Label(window, image=python_image)

# Grid
# Grid do oponente,
label1.grid(row=0, column=3, sticky="nsew")
label2.grid(row=0, column=4, sticky="nsew")
label3.grid(row=0, column=5, sticky="nsew")
label4.grid(row=1, column=3, sticky="nsew")
label5.grid(row=1, column=4, sticky="nsew")
label6.grid(row=1, column=5, sticky="nsew")
label7.grid(row=2, column=3, sticky="nsew")
label8.grid(row=2, column=4, sticky="nsew")
label9.grid(row=2, column=5, sticky="nsew")
# Rótulo de somatório das colunas do oponente
label10.grid(row=3, column=3, sticky="nsew")
label11.grid(row=3, column=4, sticky="nsew")
label12.grid(row=3, column=5, sticky="nsew")
# Divisao do board
label13.grid(row=4, column=0, columnspan=10, sticky="nsew") # VS
# Rótulo de somatório do jogador
label14.grid(row=5, column=3, sticky="nsew")
label15.grid(row=5, column=4, sticky="nsew")
label16.grid(row=5, column=5, sticky="nsew")
# Grid dos dados do oponente
label17.grid(row=6, column=3, sticky="nsew")
label18.grid(row=6, column=4, sticky="nsew")
label19.grid(row=6, column=5, sticky="nsew")
label20.grid(row=7, column=3, sticky="nsew")
label21.grid(row=7, column=4, sticky="nsew")
label22.grid(row=7, column=5, sticky="nsew")
label23.grid(row=8, column=3, sticky="nsew")
label24.grid(row=8, column=4, sticky="nsew")
label25.grid(row=8, column=5, sticky="nsew")
#botoes de selecao de coluna
button1.grid(row=9, column=3, sticky="nsew")
button2.grid(row=9, column=4, sticky="nsew")
button3.grid(row=9, column=5, sticky="nsew")
#imagem
image.grid(row=8, columns=7, sticky="nsew")

window.mainloop()
