import tkinter as tk

# Função que será chamada quando o botão for clicado
def on_button_click():
    label.config(text="Você clicou no botão!")

# Criação da janela principal
root = tk.Tk()
root.title("Minha Aplicação Tkinter")

# Configuração do tamanho da janela
root.geometry("300x200")

# Criação de um rótulo (label) na janela
label = tk.Label(root, text="Clique no botão abaixo")
label.pack(pady=20)

# Criação de um botão na janela
button = tk.Button(root, text="Clique aqui", command=on_button_click)
button.pack(pady=10)

# Inicia o loop principal da aplicação
root.mainloop()