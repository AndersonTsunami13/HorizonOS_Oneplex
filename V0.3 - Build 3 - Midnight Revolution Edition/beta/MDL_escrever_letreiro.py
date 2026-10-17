# MDL_escrever_letreiro.py
import time

def posicionar(linha, coluna):
    # Garante que linha e coluna nunca sejam menores que 1
    l = max(1, linha)
    c = max(1, coluna)
    print(f"\033[{l};{c}H", end="", flush=True)

def limpar_linha(linha):
    # \033[2K limpa a linha inteira de onde o cursor estiver
    print(f"\033[{linha};1H\033[2K", end="", flush=True)

def mdl_escrever_letreiro(texto, inicio_x, fim_x, linha_y, delay=0.03):
    passo = 1 if fim_x > inicio_x else -1
    
    for x in range(inicio_x, fim_x + passo, passo):
        limpar_linha(linha_y)             # 1. Apaga a linha inteira
        posicionar(linha_y, x)            # 2. Vai direto para a posição X correta
        print(texto, end="", flush=True)  # 3. Desenha o texto sem pular linha
        time.sleep(delay)
    
    print()

# --- Teste de Execução ---
if __name__ == "__main__":
    # Opcional: Limpa a tela inteira antes de começar (\033[2J)
    print("\033[2J", end="", flush=True)
    
    # Executa a animação na Linha 5, da Coluna 5 até a 45
    mdl_escrever_letreiro(">>> Anderson_Tsunami.M3_E36 <<<", inicio_x=5, fim_x=45, linha_y=5, delay=0.03)