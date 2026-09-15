# MDL_perguntar.py

# Modulo para substituir o input padrão do python por um talvez mais eficiente.

def mdl_perguntar(texto, x=1, y=1, cor=None, fundo=None, tipo=str, xy=True):

    # dicionário de cores
    cores = {
        "BLACK": "\033[30m",
        "RED": "\033[31m",
        "GREEN": "\033[32m",
        "YELLOW": "\033[33m",
        "BLUE": "\033[34m",
        "MAGENTA": "\033[35m",
        "CYAN": "\033[36m",
        "WHITE": "\033[37m"
    }

    fundos = {
        "BLACK": "\033[40m",
        "RED": "\033[41m",
        "GREEN": "\033[42m",
        "YELLOW": "\033[43m",
        "BLUE": "\033[44m",
        "WHITE": "\033[47m"
    }

    # Posiciona o cursor
    if xy:
        print(f"\033[{y};{x}H", end="")

    # Define as cores
    if cor:
        print(cores.get(cor.upper(), ""), end="")

    if fundo:
        print(fundos.get(fundo.upper(), ""), end="")

    # Pergunta
    resposta = input(texto)

    # Volta ao padrão
    print("\033[0m", end="")

    # Converte para o tipo solicitado
    return tipo(resposta)
    
# teste
if __name__ == "__main__":
    idade = mdl_perguntar(
        "Idade: ",
        x=4,
        y=7,
        cor="BLUE",
        fundo="WHITE",
        tipo=int,
        xy=False
    )

    print(idade + 1)
    input()

# Anderson_Tsunami.M3_E36