import os
import time
from datetime import datetime

VERDE = "\033[92m"
BRANCO = "\033[97m"
AZUL = "\033[96m"
AMARELO = "\033[93m"
RESET = "\033[0m"

dias = [
    "Segunda-feira", "Terça-feira", "Quarta-feira",
    "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
]

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

while True:
    largura = os.get_terminal_size().columns
    altura = os.get_terminal_size().lines

    agora = datetime.now()

    hora = agora.strftime("%H:%M:%S")
    dia = dias[agora.weekday()]
    data = f"{agora.day} de {meses[agora.month-1]} de {agora.year}"

    os.system("cls" if os.name == "nt" else "clear")

    caixa = [
        "┌────────────────────────────────────┐",
        "│                                    │",
        f"│{VERDE}{hora.center(36)}{RESET}│",
        "│                                    │",
        f"│{BRANCO}{dia.center(36)}{RESET}│",
        f"│{BRANCO}{data.center(36)}{RESET}│",
        "│                                    │",
        f"│{AZUL}{'HorizonOS'.center(36)}{RESET}│",
        "│                                    │",
        f"│{AMARELO}{'Pressione ENTER'.center(36)}{RESET}│",
        "└────────────────────────────────────┘"
    ]

    print("\n" * max(0, (altura - len(caixa)) // 2))

    for linha in caixa:
        print(linha.center(largura))

    time.sleep(0.2)