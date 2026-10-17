# MDL_status_bar.py

# === Importações ===
import threading
import time
from datetime import datetime

from colorama import init, Fore, Back, Style


# === Configuração de desenvolvimento ===
try:
    from Information.devmode import delay_status_bar as delay
except ImportError:
    delay = 0.1


# === Inicializa o Colorama ===
init(autoreset=True)


# === Lock do terminal ===
# Evita que duas threads escrevam no terminal exatamente ao mesmo tempo.
terminal_lock = threading.Lock()


# === Função responsável pela animação ===
def texto_animado(texto, largura, posicao=0):

    # Se o texto couber na largura, não precisa animar.
    if len(texto) <= largura:
        return texto.ljust(largura), 0

    # Espaços antes e depois para criar
    # o efeito de entrada e saída.
    texto_animado = (
        (" " * largura)
        + texto
        + (" " * largura)
    )

    # Reinicia a animação quando chegar ao final.
    if posicao >= len(texto_animado):
        posicao = 0

    # Pega somente a parte visível.
    trecho = texto_animado[
        posicao:posicao + largura
    ]

    # Completa com espaços caso necessário.
    if len(trecho) < largura:
        trecho = trecho.ljust(largura)

    return trecho, posicao + 1


# ============================================================
# MENSAGENS
# ============================================================

notification_status_bar_1 = (
    "Sistema ativo.                "
    "taca gelo agachandooooooo                "
    "corpinho de anjo, mente do djabo.                "
    "dinheiro não compra felicidade mas pode comprar uma bmw m3 e36 1996.                "
    "minha querida, não sei qual é sua placa-mãe, mas sei que meu processador se encaixa perfeitamente no seu soquete.                "
    "meu amor, vou ter que comprar um watercooler pra mim, depois que eu te vi chega fiquei quente.                "
    "aqui meu povo, uma caverna, da ate pra morar aqui embaixo.   Aoooooo buraco do djabo.                "
   "o sistema ta calmo, mas ele nem imagina que tem umas 896 abas aberta ao mesmo tempo.                "
   "nois sempre fez coisas perfeitas, mas sua mae... ela foi longe demais.                "
   "eai meu compassa, e aquele negocinho que faz.. jogue na minha papai...    "
)

notification_status_bar_2 = "Sistema quieto."

notification_status_bar_3 = "Sem logs recentes!."


# ============================================================
# POSIÇÃO DAS ANIMAÇÕES
# ============================================================

# Cada barra possui sua própria posição.
pos_1 = 0
pos_2 = 0
pos_3 = 0


# ============================================================
# EVENTOS DE PARADA
# ============================================================

parar_bar_1 = threading.Event()
parar_bar_2 = threading.Event()
parar_bar_3 = threading.Event()


# ============================================================
# STATUS BAR 1
# ============================================================

def mostrar_status_bar_1():

    global notification_status_bar_1
    global pos_1

    while not parar_bar_1.is_set():

        mensagem, pos_1 = texto_animado(
            notification_status_bar_1,
            35,
            pos_1
        )

        hora = datetime.now().strftime("%H:%M:%S")

        barra = (
            Back.WHITE
            + Fore.BLACK
            + f" HorizonOS - {mensagem} - {hora} "
            + Style.RESET_ALL
        )

        with terminal_lock:
            print(
                f"\033[s\033[1;1H{barra}\033[K\033[u",
                end="",
                flush=True
            )

        time.sleep(delay)


# ============================================================
# STATUS BAR 2
# ============================================================

def mostrar_status_bar_2():

    global notification_status_bar_2
    global pos_2

    while not parar_bar_2.is_set():

        mensagem, pos_2 = texto_animado(
            notification_status_bar_2,
            50,
            pos_2
        )

        barra = (
            Back.WHITE
            + Fore.BLACK
            + f" Message: {mensagem}"
            + Style.RESET_ALL
        )

        with terminal_lock:
            print(
                f"\033[s\033[2;1H{barra}\033[K\033[u",
                end="",
                flush=True
            )

        time.sleep(delay)


# ============================================================
# STATUS BAR 3
# ============================================================

def mostrar_status_bar_3():

    global notification_status_bar_3
    global pos_3

    while not parar_bar_3.is_set():

        mensagem, pos_3 = texto_animado(
            notification_status_bar_3,
            52,
            pos_3
        )

        barra = (
            Back.WHITE
            + Fore.BLACK
            + f" Logs - {mensagem}"
            + Style.RESET_ALL
        )

        with terminal_lock:
            print(
                f"\033[s\033[3;1H{barra}\033[K\033[u",
                end="",
                flush=True
            )

        time.sleep(delay)


# ============================================================
# SYSTEM STATUS BAR
# ============================================================

def mdl_status_bar_system_start():
    global status_bar_1

    # Permite iniciar novamente depois de finalizar.
    parar_bar_1.clear()

    status_bar_1 = threading.Thread(
        target=mostrar_status_bar_1,
        daemon=True
    )

    status_bar_1.start()


def mdl_status_bar_system(message):

    global notification_status_bar_1

    notification_status_bar_1 = message


def mdl_status_bar_system_finish():

    parar_bar_1.set()

    if status_bar_1.is_alive():
        status_bar_1.join()


# ============================================================
# MESSAGE STATUS BAR
# ============================================================

def mdl_status_bar_message_start():
    global status_bar_2

    parar_bar_2.clear()

    status_bar_2 = threading.Thread(
        target=mostrar_status_bar_2,
        daemon=True
    )

    status_bar_2.start()


def mdl_status_bar_message(message):

    global notification_status_bar_2

    notification_status_bar_2 = message


def mdl_status_bar_message_finish():

    parar_bar_2.set()

    if status_bar_2.is_alive():
        status_bar_2.join()


# ============================================================
# LOG STATUS BAR
# ============================================================

def mdl_status_bar_log_start():
    global status_bar_3

    parar_bar_3.clear()

    status_bar_3 = threading.Thread(
        target=mostrar_status_bar_3,
        daemon=True
    )

    status_bar_3.start()


def mdl_status_bar_log(message):

    global notification_status_bar_3

    notification_status_bar_3 = message


def mdl_status_bar_log_finish():

    parar_bar_3.set()

    if status_bar_3.is_alive():
        status_bar_3.join()


# ============================================================
# TESTE DO MÓDULO
# ============================================================

if __name__ == "__main__":

    mdl_status_bar_system_start()
    mdl_status_bar_message_start()
    mdl_status_bar_log_start()

    time.sleep(85)

    mdl_status_bar_system(
        "Nova mensagem na barra de status!"
    )

    mdl_status_bar_message(
        "Nova mensagem na barra de mensagens!"
    )

    mdl_status_bar_log(
        "Novo log registrado!"
    )

    time.sleep(5)

    mdl_status_bar_system_finish()
    mdl_status_bar_message_finish()
    mdl_status_bar_log_finish()


# Anderson_TSunami.M3_E36