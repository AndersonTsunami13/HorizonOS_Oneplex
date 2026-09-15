# UI/boot.py

import time

from Information.info import *
from Information.devmode import assist_message
from Engine.UI_Engine_ConsoleX import escrever, enter, limpar, escrever_loading, pular_linha
from UI.assist import *
from UI.anim.loading import loading

# ==== boot ====
# simulacao de inicializacao de um sistema
def boot_sequence():
    limpar()

    escrever_loading(2, f"Starting {name_system}", "RED")
    escrever(f"\n{name_system} - {versao_system}", "GREEN", "destaque")

    escrever_loading(1, "Carregando núcleo", "YELLOW")
    escrever("[OK] Núcleo carregado", "YELLOW")
    escrever_loading(1, "Carregando interface", "YELLOW")
    escrever("[OK] Interface Terminal pronta")

    escrever("\nDigite 'ajuda' para listar os comandos disponíveis\n", "CYAN")

    if assist_message:
        escrever("-" * 50)
        escrever("\n\n✓ conheça o novo assistente:\n")
        time.sleep(0.8)
        escrever(dead, "RED")
        time.sleep(0.2)
        escrever("[D.E.A.D.]: Cuidado é irrelevante. Você já foi deletado.\n", "RED")
        time.sleep(1)
    else:
        pular_linha()