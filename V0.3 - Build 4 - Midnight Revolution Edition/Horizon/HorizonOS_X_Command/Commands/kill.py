# kill.py

from Information.info import command_kill
from UI.system.BSOD import bsod

def f_kill(argumento):
    if command_kill:
        while True:
            bsod()
    else:
        print("O comando está desativado.")