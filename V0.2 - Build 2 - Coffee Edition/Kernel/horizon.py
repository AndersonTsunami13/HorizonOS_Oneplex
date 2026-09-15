# Horzion.py

from Information.dados import UI_ENGINE

import sys

def start_system():
    if UI_ENGINE == "XConsole":
        from Engine.UI_Engine_ConsoleX import loading1
        from Kernel.verification import system_verification
        from UI.bios.bios_1 import bios_sequence
        from UI.boot.boot_1 import boot_sequence
        from UI.login.login import login
        from Horizon.HorizonOS_X import iniciar_terminal

        loading1()
        system_verification(False)
        bios_sequence()
        boot_sequence()
        login()
        iniciar_terminal()
    elif UI_ENGINE == "XGUI":
        print("A interface gráfica ainda não está implementada. Por favor, use a interface XConsole.")
        input()
    elif UI_ENGINE == "WIN":
        print("A interface gráfica ainda não está implementada. Por favor, use a interface XConsole.")
        input()