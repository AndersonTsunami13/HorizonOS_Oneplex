# MDL_status_bar_one.py

# Inportações
import threading
import time
from datetime import datetime
from colorama import init, Fore, Back, Style

# Modulo resposavel pela animação da status bar.
from MDL_texto_rolando import code_au

# Inicializa o colorama
init(autoreset=True)

# Variável global acessível por todas as funções
notification_status_bar_one = "Sistema ativo." # Mensagem da primeira linha.
pos = 0 # variavel do modulo texto rolando.

def mostrar_status_bar_one():
    global notification_status_bar_one
    global pos

    # Atualiza a barra de status em segundo plano
    while not parar_bar_one.is_set():
        mensagem, pos = code_au(notification_status_bar_one, 35, pos)
        hora = datetime.now().strftime("%H:%M:%S")
        
        # Monta a string formatada
        barra = (Back.WHITE + Fore.BLACK + f" HorizonOS - {mensagem} - {hora} " + Style.RESET_ALL)
        print(f"\033[s\033[1;1H{barra}\033[K\033[u", end="", flush=True)
        time.sleep(0.2) # delay da barra de status

    print("status_bar encerrada. ")

parar_bar_one = threading.Event()

def code_ar(): # inicia a status bar
    global status_bar_one

    status_bar_one = threading.Thread(target=mostrar_status_bar_one, daemon=True)
    status_bar_one.start()

def code_ar2(message): # muda a mensagem da status bar
    global notification_status_bar_one
    notification_status_bar_one = message

def code_ar3(): # encerrar a status bar
    parar_bar_one.set()
    status_bar_one.join()

# Anderson_TSunami.11Xx