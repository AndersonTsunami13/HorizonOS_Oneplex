# Error_screen.py

import sys, time, os, platform

import sys
import time
import os
import platform

def titulo(mensagem="Error"):
    sistema = platform.system()

    if sistema == "Windows":
        os.system(f"title {mensagem}")
    else:
        sys.stdout.write(f"\033]0;{mensagem}\a")
        sys.stdout.flush()

def error_screen(duracao=3, x=1, y=1, mensagem="Error"):
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    for _ in range(duracao):
        for pontos in [
            f"  {mensagem}  ",
            " " * (len(mensagem) + 4)
        ]:
            # Posiciona o cursor em x, y TODA vez
            titulo(mensagem)
            sys.stdout.write(f"\033[{y};{x}H")
            sys.stdout.write(pontos)
            sys.stdout.flush()

            time.sleep(0.5)
            titulo(f"{mensagem}_")

    # Mostra o cursor novamente
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()


if __name__ == "__main__":
    error_screen(duracao=3, x=7, y=9)


# Anderson_Tsunami.M3_E36