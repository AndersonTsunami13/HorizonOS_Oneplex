# debug.py

import sys, time, os

# Importações
from Information.info import debug_version
from Information.dados import *
from Information.devmode import *

# Importações de funções de debug
from Debug_files.debug1 import debug1
from Debug_files.debug2 import debug2
from Debug_files.debug3 import debug3
from Debug_files.debug4 import debug4
from Debug_files.debug5 import debug5
from Debug_files.debug6 import debug6

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def escrever(text):
    print(text)

# 1. Crie uma lista simples relacionando o número digitado à função
OPCOES_MENU = [
    ("1", debug2),
    ("2", debug1),
    ("3", debug3),
    ("4", debug4),
    ("5", debug5),
    ("6", debug6)
]

def main():
    while True:
        limpar()
        escrever(f"Interface de debug\n> [{debug_version}] <\n")
        
        escrever("""
[1] Engine/UI_Engine_ConsoleX.py
[2] Information/info.py
[3] Security/securitymodule_createpassword.py
[4] Security/securitymodule_verification.py
[5] Kernel/verification.py
[6] UI/screen_vibe/Ghost_Clock.py
[s] Sair
""")
        
        r = input("> ")
        
        if r.lower() == "s":
            sys.exit()
            
        # 2. Converte a lista em um dicionário temporário para buscar a função direto
        acoes = dict(OPCOES_MENU)
        
        if r in acoes:
            acoes[r]() # Executa a função correspondente
        else:
            escrever("Opção incorreta!\n")
            time.sleep(1.5)
            
if __name__ == "__main__":
    main()
    
# Anderson_Tsunami.11Xx
