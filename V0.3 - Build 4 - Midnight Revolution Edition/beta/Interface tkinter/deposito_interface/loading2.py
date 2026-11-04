import sys
import time

def barra_carregando(duracao=5, tamanho=50):
    for i in range(1, tamanho + 1):
        barra = "█" * i
        porcentagem = int((i / tamanho) * 100)
        sys.stdout.write(f"\r{porcentagem}% {barra}")
        sys.stdout.flush()
        time.sleep(duracao / tamanho)
