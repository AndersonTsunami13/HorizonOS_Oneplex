import tkinter as tk

from Engine.UI_TitleBar import *

def abrir_test_statusbar(janela):

    janela_teste = tk.Toplevel(janela)
    janela_teste.title("Teste da StatusBar")
    janela_teste.geometry("300x120")
    janela_teste.resizable(False, False)

    tk.Label(
        janela_teste,
        text="Mensagem:"
    ).pack(pady=(10, 0))

    entrada = tk.Entry(janela_teste, width=35)
    entrada.pack(pady=5)

    def enviar():
        mensagem = entrada.get().strip()

        if mensagem:
            set_status(mensagem)
            janela_teste.after(
                3000,
                lambda: set_status("Sistema reparado!")
            )

    tk.Button(
        janela_teste,
        text="Enviar notificação",
        command=enviar
    ).pack(pady=10)