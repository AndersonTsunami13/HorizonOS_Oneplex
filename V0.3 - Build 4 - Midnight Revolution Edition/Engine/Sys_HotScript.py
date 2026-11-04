# HotScript.py

import os
import time

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def escrever(texto):
    print(texto)

def executar_linha(linha):

    linha = linha.strip()

    if not linha:
        return

    if linha == "limpar":
        limpar()

    elif linha.startswith("escrever"):
        texto = linha.replace("escrever", "").strip().replace('"', '')
        escrever(texto)

    elif linha.startswith("esperar"):
        try:
            ms = int(linha.split()[1])
            time.sleep(ms / 1000)
        except:
            escrever("erro no esperar")
            
def executar_hotfile(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        for linha in f:
            executar_linha(linha)

def Hotlinguage():
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    arquivo = os.path.join(diretorio_script, "test.hot")

    executar_hotfile(arquivo)
    
if __name__ == "__main__":
    Hotlinguage()
    
# Esse arquivo vai ser responsável pela futura linguagem do horizon
# por enquanto esse e um projeto beta

# Anderson_Tsunami.11Xx