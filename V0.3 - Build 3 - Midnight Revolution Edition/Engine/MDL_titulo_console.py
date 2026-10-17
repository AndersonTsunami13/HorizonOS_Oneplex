# MDL_titulo_console.py

# Importações
import os, platform

# título na janela do terminal 
def mdl_titulo_console(nome):
    sistema = platform.system() # pega o sistema operacional do usuário

    if sistema == "Windows": 
        os.system(f"title {nome}") # esse comando funciona perfeitamente no Windows
        
    else:
        print(f"\033]0;{nome}\a", end="") # esse comando funciona perfeitamente no Linux e MacOS, ja que o comando "title" não é reconhecido nesses sistemas operacionais.

if __name__ == "__main__":
    mdl_titulo_console("Anderson_Tsunami.M3_E36") # chama a função para mudar o título do terminal

# Anderson_Tsunami.M3_E36