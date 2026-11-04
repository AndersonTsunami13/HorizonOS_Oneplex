# MDL_janela_terminal.py

import time

# Esse modulo é usado para para posicionamento do cursor para a construção da janela
def posicionar(linha, coluna):
    print(f"\033[{linha};{coluna}H", end="")

def mdl_janela_terminal(linha, coluna, largura, altura, titulo="", anim=False, delay=0.02):
    # valorize isso! passei horas para fazer a matematica da janela. porem agora tem animação!
    
    if not anim:
        # Linha superior
        posicionar(linha, coluna)
        print("┌" + "─" * (largura - 2) + "┐", end="")
        
        # Meio
        for i in range(1, altura - 1):
            posicionar(linha + i, coluna)
            print("│" + " " * (largura - 2) + "│", end="")

        # Linha inferior
        posicionar(linha + altura - 1, coluna)
        print("└" + "─" * (largura - 2) + "┘", end="")

    else:
            # Animação de expansão horizontal
            for w in range(2, largura + 1):
                posicionar(linha, coluna)
                print("┌" + "─" * (w - 2) + "┐", end="", flush=True)
                time.sleep(delay)
                
            # Animação de expansão vertical
            for h in range(2, altura + 1):
                # Desenha as laterais até a altura atual h
                for i in range(1, h - 1):
                    posicionar(linha + i, coluna)
                    print("│" + " " * (largura - 2) + "│", end="")
                
                # Desenha o fundo da caixa no nível h - 1
                posicionar(linha + h - 1, coluna)
                print("└" + "─" * (largura - 2) + "┘", end="", flush=True)
                time.sleep(delay)


    # Título
    if titulo:
        posicionar(linha, coluna + 2)
        print(titulo, end="")
        
    posicionar(linha + altura, 1)

if __name__ == "__main__":
    mdl_janela_terminal(5, 10, 30, 10, "Janela de Teste", anim=True, delay=0.05)
    mdl_janela_terminal(16, 10, 40, 10, "Janela de Teste sem animação", anim=False, delay=0.05)

# Anderson_Tsunami.M3_E36