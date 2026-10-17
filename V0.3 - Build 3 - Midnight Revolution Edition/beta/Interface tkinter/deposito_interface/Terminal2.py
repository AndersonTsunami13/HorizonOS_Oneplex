import time
import tkinter as tk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "dados"))
from Information.configapps import *

def abrir_terminal():
    term = tk.Toplevel()
    term.title("Terminal")
    term.geometry("600x400")
    term.configure(bg=f"{TEMA_FUNDO}")

    entrada = tk.Entry(term, bg=f"{TEMA_TEXTO_2}", fg="lime", insertbackground="lime", font=("Consolas", 12))
    entrada.pack(fill="x")

    output = tk.Text(term, bg=f"{TEMA_TEXTO_1}", fg="lime", font=("Consolas", 12))
    output.pack(expand=True, fill="both")

    def executar_cmd(event):
        comando = entrada.get()
        entrada.delete(0, tk.END)

        if comando == "ver":
            output.insert("end", f"Horizon Galaxy Edition One {VERSAO_HORIZON_2}\nBaseado na base {VERSAO_BASE}\n")
        elif comando == "dir":
            output.insert("end", "C: Arquivos de programas\nD: Acesso negado\nOutras unidades não disponíveis!\n")
        elif comando == "help":
            output.insert("end", "Comandos disponíveis:\n- ver\n- dir\n- help\n- cls\n- hora\n- sobre\n- piada\n- apps\n- games\n")
        elif comando == "cls":
            output.delete("1.0", tk.END)
        elif comando == "hora":
            output.insert("end", f"Hora atual: {time.strftime('%H:%M:%S')}\n")
        elif comando == "apps":
            output.insert("end", "Lista dos apps atuais instalados no sistema:\n     Lixeira\n     MeuPc\n     Navegador\n     Terminal\n(apps do sistema raiz nao podem ser mostrados)\n")
        elif comando == "games":
            output.insert("end", "Nenhum jogos instalado no sistema\n")
        elif comando == "sobre":
            output.insert("end", "Esse é o terminal do Horizon Galaxy Edition One.\nDesenvolvido para um sistema estilo retrô!\n")
        elif comando == "piada":
            output.insert("end", "indisponivel!\n")
        else:
            output.insert("end", f"{comando}: comando não reconhecido.\nTente novamente.\n")

    entrada.bind("<Return>", executar_cmd)
