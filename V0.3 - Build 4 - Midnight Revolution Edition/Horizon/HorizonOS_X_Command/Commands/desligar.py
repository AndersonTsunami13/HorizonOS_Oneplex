# desligar.py

import sys

from Engine.MDL_loading5 import mdl_loading5 as loading5

def f_desligar(argumento):
    if argumento == "flash":
        sys.exit()
    else:
        loading5(5, "Desligando", "YELLOW")
        sys.exit()