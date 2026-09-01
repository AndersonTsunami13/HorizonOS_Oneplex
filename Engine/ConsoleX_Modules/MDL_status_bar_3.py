# MDL_status_bar_3.py

import threading
import time

from colorama import init, Fore, Back, Style
init(autoreset=True)

from MDL_texto_rolando import code_au

notification_status_bar_3 = "Sem logs recentes!."
pos = 0

def mostrar_status_bar_3():
    global notification_status_bar_3
    global pos

    while not parar_bar_3.is_set():
        mensagem, pos = code_au(notification_status_bar_3, 52, pos)
        barra = (Back.WHITE + Fore.BLACK + f" Logs - {mensagem}" + Style.RESET_ALL)
        print(f"\033[s\033[3;1H{barra}\033[K\033[u", end="", flush=True)
        time.sleep(0.2)
    print("status_bar_3 encerrada. ")

parar_bar_3 = threading.Event()

def code_at():
    global status_bar_3

    print("\n")
    status_bar_3 = threading.Thread(target=mostrar_status_bar_3, daemon=True)
    status_bar_3.start()

def code_at2(message):
    global notification_status_bar_3  # Agora altera a variável global correta!
    notification_status_bar_3 = message

def code_at3():
    parar_bar_3.set()
    status_bar_3.join()

# Anderson_TSunami.11Xx