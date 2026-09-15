# UI/boot.py

import time

from Information.info import *
from Information.devmode import assist_message
from Engine.UI_Engine_ConsoleX import escrever, limpar, pular_linha, loading5
from Information.dados import assist

# ==== boot ====
# simulacao de inicializacao de um sistema
def boot_sequence():
    limpar()

    loading5(2, f"Starting {name_system}", "RED")
    escrever(f"\n{name_system} - {versao_system}", "GREEN", "destaque")

    loading5(1, "Carregando núcleo", "YELLOW")
    escrever("[OK] Núcleo carregado", "YELLOW")
    loading5(1, "Carregando interface", "YELLOW")
    escrever("[OK] Interface Terminal pronta")

    escrever("\nDica: Digite 'ajuda' para listar os comandos disponíveis\n", "CYAN")

    if assist_message:
        escrever("-" * 50)
        escrever("\n\n✓ conheça o novo assistente:\n")
        time.sleep(0.8)
        escrever(assist, "RED")
        time.sleep(0.2)
        escrever("[D.E.A.D.]: Cuidado é irrelevante. Você já foi deletado.\n", "RED")
        time.sleep(1)
    else:
        pular_linha()