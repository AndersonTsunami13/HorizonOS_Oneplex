import sys, time

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
 
def code_aq(
    duracao=3,
    texto="Certo! Aguarde",
    cor1="BLUE"
):

    cor = TEXTOS[cor1]

    for _ in range(duracao):

        for pontos in [
            "     ",
            ".    ",
            "..   ",
            "...  ",
            ".... ",
            "....."
        ]:

            sys.stdout.write(
                f"\r{Style.BRIGHT}{cor}{texto}{pontos}{Style.RESET_ALL}"
            )

            sys.stdout.flush()

            time.sleep(0.5)

    print()

if __name__ == "__main__":
    loading1()