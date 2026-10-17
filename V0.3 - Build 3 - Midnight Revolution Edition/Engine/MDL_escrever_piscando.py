# MDL_escrever_piscando.py

import time

def posicionar(linha, coluna):
    print(f"\033[{linha};{coluna}H", end="")

def mdl_escrever_piscando(texto, x, y, vezes, delay):
    for i in range(vezes):
        posicionar(x, y)
        print(texto, end="", flush=True)
        time.sleep(delay)
        
        # Só apaga se NÃO for a última repetição
        if i < vezes - 1:
            posicionar(x, y)
            print(" " * len(texto), end="", flush=True)
            time.sleep(delay)

if __name__ == "__main__":
    texto = "Olá, mundo!"
    x = 5  # Linha
    y = 10  # Coluna
    vezes = 5
    delay = 0.5  # segundos

    mdl_escrever_piscando(texto, x, y, vezes, delay)
            
# Anderson_Tsunami.M3_E36