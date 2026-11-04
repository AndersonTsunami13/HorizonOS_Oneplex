# tempo.py

import time

from Engine.MDL_escrever import mdl_escrever as escrever

from Information.info import inicio_sistema

def f_tempo(argumento):
    hora = time.strftime("%H:%M:%S")
    data = time.strftime("%d/%m/%Y")

    uptime = int(time.time()-inicio_sistema)

    escrever(f"Hora: {hora}", "CYAN")
    escrever(f"Data: {data}", "CYAN")
    escrever(f"Sistema ligado: {uptime}s", "CYAN")