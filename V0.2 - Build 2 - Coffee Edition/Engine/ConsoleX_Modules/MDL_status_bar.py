# MDL_status_bar.py

# === Inportações ===
import threading, time
from datetime import datetime
from colorama import init, Fore, Back, Style

try:
    from Information.devmode import delay_status_bar as delay
except ImportError:
    delay = 0.02  # Valor padrão caso não seja possível importar

# === Inicializa o colorama ===
init(autoreset=True)

# === Modulo resposavel pela animação da status bar. ===
def texto_animado(texto, largura, posicao=0):
    if len(texto) <= largura: # Se cabe na barra, não anima.
        return texto.ljust(largura), 0

    # Espaços antes e depois para dar efeito de entrada e saída.
    texto_animado = (" " * largura) + texto + (" " * largura)
    
    # Reinicia quando terminar toda a animação.
    if posicao >= len(texto_animado): 
        posicao = 0

    # Pega apenas a parte visível.
    trecho = texto_animado[posicao:posicao + largura] 

    # Caso esteja no final da animação.
    if len(trecho) < largura: 
        trecho = trecho.ljust(largura)

    return trecho, posicao + 1

# === Variável global acessível por todas as funções ===
# Mensagem da primeira linha.
notification_status_bar_1 = "Sistema ativo." 
notification_status_bar_2 = "Sistema quieto."
notification_status_bar_3 = "Sem logs recentes!."

# variavel do modulo texto rolando.
pos = 0 

def mostrar_status_bar_1():
    global notification_status_bar_1
    global pos

    # Atualiza a barra de status em segundo plano
    while not parar_bar_1.is_set():
        mensagem, pos = texto_animado(notification_status_bar_1, 35, pos)
        hora = datetime.now().strftime("%H:%M:%S")
        
        # Monta a string formatada
        barra = (Back.WHITE + Fore.BLACK + f" HorizonOS - {mensagem} - {hora} " + Style.RESET_ALL)
        print(f"\033[s\033[1;1H{barra}\033[K\033[u", end="", flush=True)
        time.sleep(delay)

    print("status_bar_1 encerrada. ")

def mostrar_status_bar_2():
    global notification_status_bar_2
    global pos

    while not parar_bar_2.is_set():
        mensagem, pos = texto_animado(notification_status_bar_2, 50, pos)
        barra = (Back.WHITE + Fore.BLACK + f" Message: {mensagem}" + Style.RESET_ALL)
        print(f"\033[s\033[2;1H{barra}\033[K\033[u", end="", flush=True)
        time.sleep(delay)
    print("status_bar_2 encerrada. ")
    
def mostrar_status_bar_3():
    global notification_status_bar_3
    global pos

    while not parar_bar_3.is_set():
        mensagem, pos = texto_animado(notification_status_bar_3, 52, pos)
        barra = (Back.WHITE + Fore.BLACK + f" Logs - {mensagem}" + Style.RESET_ALL)
        print(f"\033[s\033[3;1H{barra}\033[K\033[u", end="", flush=True)
        time.sleep(delay)
    print("status_bar_3 encerrada. ")

parar_bar_1 = threading.Event()
parar_bar_2 = threading.Event()
parar_bar_3 = threading.Event()

def mdl_status_bar_system_start(): # inicia a status bar
    global status_bar_1

    status_bar_1 = threading.Thread(target=mostrar_status_bar_1, daemon=True)
    status_bar_1.start()

def mdl_status_bar_system(message): # muda a mensagem da status bar
    global notification_status_bar_1
    notification_status_bar_1 = message

def mdl_status_bar_system_finish(): # encerrar a status bar
    parar_bar_1.set()
    status_bar_1.join()

def mdl_status_bar_message_start():
    global status_bar_2

    status_bar_2 = threading.Thread(target=mostrar_status_bar_2, daemon=True)
    status_bar_2.start()

def mdl_status_bar_message(message):
    global notification_status_bar_2
    notification_status_bar_2 = message

def mdl_status_bar_message_finish():
    parar_bar_2.set()
    status_bar_2.join()

def mdl_status_bar_log_start():
    global status_bar_3

    print("\n")
    status_bar_3 = threading.Thread(target=mostrar_status_bar_3, daemon=True)
    status_bar_3.start()

def mdl_status_bar_log(message):
    global notification_status_bar_3  # Agora altera a variável global correta!
    notification_status_bar_3 = message

def mdl_status_bar_log_finish():
    parar_bar_3.set()
    status_bar_3.join()

if __name__ == "__main__":
    # Exemplo de uso
    mdl_status_bar_system_start()
    mdl_status_bar_log_start()
    mdl_status_bar_message_start()
    time.sleep(5)
    mdl_status_bar_system("Nova mensagem na barra de status!")
    mdl_status_bar_message("Nova mensagem na barra de mensagens!")
    mdl_status_bar_log("Novo log registrado!") 
    time.sleep(5)
    mdl_status_bar_system_finish()
    mdl_status_bar_message_finish()
    mdl_status_bar_log_finish()

# Anderson_TSunami.M3_E36