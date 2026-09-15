# MDL_loading7.py

import sys
import time


def mdl_loading7(duracao=5, velocidade=0.08):
    largura = 15
    blocos = "█████"

    inicio = time.time()

    while time.time() - inicio < duracao:
        for posicao in range(-len(blocos), largura + 1):

            # Monta a barra vazia
            barra = [" "] * largura

            # Coloca os 3 blocos na posição atual
            for i in range(len(blocos)):
                indice = posicao + i

                if 0 <= indice < largura:
                    barra[indice] = blocos[i]

            # Volta para o início da linha
            sys.stdout.write(
                "\r[" + "".join(barra) + "]"
            )
            sys.stdout.flush()

            time.sleep(velocidade)

    # Limpa a barra no final
    sys.stdout.write("\r" + " " * (largura + 2) + "\r")
    sys.stdout.flush()


# Teste
if __name__ == "__main__":
    mdl_loading7(5)