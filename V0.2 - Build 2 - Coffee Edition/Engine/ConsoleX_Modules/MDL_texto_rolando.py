# MDL_texto_rolando.py — Módulo de rolagem de texto do HorizonOS Oneplex

import time

def mdl_texto_rolando(texto, largura, posicao=0, temp_max=5000, limpar=True):
    if len(texto) <= largura:
        print(texto.ljust(largura))
        return

    texto_animado = (" " * largura) + texto + (" " * largura)
    temp = 0

    try:
        while True:
            if posicao >= len(texto_animado):
                posicao = 0

            trecho = texto_animado[posicao:posicao + largura]

            if len(trecho) < largura:
                trecho = trecho.ljust(largura)

            if limpar:
                print("\033[H\033[J", end="")

            print(trecho)

            posicao += 1
            temp += 1

            time.sleep(0.1)

            if temp >= temp_max:
                break

    except KeyboardInterrupt:
        print("\nRolagem interrompida pelo usuário.")


if __name__ == "__main__":
    mdl_texto_rolando("Este é um exemplo de texto rolando na tela. Aperte Ctrl+C para interromper a rolagem.", 30)

# Anderson_Tsunami.M3_E36