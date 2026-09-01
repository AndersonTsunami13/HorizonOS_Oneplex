import os

# ~~~~~~~~~~~~~~~~~~~~~~~~
# Minerador (Simulador de Bitcoin)
def salvar_saldo(saldo, arquivo="mineracao.hos"):
    try:
        with open(arquivo, "w") as f:
            f.write(f"{saldo:.4f}")
    except Exception:
        pass

def carregar_saldo(arquivo="mineracao.hos"):
    try:
        if os.path.exists(arquivo):
            with open(arquivo, "r") as f:
                return float(f.read())
    except Exception:
        pass
    return 0.0

def mostrar_barrinha(porcentagem, largura=24):
    preenchido = int(porcentagem * largura)
    vazio = largura - preenchido
    return "[" + "#" * preenchido + "-" * vazio + "]"

def minerar_simulado():
    saldo = carregar_saldo()
    incremento = 0.0004
    delay = 0.5
    try:
        passo = 0
        while True:
            saldo += incremento
            passo += 1
            porcentagem = (passo % 50) / 50
            barra = mostrar_barrinha(porcentagem)
            sys.stdout.write(f"\rMinerando... {barra} Saldo: {saldo:.4f}")
            sys.stdout.flush()
            incremento += 0.00005
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\n")
        salvar_saldo(saldo)
        if input("Deseja resgatar moedas? (s/n): ").strip().lower() == "s":
            salvar_saldo(0.0) 
            
# Fim do minerador
# ~~~~~~~~~~~~~~~