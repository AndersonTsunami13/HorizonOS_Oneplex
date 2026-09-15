# HorizonOS_X.py
import time, sys, random
from datetime import datetime

from Engine.UI_Engine_ConsoleX import escrever, limpar
from Information.info import inicio_sistema, name_tegs_system
from Information.dados import name_user

# Comandos
def f_mostrar_ajuda():

    escrever("\n=== COMANDOS ===", "CYAN")

    lista = [
        "ajuda",
        "meu_pc",
        "tempo"
    ]

    for comando in lista:
        escrever(f"- {comando}")

def f_tempo():
    hora = time.strftime("%H:%M:%S")
    data = time.strftime("%d/%m/%Y")

    uptime = int(time.time()-inicio_sistema)

    escrever(f"Hora: {hora}", "CYAN")
    escrever(f"Data: {data}", "CYAN")
    escrever(f"Sistema ligado: {uptime}s", "CYAN")

# Dicionário
comandos = {

    "ajuda":f_mostrar_ajuda,
    "tempo":f_tempo
}


# Terminal principal
def iniciar_terminal():
    limpar()

    escrever("HorizonOS Professional XWin One", "GREEN")

    escrever("Digite ajuda", "CYAN")

    while True:
        try:
            comando=input(f"\n{name_user}@{name_tegs_system}> ").lower().strip()

            if comando in comandos:
                comandos[comando]()

            else:
                escrever(f"Comando '{comando}' não existe", "RED")

        except KeyboardInterrupt:
            escrever("\nSistema interrompido", "RED")
            break

if __name__=="__main__":

    iniciar_terminal()