# MDL_cursor_posicionar.py

# Esse modulo é responsavel por mover o cursor do console para lugares especificos.

"""

Metodo de uso:

mdl_cursor_posicionar(1,2)

o primeiro espaço representa a linha e o segundo espaço representa a coluna do terminal

Tambem pode ser representado com x e y
x = 1
y = 2


"""

def mdl_cursor_posicionar(linha, coluna):
    print(f"\033[{linha};{coluna}H", end="")

if __name__ == "__main__":
    mdl_cursor_posicionar(3, 4)  # Exemplo de uso: move o cursor para a linha 3, coluna 4

# Anderson_Tsunami.M3_E36

# Revision 07/10/2026
