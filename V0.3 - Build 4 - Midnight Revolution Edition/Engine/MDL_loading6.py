# MDL_loading6.py

import time

def mdl_loading6(total, delay):
    for i in range(total + 1):
        porcentagem = int((i / total) * 100)
        barra = "█" * i + "░" * (total - i)
        print(f"\r[{barra}] {porcentagem}%", end="", flush=True)
        time.sleep(delay)
    print()
    
if __name__ == "__main__":
    mdl_loading6(30, 0.1)

# Anderson_Tsunami.M3_E36