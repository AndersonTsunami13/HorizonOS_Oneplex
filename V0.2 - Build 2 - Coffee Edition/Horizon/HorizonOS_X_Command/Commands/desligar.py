# desligar.py

import sys

from Engine.UI_Engine_ConsoleX import loading5

def f_desligar(argumento):
    if argumento == "flash":
        sys.exit()
    else:
        loading5(5, "Desligando", "YELLOW")
        sys.exit()