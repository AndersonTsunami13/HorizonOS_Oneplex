# mostrar_ajuda.py

from Engine.UI_Engine_ConsoleX import escrever
from .list_command import lista

# Comandos
def f_mostrar_ajuda(argumento):

    escrever("\n=== COMANDOS ===", "CYAN")

    for comando in lista:
        escrever(f"- {comando}")