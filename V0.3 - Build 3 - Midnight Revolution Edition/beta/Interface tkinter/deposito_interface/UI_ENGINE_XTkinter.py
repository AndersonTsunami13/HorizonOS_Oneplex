# -*- coding: utf-8 -*-
# UI_ENGINE_XTkinter.py

import tkinter as tk
import sys
import io

# =======================
# UTF-8
# =======================

if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer,
        encoding="utf-8"
    )

# =======================
# Janela
# =======================

root = tk.Tk()
root.title("HorizonOS Professional XWin One")
root.geometry("900x500")
root.configure(bg="black")

terminal = tk.Text(
    root,
    bg="black",
    fg="cyan",
    insertbackground="white",
    font=("Courier New", 11),
    relief="flat",
    borderwidth=0
)

terminal.pack(fill="both", expand=True)

# =======================
# Cores
# =======================

CORES = {
    "BLACK": "#000000",
    "RED": "#ff4444",
    "GREEN": "#00ff00",
    "YELLOW": "#ffff00",
    "BLUE": "#4da6ff",
    "MAGENTA": "#ff00ff",
    "CYAN": "#00ffff",
    "WHITE": "#ffffff"
}

for nome, cor in CORES.items():
    terminal.tag_config(nome, foreground=cor)

terminal.tag_config(
    "DESTAQUE",
    font=("Courier New", 11, "bold")
)

# =======================
# Tema
# =======================

TEMA_ATUAL = {
    "cor": "CYAN",
    "velocidade": 30,   # milissegundos
    "performance": False
}

# =======================
# Fila de escrita
# =======================

fila = []
escrevendo = False

# =======================
# Utilidades
# =======================

def limpar():
    terminal.delete("1.0", "end")


def titulo_console(nome):
    root.title(nome)

# =======================
# Motor de escrita
# =======================

def escrever(
    texto,
    cor=None,
    velocidade=None,
    performance=None,
    pular_linha=True
):

    global escrevendo

    cor = cor or TEMA_ATUAL["cor"]

    if velocidade is None:
        velocidade = TEMA_ATUAL["velocidade"]
    else:
        velocidade = int(velocidade * 1000)

    if performance is None:
        performance = TEMA_ATUAL["performance"]

    if performance:
        velocidade = 0

    fila.append({
        "texto": texto,
        "cor": cor,
        "velocidade": velocidade,
        "indice": 0,
        "pular_linha": pular_linha
    })

    if not escrevendo:
        processar_fila()


def processar_fila():

    global escrevendo

    if not fila:
        escrevendo = False
        return

    escrevendo = True

    item = fila[0]

    if item["indice"] < len(item["texto"]):

        terminal.insert(
            "end",
            item["texto"][item["indice"]],
            item["cor"]
        )

        terminal.see("end")

        item["indice"] += 1

        root.after(
            item["velocidade"],
            processar_fila
        )

    else:

        if item["pular_linha"]:
            terminal.insert("end", "\n")

        terminal.see("end")

        fila.pop(0)

        root.after(
            1,
            processar_fila
        )

# =======================
# Teste
# =======================

escrever(
    "====================================",
    "CYAN"
)

escrever(
    " HorizonOS Professional XWin One ",
    "GREEN"
)

escrever(
    "====================================",
    "CYAN"
)

escrever(
    "Inicializando sistema...",
    "WHITE",
    velocidade=0.02
)

escrever(
    "[ OK ]",
    "GREEN"
)

escrever(
    "Erro crítico detectado!",
    "RED"
)

root.mainloop()