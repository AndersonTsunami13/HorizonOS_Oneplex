# MDL_anim_module.py

import os, time

from Engine.ConsoleX_Modules.MDL_cursor_posicionar import code_am as goto
from Engine.ConsoleX_Modules.MDL_limpar import code_aa as clear

# Animação de letreiro
def code_av(texto, inicio, fim, y, delay=0.03):
    passo = 1 if fim > inicio else -1
    for x in range(inicio, fim + passo, passo):
        clear()
        goto(x, y)
        print(texto)
        time.sleep(delay)

# Animação de criação de janela no terminal
def code_aw(x, y, largura, altura, delay=0.03):
    for w in range(2, largura + 1):
        clear()
        goto(x, y)
        print("┌" + "─" * (w - 2) + "┐")
        time.sleep(delay)
    for h in range(2, altura + 1):
        clear()
        goto(x, y)
        print("┌" + "─" * (largura - 2) + "┐")
        for i in range(h - 2):
            goto(x, y + i + 1)
            print("│" + " " * (largura - 2) + "│")
        goto(x, y + h - 1)
        print("└" + "─" * (largura - 2) + "┘")
        time.sleep(delay)

# texto piscando
def code_ax(texto, x, y, vezes, delay):
    for i in range(vezes):
        goto(x, y)
        print(texto, end="", flush=True)
        time.sleep(delay)
        
        # Só apaga se NÃO for a última repetição
        if i < vezes - 1:
            goto(x, y)
            print(" " * len(texto), end="", flush=True)
            time.sleep(delay)

# barra de progresso
def code_ay(total, delay):
    for i in range(total + 1):
        porcentagem = int((i / total) * 100)
        barra = "█" * i + "░" * (total - i)
        print(f"\r[{barra}] {porcentagem}%", end="", flush=True)
        time.sleep(delay)
    print()

# Anderson_Tsunami.11Xx
