# MDL_dynamic_bar.py

# Importações
import threading, time, shutil
from datetime import datetime

def texto_rolando(texto, largura, posicao=0): # Função MDL_texto_rolando.py otimizada nesse módulo.
    if len(texto) <= largura: 
        return texto.ljust(largura), 0
    texto_animado = (" " * largura) + texto + (" " * largura)
    if posicao >= len(texto_animado): 
        posicao = 0
    trecho = texto_animado[posicao:posicao + largura] 
    if len(trecho) < largura: 
        trecho = trecho.ljust(largura)
    return trecho, posicao + 1

# ============================================================
# VARIÁVEIS
# ============================================================

# Mensagem da primeira linha
notification_dynamic_bar = "Sistema ativo."

# Variável do módulo texto rolando
pos = 0

# Valores simulados da Dynamic Bar
cpu = 12
ram = 51


# Evento para encerrar a Status Bar
parar_dynamic_bar = threading.Event()


def mostrar_dynamic_bar():

    global notification_dynamic_bar
    global pos
    global cpu
    global ram

    # Atualiza a barra de status em segundo plano
    while not parar_dynamic_bar.is_set():

        # Animação da mensagem
        mensagem, pos = texto_rolando(
            notification_dynamic_bar,
            35,
            pos
        )

        # Horário
        hora = datetime.now().strftime("%H:%M:%S")


        # ====================================================
        # STATUS BAR
        # ====================================================

        barra = (
            "\033[47m"
            "\033[30m"
            f" HorizonOS - {mensagem} - {hora} "
            "\033[0m"
        )

        # Primeira linha
        print(
            f"\033[s"
            f"\033[1;1H"
            f"{barra}"
            f"\033[K"
            f"\033[u",
            end="",
            flush=True
        )


        # ====================================================
        # DYNAMIC BAR
        # ====================================================

        # Simulação dos valores
        cpu += 1

        if cpu > 99:
            cpu = 10

        ram += 1

        if ram > 99:
            ram = 30


        # Pega o tamanho atual do terminal
        largura, altura = shutil.get_terminal_size()


        # Monta a Dynamic Bar
        dynamic_bar = (
            "\033[47m"
            "\033[30m"
            f" [●] HorizonOS   "
            f"CPU {cpu}%   "
            f"RAM {ram}%   "
            f"{hora} "
            "\033[0m"
        )


        # Última linha do terminal
        print(
            f"\033[s"
            f"\033[{altura};1H"
            f"{dynamic_bar}"
            f"\033[K"
            f"\033[u",
            end="",
            flush=True
        )


        # Delay
        time.sleep(0.2)


    print("dynamic_bar encerrada.")


# ============================================================
# INICIAR
# ============================================================

def mdl_dynamic_bar_start():

    global dynamic_bar

    dynamic_bar = threading.Thread(
        target=mostrar_dynamic_bar,
        daemon=True
    )

    dynamic_bar.start()


# ============================================================
# ALTERAR MENSAGEM
# ============================================================

def mdl_dynamic_bar(message):

    global notification_dynamic_bar

    notification_dynamic_bar = message


# ============================================================
# ENCERRAR
# ============================================================

def mdl_dynamic_bar_finish():
    
    parar_dynamic_bar.set()
    dynamic_bar.join()

if __name__ == "__main__":
    mdl_dynamic_bar_start()
    time.sleep(5)
    mdl_dynamic_bar("Nova mensagem na Dynamic Bar!")
    time.sleep(5)
    mdl_dynamic_bar_finish()

# Anderson_Tsunami.M3_E36