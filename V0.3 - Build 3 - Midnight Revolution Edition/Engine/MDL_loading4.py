# MDL_loading4.py

# Importações 
import sys, time
from colorama import Fore, Style

# Dicionario de cores do colorama
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

def mdl_loading4(duracao=3, cor1="BLUE"):
    cor = TEXTOS[cor1]

    sys.stdout.write("\033[?25l") # esconder o cursor
    sys.stdout.flush()

    for _ in range(duracao):

        for pontos in [
            "     ",
            ".    ",                # atualização que mudou de 3 para 5 pontos
            "..   ",
            "...  ",
            ".... ",
            ".....",
            " ....",
            "  ...",
            "   ..",
            "    ."
        ]:

            sys.stdout.write(f"\r{Style.BRIGHT}{cor} {pontos}{Style.RESET_ALL}")
            sys.stdout.flush()
            
            time.sleep(0.1)

    sys.stdout.write("\033[?25h") # mostrar o cursor
    sys.stdout.flush()
    
    print() # Evita um bug especifico....

if __name__ == "__main__":
    mdl_loading4(3, "GREEN")

# Anderson_Tsunami.M3_E36