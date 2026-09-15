# MDL_titulo_console.py

# Importações
import os, platform

# título na janela do terminal 
def code_ae(nome):
    sistema = platform.system() # pega o sistema operacional do usuário

    if sistema == "Windows": 
        os.system(f"title {nome}") # esse comando funciona perfeitamente no Windows

    else:
        print(f"\033]0;{nome}\a", end="") # esse comando funciona perfeitamente no Linux e MacOS, ja que o comando "title" não é reconhecido nesses sistemas operacionais.

# Anderson_Tsunami.11Xx