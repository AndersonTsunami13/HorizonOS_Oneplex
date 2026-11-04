# navegador.py
import tkinter as tk
from tkinter import messagebox

def abrir_navegador():
    janela = tk.Toplevel()
    janela.title("Navegador Horizon")
    janela.geometry("600x300")
    janela.configure(bg="black")

    label = tk.Label(janela, text="Digite o site:", bg="black", fg="white", font=("Arial", 12))
    label.pack(pady=5)

    entrada = tk.Entry(janela, width=50)
    entrada.pack(pady=5)

    def abrir_site():
        url = entrada.get()
        if not url.startswith("http"):
            url = "http://" + url

        # Simulação de vírus e erro
        messagebox.showwarning("Aviso", "Esse site tem vírus brutais!!!!!!!!!!!!")
        messagebox.showerror("Erro", f"O site {url} não pôde ser aberto.\n\nErro: Simulação de falha no carregamento.")

    botao = tk.Button(janela, text="Ir", command=abrir_site,
                      bg="black", fg="white", font=("Arial", 12))
    botao.pack(pady=5)
