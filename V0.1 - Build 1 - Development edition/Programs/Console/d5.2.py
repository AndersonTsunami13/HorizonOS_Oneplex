import time
import random
import sys

# ------------------------
# ANIMAÇÃO DOS "..."
# ------------------------
def animar_pontos(texto, duracao=1.5):
    inicio = time.time()
    dots = ""

    while time.time() - inicio < duracao:
        sys.stdout.write("\r" + texto + dots + "   ")
        sys.stdout.flush()

        time.sleep(0.3)

        dots += "."
        if len(dots) > 3:
            dots = ""

    print()  # quebra linha depois

# ------------------------
# PROGRESSO 0 → 100
# ------------------------
def progresso_completo(texto):
    progresso = 0

    while progresso < 100:
        sys.stdout.write(f"\r{texto} {int(progresso)}% concluído...   ")
        sys.stdout.flush()

        # comportamento mais "realista"
        if progresso < 30:
            progresso += random.uniform(1.5, 4)
            time.sleep(0.08)

        elif progresso < 80:
            progresso += random.uniform(0.5, 2)
            time.sleep(0.12)

        else:
            progresso += random.uniform(0.2, 0.6)
            time.sleep(0.2)  # desacelera no final 😏

    print(f"\r{texto} 100% concluído...")

# ------------------------
# SEQUÊNCIA HORIZON
# ------------------------

print()

animar_pontos("Atualizando o sistema")
progresso_completo("Atualizando o sistema")

animar_pontos("Atualizando a interface")
progresso_completo("Atualizando a interface")

animar_pontos("Atualizando kernel")
progresso_completo("Atualizando kernel")

animar_pontos('> Loading "especial 🥵🍷"')

progresso_completo("/ Atualizando")
progresso_completo("/ Instalando")

animar_pontos(">>> Aguarde", 2.5)
animar_pontos("/// Inicializando", 3)

print("\nSistema carregado.")