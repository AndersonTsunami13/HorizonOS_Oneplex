# MDL_limpar.py

# Importação
import os

# O devmode.py é chamado para saber se o sistema pode ou nao limpar a tela do terminal.
# Isso é feito especialmente para debug do sistema.
from Information.devmode import limpar_on

def code_aa(): # para limpar a tela
    if limpar_on:
        os.system("cls" if os.name == "nt" else "clear") 
    else:
        print("\n") # Pula uma linha no lugar de limpar a tela

# Anderson_Tsunami.11Xx