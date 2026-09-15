# HorizonOS_X.py
from Engine.UI_Engine_ConsoleX import escrever, limpar
from Information.info import name_tegs_system
from Information.dados import name_user

from .HorizonOS_X_Command.dc_command import comandos


def iniciar_terminal():
    limpar()

    escrever("HorizonOS Oneplex", "GREEN")
    escrever("Digite ajuda", "CYAN")

    while True:
        try:
            entrada = input(
                f"\n{name_user}@{name_tegs_system}> "
            ).strip()

            partes = entrada.split(" ", 1)

            nome_comando = partes[0].lower()

            argumentos = partes[1] if len(partes) > 1 else ""

            if nome_comando in comandos:
                comandos[nome_comando](argumentos)

            else:
                escrever(
                    f"Comando '{nome_comando}' não existe",
                    "RED"
                )

        except KeyboardInterrupt:
            escrever("\nSistema interrompido", "RED")
            break


if __name__ == "__main__":
    iniciar_terminal()