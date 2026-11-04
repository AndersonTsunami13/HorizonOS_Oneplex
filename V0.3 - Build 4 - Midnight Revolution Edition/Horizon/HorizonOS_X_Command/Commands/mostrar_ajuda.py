# mostrar_ajuda.py

from Engine.MDL_escrever import mdl_escrever as escrever

from .list_command import lista

# Comandos
def f_mostrar_ajuda(argumento):

    if argumento == "pass":
        escrever("\n=== COMANDOS ===", "CYAN", performance=True)

        for comando in lista:
            escrever(f"- {comando}", performance=True)
    else:
        escrever("\n=== COMANDOS ===", "CYAN")

        for comando in lista:
            escrever(f"- {comando}")