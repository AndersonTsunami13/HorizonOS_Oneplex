# MDL_limpar.py

# Importação
import os

# O devmode.py é chamado para saber se o sistema pode ou nao limpar a tela do terminal.
# Isso é feito especialmente para debug do sistema.
try:
    from Information.devmode import limpar_on
except ImportError:
    limpar_on = True # Se não conseguir importar, assume que pode limpar a tela.

def mdl_limpar(): # para limpar a tela
    if limpar_on:
        os.system("cls" if os.name == "nt" else "clear") 
    else:
        print("\n") # Pula uma linha no lugar de limpar a tela

if __name__ == "__main__":
    mdl_limpar() # Teste da função

# Anderson_Tsunami.M3_E36