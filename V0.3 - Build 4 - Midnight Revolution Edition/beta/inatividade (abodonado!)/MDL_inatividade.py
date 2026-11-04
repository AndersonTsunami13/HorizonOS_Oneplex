# MDL_inatividade.py
# HorizonOS Oneplex
# Monitor de inatividade multiplataforma: Linux + Windows

import os
import sys
import time
import threading

from Engine.MDL_escrever import mdl_escrever as escrever
from Engine.MDL_limpar import mdl_limpar as limpar

from UI.system.sleep_screen import (
    sleep_screen,
    atualizar_relogio
)
from UI.system.lock_screen import lock_screen, lock_screen_2

# Importa somente as bibliotecas do sistema atual.
if os.name == "nt":
    import msvcrt
else:
    import select
    import termios
    import tty


# Exemplo: altere antes de usar.
# Não publique uma senha real no GitHub.
SENHA_BLOQUEIO = "troque_esta_senha"


class MonitorInatividade:
    def __init__(self, descanso=60, bloqueio=120):
        self.descanso = descanso
        self.bloqueio = bloqueio

        self.ultima_atividade = time.monotonic()
        self.estado = "normal"

        self.lock = threading.Lock()
        self.parar = threading.Event()

        self.thread = threading.Thread(
            target=self._monitorar,
            daemon=True
        )

    def iniciar(self):
        self.thread.start()

    def registrar_atividade(self):
        with self.lock:
            self.ultima_atividade = time.monotonic()

    def obter_estado(self):
        with self.lock:
            return self.estado

    def retomar(self):
        with self.lock:
            self.ultima_atividade = time.monotonic()
            self.estado = "normal"

    def _monitorar(self):
        while not self.parar.wait(0.2):
            with self.lock:
                inativo = (
                    time.monotonic() - self.ultima_atividade
                )

                if inativo >= self.bloqueio:
                    self.estado = "bloqueado"
                elif inativo >= self.descanso:
                    self.estado = "descanso"
                else:
                    self.estado = "normal"

    def parar_monitor(self):
        self.parar.set()


def _ler_tecla():
    """Lê uma tecla sem bloquear o monitor de inatividade."""
    if os.name == "nt":
        if not msvcrt.kbhit():
            return None

        tecla = msvcrt.getwch()

        # Ignora teclas especiais, como setas e teclas de função.
        if tecla in ("\x00", "\xe0"):
            if msvcrt.kbhit():
                msvcrt.getwch()
            return None

        return tecla

    leitura, _, _ = select.select(
        [sys.stdin], [], [], 0
    )

    if leitura:
        return sys.stdin.read(1)

    return None


def _ler_senha():
    """Lê a senha mostrando apenas asteriscos."""
    senha = ""

    while True:
        tecla = _ler_tecla()

        if tecla is None:
            time.sleep(0.02)
            continue

        if tecla in ("\r", "\n"):
            print()
            return senha

        if tecla in ("\b", "\x7f", "\x08"):
            if senha:
                senha = senha[:-1]
                print("\b \b", end="", flush=True)
            continue

        if tecla.isprintable():
            senha += tecla
            print("*", end="", flush=True)


def _preparar_terminal():
    """Ativa a leitura de teclas sem ENTER no Linux."""
    if os.name == "nt":
        return None

    fd = sys.stdin.fileno()
    original = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    return original


def _restaurar_terminal(original):
    if os.name != "nt" and original is not None:
        termios.tcsetattr(
            sys.stdin.fileno(),
            termios.TCSADRAIN,
            original
        )


def _restaurar_prompt(prompt, entrada):
    limpar()
    print(prompt + entrada, end="", flush=True)


def ler_entrada_com_inatividade(prompt, monitor):
    entrada = ""
    estado_exibido = "normal"
    ultimo_relogio = 0

    configuracao_original = _preparar_terminal()

    try:
        print(prompt, end="", flush=True)

        while True:
            estado = monitor.obter_estado()

            # Desenha cada tela somente ao entrar naquele estado.
            if estado != estado_exibido:
                if estado == "descanso":
                    limpar()
                    sleep_screen()
                    ultimo_relogio = 0

                elif estado == "bloqueado":
                    lock_screen()

                elif estado == "normal":
                    _restaurar_prompt(prompt, entrada)

                estado_exibido = estado

            # Atualiza o relógio da tela de descanso.
            if estado == "descanso":
                agora = time.monotonic()

                if agora - ultimo_relogio >= 1:
                    atualizar_relogio()
                    ultimo_relogio = agora

            tecla = _ler_tecla()

            if tecla is None:
                time.sleep(0.02)
                continue

            # Durante o descanso, qualquer tecla retoma a sessão.
            if estado == "descanso":
                monitor.retomar()
                continue

            # Na tela bloqueada, ENTER abre a janela da senha.
            if estado == "bloqueado":
                if tecla not in ("\r", "\n"):
                    continue

                lock_screen_2()
                senha_digitada = _ler_senha()

                if senha_digitada == SENHA_BLOQUEIO:
                    monitor.retomar()
                else:
                    limpar()
                    escrever("Senha incorreta!", "RED")
                    time.sleep(1)
                    lock_screen()

                estado_exibido = "bloqueado"
                continue

            # Entrada normal do terminal.
            monitor.registrar_atividade()

            if tecla in ("\r", "\n"):
                print()
                return entrada

            if tecla in ("\b", "\x7f", "\x08"):
                if entrada:
                    entrada = entrada[:-1]
                    print("\b \b", end="", flush=True)

            elif tecla.isprintable():
                entrada += tecla
                print(tecla, end="", flush=True)

    finally:
        _restaurar_terminal(configuracao_original)
