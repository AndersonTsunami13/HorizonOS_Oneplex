# hardware.py

import random

from Engine.UI_Engine_ConsoleX import escrever

# Memória e hardware
RAM_TOTAL = 128  # MB
RAM_USADA = 0

VRAM_TOTAL = 32  # MB
VRAM_USADA = 0

DISCO_TOTAL = 1024  # MB
DISCO_USADO_BASE = random.randint(100, 490)
DISCO_USADO_LOGS = 1
DISCO_USADO = 0

CPU_NAME = "Infiel T1155 Series"
CPU_USO = random.uniform(0.1, 95.9)

rede_active = False
rede_download = random.uniform(10.0, 100.0)
rede_upload = random.uniform(2.0, 50.0)

# Funções de hardware
def ram_livre():
    return RAM_TOTAL - RAM_USADA

def vram_livre():
    return VRAM_TOTAL - VRAM_USADA

def disco_livre():
    return DISCO_TOTAL - (DISCO_USADO_BASE + DISCO_USADO_LOGS + DISCO_USADO)

def usar_ram(mb):
    global RAM_USADA
    if ram_livre() >= mb:
        RAM_USADA += mb
        return True
    else:
        escrever("[ERROR] Memória RAM insuficiente!", "RED")
        return False

def liberar_ram(mb):
    global RAM_USADA
    RAM_USADA = max(0, RAM_USADA - mb)

def usar_vram(mb):
    global VRAM_USADA
    if vram_livre() >= mb:
        VRAM_USADA += mb
        return True
    else:
        escrever("[ERROR] Memória VRAM insuficiente!")
        return False

def liberar_vram(mb):
    global VRAM_USADA
    VRAM_USADA = max(0, VRAM_USADA - mb)

def usar_disco(mb):
    global DISCO_USADO
    if disco_livre() >= mb:
        DISCO_USADO += mb
        return True
    else:
        escrever("[ERROR] Espaço em disco insuficiente!", "RED")
        return False

def liberar_disco(mb):
    global DISCO_USADO
    DISCO_USADO = max(0, DISCO_USADO - mb)

# esse arquivo não tem muitos comentários por ser pequeno e fácil de ler, quem sabe mexer com python não vai ter problemas.

# Anderson_Tsunami.11Xx