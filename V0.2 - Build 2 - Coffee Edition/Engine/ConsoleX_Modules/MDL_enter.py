# MDL_enter.py

# Importações
from colorama import Fore, Style

# Esse modulo serve para mostrar mensagens para continuar como "Pressione enter para continuar...".

def mdl_enter(name): # aperta enter para continuar
    input(Fore.CYAN + Style.BRIGHT + name)

if __name__ == "__main__":
    mdl_enter("Pressione enter para continuar...")

# Anderson_Tsunami.M3_E36