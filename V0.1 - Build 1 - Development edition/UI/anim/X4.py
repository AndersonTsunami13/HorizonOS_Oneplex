import os
import time
from datetime import datetime

DIGITOS = {
    "0": [
        " ███ ",
        "█   █",
        "█   █",
        "█   █",
        " ███ "
    ],
    "1": [
        "  █  ",
        " ██  ",
        "  █  ",
        "  █  ",
        "█████"
    ],
    "2": [
        "████ ",
        "    █",
        " ███ ",
        "█    ",
        "█████"
    ],
    "3": [
        "████ ",
        "    █",
        " ███ ",
        "    █",
        "████ "
    ],
    "4": [
        "█  █ ",
        "█  █ ",
        "█████",
        "   █ ",
        "   █ "
    ],
    "5": [
        "█████",
        "█    ",
        "████ ",
        "    █",
        "████ "
    ],
    "6": [
        " ███ ",
        "█    ",
        "████ ",
        "█   █",
        " ███ "
    ],
    "7": [
        "█████",
        "    █",
        "   █ ",
        "  █  ",
        " █   "
    ],
    "8": [
        " ███ ",
        "█   █",
        " ███ ",
        "█   █",
        " ███ "
    ],
    "9": [
        " ███ ",
        "█   █",
        " ████",
        "    █",
        " ███ "
    ],
    ":": [
        "     ",
        "  █  ",
        "     ",
        "  █  ",
        "     "
    ]
}

VERDE = "\033[92m"
RESET = "\033[0m"

while True:
    largura = os.get_terminal_size().columns
    altura = os.get_terminal_size().lines

    hora = datetime.now().strftime("%H:%M:%S")

    linhas = [""] * 5

    for c in hora:
        desenho = DIGITOS[c]
        for i in range(5):
            linhas[i] += desenho[i] + "  "

    os.system("cls" if os.name == "nt" else "clear")

    print("\n" * ((altura - 5) // 2))

    for linha in linhas:
        print((VERDE + linha + RESET).center(largura))

    time.sleep(0.1)