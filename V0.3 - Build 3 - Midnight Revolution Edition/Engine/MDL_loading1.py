# MDL_loading1.py

import time, sys, random

def mdl_loading1(text="concluído"):
    
    frames = ["|", "/", "-", "\\"]
    progresso = 0
    frame_index = 0

    sys.stdout.write("\033[?25l")  # Desativa o cursor durante a animação
    sys.stdout.flush()

    while progresso <= 101: # 101 para ir até 100% na tela
        # animação + porcentagem na mesma linha
        sys.stdout.write(f"\r{frames[frame_index]} {int(progresso)}% {text}...")
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

    sys.stdout.write("\033[?25h") # Reativa o cursor após a animação
    sys.stdout.flush()
    
    print("\n")

if __name__ == "__main__":
    mdl_loading1("carregando")

# Anderson_Tsunami.M3_E36