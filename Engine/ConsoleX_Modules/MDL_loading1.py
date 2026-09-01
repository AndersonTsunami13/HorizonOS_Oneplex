# MDL_loading.py

import time
import sys
import random

from Engine.ConsoleX_Modules.MDL_cursor import code_ag as cursor

def code_ao(text="concluído"):
    
    frames = ["|", "/", "-", "\\"]
    progresso = 0
    frame_index = 0

    cursor(False)  # Desativa o cursor durante a animação

    while progresso <= 101: # 101 para ir até 100% na tela
        # animação + porcentagem na mesma linha
        sys.stdout.write(
            f"\r{frames[frame_index]} {int(progresso)}% {text}..."
        )
        sys.stdout.flush()

        frame_index = (frame_index + 1) % len(frames)

        # progresso mais realista
        if progresso < 30:
            progresso += random.uniform(1, 3)
            time.sleep(0.05)
        elif progresso < 80:
            progresso += random.uniform(0.5, 1.5)
            time.sleep(0.1)
        else:
            progresso += random.uniform(0.2, 0.6)
            time.sleep(0.15)

    cursor(True)  # Reativa o cursor após a animação
    print("\n")
    
# Anderson_Tsunami.11Xx