# MDL_status_bar_one.py

import threading
import time
from colorama import init, Fore, Back, Style
init(autoreset=True)
from MDL_texto_rolando import code_au

notification_status_bar_two = "Sistema quieto."
pos = 0

def mostrar_status_bar_two():
    global notification_status_bar_two
    global pos

    while not parar_bar_two.is_set():
        mensagem, pos = code_au(notification_status_bar_two, 50, pos)
        barra = (Back.WHITE + Fore.BLACK + f" Message: {mensagem}" + Style.RESET_ALL)
        print(f"\033[s\033[2;1H{barra}\033[K\033[u", end="", flush=True)
        time.sleep(0.2)
    print("status_bar_two encerrada. ")

parar_bar_two = threading.Event()

def code_as():
    global status_bar_two

    status_bar_two = threading.Thread(target=mostrar_status_bar_two, daemon=True)
    status_bar_two.start()

def code_as2(message):
    global notification_status_bar_two
    notification_status_bar_two = message

def code_as3():
    parar_bar_two.set()
    status_bar_two.join()

# Anderson_TSunami.11Xx