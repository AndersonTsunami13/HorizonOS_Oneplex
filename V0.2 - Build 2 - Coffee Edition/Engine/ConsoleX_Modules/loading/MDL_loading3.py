# MDL_loading3.py

import sys, time, platform, os

from colorama import Fore, Style

TEXTOS = {
    "BLACK": Fore.BLACK, # Preto
    "RED": Fore.RED, # Vermelho 
    "GREEN": Fore.GREEN, # Verde
    "YELLOW": Fore.YELLOW, # Amarelo
    "BLUE": Fore.BLUE, # Azul
    "MAGENTA": Fore.MAGENTA, # Rosa
    "CYAN": Fore.CYAN, # Azul claro
    "WHITE": Fore.WHITE # Branco
} 

sistema = platform.system()

def console_titulo(nome):
    if sistema == "Windows": 
        os.system(f"title {nome}")
    else:
        print(f"\033]0;{nome}\a", end="")

def mdl_loading3(duracao=3, texto="Certo! Aguarde...", cor1="BLUE"):
    
    cor = TEXTOS[cor1]

    for _ in range(duracao):

        for pontos in [
            "[     ]",
            "[.    ]",
            "[..   ]",
            "[...  ]",
            "[ ... ]",
            "[  ...]",
            "[   ..]",
            "[    .]"
        ]:

            sys.stdout.write(f"\r{Style.BRIGHT}{cor}{pontos} {texto}{Style.RESET_ALL}")
            console_titulo(pontos)
            sys.stdout.flush()

            time.sleep(0.2)

    print()
    
if __name__ == "__main__":
    mdl_loading3(3, "carregando", "GREEN")

# Anderson_Tsunami.M3_E36