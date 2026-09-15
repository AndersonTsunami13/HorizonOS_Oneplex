import os
import time
import sys
import random

# Tamanho do terminal
largura = os.get_terminal_size().columns
altura = os.get_terminal_size().lines

# Cada coluna tem uma "posição de queda"
colunas = [random.randint(0, altura) for _ in range(largura)]

while True:
    tela = []

    for y in range(altura):
        linha = ""
        for x in range(largura):
            if colunas[x] == y:
                linha += "|"
            else:
                linha += " "
        tela.append(linha)

    # Move a "chuva"
    for i in range(largura):
        if random.random() < 0.02:  # chance de resetar no topo
            colunas[i] = 0
        else:
            colunas[i] += 1
            if colunas[i] >= altura:
                colunas[i] = 0

    # Limpa tela
    os.system("cls" if os.name == "nt" else "clear")

    print("\n".join(tela))

    time.sleep(0.05)