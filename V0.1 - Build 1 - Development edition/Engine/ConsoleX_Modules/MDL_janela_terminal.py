# MDL_janela_terminal.py

# Esse modulo é usado para para posicionamento do cursor para a construção da janela
from Engine.ConsoleX_Modules.MDL_cursor_posicionar import code_am as cursor

def code_an(linha, coluna, largura, altura, titulo=""):
    # valorize isso! passei horas para fazer a matematica da janela!

    # Linha superior
    cursor(linha, coluna)
    print("┌" + "─" * (largura - 2) + "┐", end="")

    # Meio
    for i in range(1, altura - 1):
        cursor(linha + i, coluna)
        print("│" + " " * (largura - 2) + "│", end="")

    # Linha inferior
    cursor(linha + altura - 1, coluna)
    print("└" + "─" * (largura - 2) + "┘", end="")

    # Título
    if titulo:
        cursor(linha, coluna + 2)
        print(titulo, end="")

# Anderson_Tsunami.11Xx