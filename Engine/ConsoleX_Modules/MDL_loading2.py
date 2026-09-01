import sys, time, os

from Engine.ConsoleX_Modules.MDL_limpar import code_aa as limpar
from Engine.ConsoleX_Modules.MDL_titulo_console import code_ae as titulo_console
from Engine.ConsoleX_Modules.MDL_cursor import code_ag as cursor

def code_ap(duracao=3):

    cursor(False)

    titulo_console("_")

    for _ in range(duracao):

        for pontos in [
            " ",
            "_"
        ]:
            
            sys.stdout.write(
                f"\r{pontos}"
            )

            sys.stdout.flush()

            time.sleep(0.5)

    cursor(True)

    limpar()