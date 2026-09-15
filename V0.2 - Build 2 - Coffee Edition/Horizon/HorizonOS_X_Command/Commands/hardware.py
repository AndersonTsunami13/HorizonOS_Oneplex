# hardware.py

from Kernel.hardware import RAM_TOTAL, RAM_USADA, VRAM_TOTAL, VRAM_USADA, DISCO_TOTAL, DISCO_USADO, CPU_NAME, CPU_USO, rede_active, rede_download, rede_upload, ram_livre, vram_livre, disco_livre
from Engine.UI_Engine_ConsoleX import escrever

def f_hardware(argumento):
    escrever(f"""
Total de memoria ram: {RAM_TOTAL}MB
Memoria ram usada: {RAM_USADA}MB
memoria ram livre: {ram_livre}MB

Total de vram: {VRAM_TOTAL}MB
Vram usada: {VRAM_USADA}MB
Vram livre: {vram_livre}MB

Total de disco: {DISCO_TOTAL}MB
Disco usado: {DISCO_USADO}MB
Disco livre: {disco_livre}MB

Nome do processador: {CPU_NAME}
uso de processador: {CPU_USO}%

Status da rede: {rede_active}
rede - download: {rede_download}MB/s
rede - upload: {rede_upload}MB/s

""")

def f_ram(argumento):
    escrever(f"""
Total de memoria ram: {RAM_TOTAL}MB
Memoria ram usada: {RAM_USADA}MB
memoria ram livre: {ram_livre}MB
""")


def f_disco(argumento):
    escrever(f"""
Total de disco: {DISCO_TOTAL}MB
Disco usado: {DISCO_USADO}MB
Disco livre: {disco_livre}MB
""")

def f_cpu(argumento):
    escrever(f"""
Nome do processador: {CPU_NAME}
uso de processador: {CPU_USO}%
""")

def f_vram(argumento):
    escrever(f"""
Total de vram: {VRAM_TOTAL}MB
Vram usada: {VRAM_USADA}MB
Vram livre: {vram_livre}MB
""")

def f_rede(argumento):
    escrever(f"""
Status da rede: {rede_active}
rede - download: {rede_download}MB/s
rede - upload: {rede_upload}MB/s
""")