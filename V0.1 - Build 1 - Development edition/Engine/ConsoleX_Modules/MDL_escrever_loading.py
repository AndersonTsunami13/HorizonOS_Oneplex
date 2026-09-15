# MDL_escrever_loading.py

# Importações 
import sys, time
from colorama import Fore, Style

# Importação responsavel por ocultar o cursor durante a animação de carregamento.
from Engine.ConsoleX_Modules.MDL_cursor import code_ag as cursor

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
 
def code_ak(duracao=3, texto="Certo! Aguarde", cor1="BLUE"):

    cor = TEXTOS[cor1]

    cursor(False) # oculta o cursor do console

    for _ in range(duracao):

        for pontos in [
            "     ",
            ".    ",                # atualização que mudou de 3 para 5 pontos
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

    cursor(True) # Mostra o cursor novamente
    print() # Evita um bug especifico....