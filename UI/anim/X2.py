import os
import time
import random
from datetime import datetime

# ============================
# Configuração
# ============================

LARGURA = os.get_terminal_size().columns
ALTURA = os.get_terminal_size().lines

colunas = [random.randint(0, ALTURA) for _ in range(LARGURA)]

VERDE = "\033[92m"
BRANCO = "\033[97m"
AZUL = "\033[96m"
AMARELO = "\033[93m"
RESET = "\033[0m"

dias = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo"
]

meses = [
    "Janeiro", "Fevereiro", "Março",
    "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro",
    "Outubro", "Novembro", "Dezembro"
]

while True:

    agora = datetime.now()

    hora = agora.strftime("%H:%M:%S")
    dia = dias[agora.weekday()]
    data = f"{agora.day} de {meses[agora.month-1]} de {agora.year}"

    tela = []

    # ===== Chuva =====
    for y in range(ALTURA):

        linha = []

        for x in range(LARGURA):

            if colunas[x] == y:
                linha.append(VERDE + random.choice("01|") + RESET)
            else:
                linha.append(" ")

        tela.append(linha)

    # Atualiza chuva
    for i in range(LARGURA):
        if random.random() < 0.02:
            colunas[i] = 0
        else:
            colunas[i] += 1
            if colunas[i] >= ALTURA:
                colunas[i] = 0

    # ===== Caixa Central =====

    caixa = [
        "┌────────────────────────────────────┐",
        "│                                    │",
        f"│{VERDE}{hora.center(36)}{RESET}│",
        "│                                    │",
        f"│{BRANCO}{dia.center(36)}{RESET}│",
        f"│{BRANCO}{data.center(36)}{RESET}│",
        "│                                    │",
        f"│{AZUL}{'HorizonOS Build 3'.center(36)}{RESET}│",
        "│                                    │",
        f"│{AMARELO}{'Pressione ENTER'.center(36)}{RESET}│",
        f"│{AMARELO}{'para desbloquear'.center(36)}{RESET}│",
        "└────────────────────────────────────┘"
    ]

    inicio_y = ALTURA // 2 - len(caixa) // 2
    inicio_x = LARGURA // 2 - 19

    for i, texto in enumerate(caixa):
        y = inicio_y + i

        if 0 <= y < ALTURA:
            for j, ch in enumerate(texto):
                x = inicio_x + j
                if 0 <= x < LARGURA:
                    tela[y][x] = ch

    os.system("cls" if os.name == "nt" else "clear")

    for linha in tela:
        print("".join(linha))

    time.sleep(0.05)