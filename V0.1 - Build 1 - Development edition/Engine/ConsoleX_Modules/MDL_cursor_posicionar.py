# MDL_cursor_posicionar.py

# Esse modulo é responsavel por mover o cursor do console para lugares especificos.
def code_am(linha, coluna):
    print(f"\033[{linha};{coluna}H", end="")

# Anderson_Tsunami.11Xx