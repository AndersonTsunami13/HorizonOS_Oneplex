# verification.py

# importações 
import sys, os

from Engine.UI_Engine_ConsoleX import escrever, time_s, titulo_console, cursor, escrever_loading
from UI.anim.loading import loading

def system_verification(a=True): # se for True aparece "Pressione para..." e False não mostra.
    titulo_console("verificando...")
    cursor(False)
    escrever_loading(3, "iniciando verificação", "YELLOW")
    loading()
    time_s(1)

    # Verifica versão do Python
    versao = sys.version_info

    if versao.major == 3 and versao.minor >= 11:
        escrever(f"Python encontrado: {sys.version}",
                 "BLUE")
        time_s(1)

        # verifica se o arquivo existe
        if os.path.exists("main.py"):
            escrever("Arquivo principal (main.py) encontrado com sucesso!",
                     "GREEN")
            time_s(1)

        else:
            titulo_console("hum...")
            escrever("arquivo principal (main.py) não encontrado...",
                  "RED")
            time_s(1)

    else:
        titulo_console("Error")
        escrever("Python 3.11+ necessário",
                 "RED")
        
    cursor(True)
    
    if a:
        titulo_console("Continuando...")
        input("Pressione qualquer tecla para continuar...")
        
if __name__ == "__main__":
        system_verification()
        
# Anderson_Tsunami.11x
