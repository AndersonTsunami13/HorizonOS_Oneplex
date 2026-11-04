# MDL_limpar.py

# Importação
import os
import sys
import time
import shutil

from Information.animations import limpar_animation

# O devmode.py é chamado para saber se o sistema pode ou nao limpar a tela do terminal.
# Isso é feito especialmente para debug do sistema.
try:
    from Information.devmode import limpar_on
except ImportError:
    limpar_on = True # Se não conseguir importar, assume que pode limpar a tela.

def mdl_limpar():
    if limpar_animation:
        mdl_limpar_2()
    else:
        mdl_limpar_1()

def mdl_limpar_1(): # para limpar a tela
    if limpar_on:
        os.system("cls" if os.name == "nt" else "clear") 
    else:
        print("\n") # Pula uma linha no lugar de limpar a tela

def mdl_limpar_2(velocidade=0.001, caractere="-"):
    """
    Horizon Sweep
    Limpeza animada do terminal para o HorizonOS Oneplex.
    Python puro, sem dependências externas.
    """

    if not sys.stdout.isatty():
        print("\033[2J\033[H", end="", flush=True)
        return

    largura, altura = shutil.get_terminal_size(fallback=(80, 24))

    # Evita ultrapassar a última coluna e provocar quebra de linha.
    largura_barra = max(1, largura - 1)

    try:
        # Esconde o cursor durante a animação.
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

        # Etapa 1: barra crescendo da esquerda para a direita.
        for tamanho in range(1, largura_barra + 1):
            sys.stdout.write(f"\033[{altura};1H")
            sys.stdout.write("\033[2K")
            sys.stdout.write(caractere * tamanho)
            sys.stdout.flush()
            time.sleep(velocidade)

        # Etapa 2: barra subindo e apagando cada linha.
        for linha in range(altura - 1, 0, -1):
            # Apaga a posição anterior da barra.
            sys.stdout.write(f"\033[{linha + 1};1H\033[2K")

            # Limpa a linha que será atravessada.
            sys.stdout.write(f"\033[{linha};1H\033[2K")

            # Desenha a barra na nova posição.
            sys.stdout.write(caractere * largura_barra)
            sys.stdout.flush()
            time.sleep(velocidade * 2)

        # Etapa 3: tela limpa.
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()

    finally:
        # Garante que o cursor volte a aparecer.
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

if __name__ == "__main__":
    mdl_limpar() # Teste da função

# Anderson_Tsunami.M3_E36