# MDL_fundo_terminal.py

import os
import shutil
from colorama import init, Fore, Back, Style

init()

def mdl_fundo_terminal(fundo, cor):
    os.system("cls" if os.name == "nt" else "clear")

    FUNDOS = {
        "BLACK": Back.BLACK,
        "RED": Back.RED,
        "GREEN": Back.GREEN,
        "YELLOW": Back.YELLOW,
        "BLUE": Back.BLUE,
        "MAGENTA": Back.MAGENTA,
        "CYAN": Back.CYAN,
        "WHITE": Back.WHITE
    }

    TEXTOS = {
        "BLACK": Fore.BLACK,
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
        "YELLOW": Fore.YELLOW,
        "BLUE": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE
    }

    terminal = shutil.get_terminal_size()

    width = terminal.columns
    height = terminal.lines 

    print(FUNDOS.get(fundo.upper(), ""), end="")
    print(TEXTOS.get(cor.upper(), ""), end="")

    for _ in range(height):
        print(" " * width)

    print("\033[H", end="")

# Anderson_Tsunami.M3_E36