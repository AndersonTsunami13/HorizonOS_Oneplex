# dynamic_bar_v2.py
#
# Dynamic Bar - código de ideia independente
# Anderson_Tsunami.M3_E36

import threading
import time
import shutil
from datetime import datetime


# ============================================================
# CONFIGURAÇÃO INTERNA
# ============================================================

notification_dynamic_bar = ""
titulo_dynamic_bar = "Dynamic Bar"

mostrar_hora = True
mostrar_tempo = False

pos = 0
inicio_dynamic_bar = None

parar_dynamic_bar = threading.Event()
dynamic_bar = None


# ============================================================
# TEXTO ROLANDO
# ============================================================

def texto_rolando(texto, largura, posicao):
    """
    Cria o trecho visível da mensagem.

    A mensagem entra pela direita, atravessa a área disponível
    e sai pela esquerda.
    """

    if largura <= 0:
        return "", 0

    if not texto:
        return " " * largura, 0

    # Espaço antes e depois para separar as mensagens
    texto_animado = (" " * largura) + texto + (" " * largura)

    # Reinicia quando chegou ao final
    if posicao >= len(texto_animado):
        posicao = 0

    trecho = texto_animado[posicao:posicao + largura]

    # Garante que sempre teremos exatamente a largura pedida
    trecho = trecho.ljust(largura)

    return trecho, posicao + 1


# ============================================================
# LADO DIREITO
# ============================================================

def montar_lado_direito():
    """
    Monta as informações que ficam presas no lado direito
    da barra.
    """

    informacoes = []

    if mostrar_hora:
        hora = datetime.now().strftime("%H:%M:%S")
        informacoes.append(hora)

    if mostrar_tempo and inicio_dynamic_bar is not None:
        tempo = int(time.monotonic() - inicio_dynamic_bar)

        horas = tempo // 3600
        minutos = (tempo % 3600) // 60
        segundos = tempo % 60

        tempo_formatado = f"{horas:02}:{minutos:02}:{segundos:02}"

        informacoes.append(f"Ligado: {tempo_formatado}")

    return " | ".join(informacoes)


# ============================================================
# MONTAR A BARRA
# ============================================================

def montar_barra(largura, mensagem):
    """
    Monta a linha completa da Dynamic Bar.

    Estrutura:

    TÍTULO - MENSAGEM ----------------------- HORA | TEMPO
    """

    # Espaços mínimos
    if largura < 10:
        return " " * largura

    # Parte esquerda
    prefixo = f" {titulo_dynamic_bar} - "

    # Parte direita
    lado_direito = montar_lado_direito()

    if lado_direito:
        sufixo = f" {lado_direito} "
    else:
        sufixo = " "

    # Descobre quanto sobra para a mensagem
    espaco_mensagem = largura - len(prefixo) - len(sufixo)

    if espaco_mensagem < 1:
        return (prefixo + sufixo)[:largura].ljust(largura)

    # A mensagem ocupa somente o espaço disponível
    mensagem = mensagem[:espaco_mensagem]

    barra = prefixo + mensagem

    # Preenche o espaço entre mensagem e informações
    barra += " " * (largura - len(barra) - len(sufixo))

    barra += sufixo

    # Segurança: exatamente a largura do terminal
    return barra[:largura].ljust(largura)


# ============================================================
# THREAD DA DYNAMIC BAR
# ============================================================

def mostrar_dynamic_bar():

    global pos

    while not parar_dynamic_bar.is_set():

        # ----------------------------------------------------
        # Tamanho atual do terminal
        # ----------------------------------------------------

        largura, altura = shutil.get_terminal_size()

        # ----------------------------------------------------
        # Parte fixa da esquerda
        # ----------------------------------------------------

        prefixo = f" {titulo_dynamic_bar} - "

        # ----------------------------------------------------
        # Parte fixa da direita
        # ----------------------------------------------------

        lado_direito = montar_lado_direito()

        if lado_direito:
            sufixo = f" {lado_direito} "
        else:
            sufixo = " "

        # ----------------------------------------------------
        # Espaço realmente disponível para a animação
        # ----------------------------------------------------

        espaco_mensagem = largura - len(prefixo) - len(sufixo)

        if espaco_mensagem < 1:
            mensagem = ""
        else:
            mensagem, pos = texto_rolando(
                notification_dynamic_bar,
                espaco_mensagem,
                pos
            )

        # ----------------------------------------------------
        # Monta a barra inteira
        # ----------------------------------------------------

        barra = montar_barra(
            largura,
            mensagem
        )

        # ----------------------------------------------------
        # Vai para a última linha do terminal
        # ----------------------------------------------------

        print(
            f"\033[s"
            f"\033[{altura};1H"
            f"\033[47m"
            f"\033[30m"
            f"{barra}"
            f"\033[0m"
            f"\033[K"
            f"\033[u",
            end="",
            flush=True
        )

        # ----------------------------------------------------
        # Aguarda 0.2 segundos.
        #
        # Event.wait() permite encerrar imediatamente caso
        # parar_dynamic_bar.set() seja chamado.
        # ----------------------------------------------------

        parar_dynamic_bar.wait(0.2)

    # Limpa a barra quando termina
    largura, altura = shutil.get_terminal_size()

    print(
        f"\033[s"
        f"\033[{altura};1H"
        f"\033[K"
        f"\033[u",
        end="",
        flush=True
    )


# ============================================================
# INICIAR
# ============================================================

def mdl_dynamic_bar_start(
    titulo="Dynamic Bar",
    hora=True,
    tempo=False
):
    """
    Inicia a Dynamic Bar.

    titulo = nome mostrado no lado esquerdo
    hora   = mostra o relógio no lado direito
    tempo  = mostra quanto tempo a barra está ligada
    """

    global dynamic_bar
    global titulo_dynamic_bar
    global mostrar_hora
    global mostrar_tempo
    global inicio_dynamic_bar
    global pos

    # Não inicia duas barras ao mesmo tempo
    if dynamic_bar is not None and dynamic_bar.is_alive():
        return

    titulo_dynamic_bar = titulo

    mostrar_hora = hora
    mostrar_tempo = tempo

    # Reseta o estado para permitir reiniciar a barra
    parar_dynamic_bar.clear()

    # Reinicia a animação
    pos = 0

    # Marca o momento em que a barra iniciou
    inicio_dynamic_bar = time.monotonic()

    dynamic_bar = threading.Thread(
        target=mostrar_dynamic_bar,
        daemon=True
    )

    dynamic_bar.start()


# ============================================================
# ALTERAR MENSAGEM
# ============================================================

def mdl_dynamic_bar(message):
    """
    Altera a mensagem exibida na barra.

    A posição da animação é reiniciada para que a nova
    mensagem apareça imediatamente.
    """

    global notification_dynamic_bar
    global pos

    notification_dynamic_bar = str(message)

    # Nova mensagem começa imediatamente
    pos = 0


# ============================================================
# ENCERRAR
# ============================================================

def mdl_dynamic_bar_finish():

    global dynamic_bar

    if dynamic_bar is None:
        return

    if not dynamic_bar.is_alive():
        dynamic_bar = None
        return

    parar_dynamic_bar.set()

    dynamic_bar.join()

    dynamic_bar = None


# ============================================================
# TESTE
# ============================================================

if __name__ == "__main__":

    mdl_dynamic_bar_start(
        titulo="Coffee mode",
        hora=True,
        tempo=True
    )

    mdl_dynamic_bar(
        "Entre todas as pessoas desse mundo, "
        "eu escolhi você pra fazer flexão comigo."
    )

    time.sleep(10)

    mdl_dynamic_bar(
        "Você ainda está aqui? Eu pensei que você fosse embora."
    )

    time.sleep(10)

    mdl_dynamic_bar_finish()

    print("Dynamic Bar encerrada.")
