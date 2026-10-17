# MDL_escrever.py

import sys
import time
import re

from Information.dados import MODO_ESCRITA


# ==========================================
# COLORAMA
# ==========================================

try:

    from colorama import init, Fore, Back, Style

    init(
        autoreset=False,
        strip=False
    )

    COLORAMA_DISPONIVEL = True

except ImportError:

    COLORAMA_DISPONIVEL = False


# ==========================================
# CORES ANSI
# ==========================================

ANSI_TEXTOS = {
    "BLACK": "\033[30m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m"
}


ANSI_FUNDOS = {
    "BLACK": "\033[40m",
    "RED": "\033[41m",
    "GREEN": "\033[42m",
    "YELLOW": "\033[43m",
    "BLUE": "\033[44m",
    "MAGENTA": "\033[45m",
    "CYAN": "\033[46m",
    "WHITE": "\033[47m"
}


ANSI_ESTILOS = {
    "normal": "\033[22m",
    "destaque": "\033[1m",
    "apagado": "\033[2m",
    "reset": "\033[0m"
}


# ==========================================
# COLORAMA
# ==========================================

if COLORAMA_DISPONIVEL:

    TEXTOS = {
        "BLACK": Fore.BLACK,
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
        "YELLOW": Fore.YELLOW,
        "BLUE": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE
    }

    FUNDOS = {
        "BLACK": Back.BLACK,
        "RED": Back.RED,
        "GREEN": Back.GREEN,
        "YELLOW": Back.YELLOW,
        "BLUE": Back.BLUE,
        "MAGENTA": Back.MAGENTA,
        "CYAN": Back.CYAN,
        "WHITE": Back.WHITE
    }

    ESTILOS = {
        "normal": Style.NORMAL,
        "destaque": Style.BRIGHT,
        "apagado": Style.DIM,
        "reset": Style.RESET_ALL
    }


# ==========================================
# CURSOR
# ==========================================

def cursor(estado):

    if estado:

        print("\033[?25h", end="")

    else:

        print("\033[?25l", end="")

    sys.stdout.flush()


# ==========================================
# MONTA MENSAGEM COLORAMA
# ==========================================

def montar_colorama(
    texto,
    cor,
    estilo,
    fundo
):

    return (
        ESTILOS.get(
            estilo,
            Style.NORMAL
        )
        +
        FUNDOS.get(
            fundo,
            Back.BLACK
        )
        +
        TEXTOS.get(
            cor,
            Fore.WHITE
        )
        +
        texto
        +
        Style.RESET_ALL
    )


# ==========================================
# MONTA MENSAGEM ASCII
# ==========================================

def montar_ascii(
    texto,
    cor,
    estilo,
    fundo
):

    return (
        ANSI_ESTILOS.get(
            estilo,
            ANSI_ESTILOS["normal"]
        )
        +
        ANSI_FUNDOS.get(
            fundo,
            ANSI_FUNDOS["BLACK"]
        )
        +
        ANSI_TEXTOS.get(
            cor,
            ANSI_TEXTOS["WHITE"]
        )
        +
        texto
        +
        ANSI_ESTILOS["reset"]
    )


# ==========================================
# ESCREVER
# ==========================================

def mdl_escrever(
    texto,
    cor="CYAN",
    estilo="normal",
    fundo="BLACK",
    velocidade=0.04,
    pular_linha=True,
    performance=False,
    mesma_linha=False,
    COLORAMA_OK=True
):

    # ======================================
    # PERFORMANCE
    # ======================================

    if performance:

        velocidade = 0


    # ======================================
    # MODO COLORAMA
    # ======================================

    if MODO_ESCRITA == "COLORAMA":

        if not COLORAMA_DISPONIVEL:

            print(texto)

            return

        mensagem = montar_colorama(
            texto,
            cor,
            estilo,
            fundo
        )


    # ======================================
    # MODO ASCII
    # ======================================

    elif MODO_ESCRITA == "ASCII":

        mensagem = montar_ascii(
            texto,
            cor,
            estilo,
            fundo
        )


    # ======================================
    # MODO SYS
    # ======================================

    elif MODO_ESCRITA == "SYS":

        mensagem = texto


    # ======================================
    # MODO INVÁLIDO
    # ======================================

    else:

        mensagem = texto


    # ======================================
    # CURSOR
    # ======================================

    cursor(False)


    # ======================================
    # MESMA LINHA
    # ======================================

    if mesma_linha:

        print(
            "\r\033[K",
            end=""
        )

        print(
            mensagem,
            end="",
            flush=True
        )


    # ======================================
    # EFEITO DE DIGITAÇÃO
    # ======================================

    else:

        # SYS não precisa interpretar códigos ANSI
        if MODO_ESCRITA == "SYS":

            print(
                mensagem,
                end=""
            )

        else:

            partes = re.split(
                r'(\x1b\[[0-9;]*m)',
                mensagem
            )

            for parte in partes:

                # Código ANSI
                if re.match(
                    r'\x1b\[[0-9;]*m',
                    parte
                ):

                    print(
                        parte,
                        end=""
                    )

                # Texto normal
                else:

                    for caractere in parte:

                        print(
                            caractere,
                            end="",
                            flush=True
                        )

                        if velocidade > 0:

                            time.sleep(
                                velocidade
                            )


    # ======================================
    # QUEBRA DE LINHA
    # ======================================

    if pular_linha:

        print()


    # ======================================
    # FINALIZA
    # ======================================

    sys.stdout.flush()

    cursor(True)