# MDL_cursor_posicionar.py

# Esse modulo é responsavel por mover o cursor do console para lugares especificos.
def mdl_cursor_posicionar(linha, coluna):
    print(f"\033[{linha};{coluna}H", end="")

if __name__ == "__main__":
    mdl_cursor_posicionar(3, 4)  # Exemplo de uso: move o cursor para a linha 3, coluna 4

# Anderson_Tsunami.M3_E36