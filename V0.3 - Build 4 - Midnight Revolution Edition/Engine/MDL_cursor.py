# MDL_cursor.py

# Importação unica
import sys

# Esse modulo é responsavel por mostrar ou ocultar o cursor do console.

"""

Metodos de uso:

mdl_cursor(False)
# Oculta o cursor do terminal

mdl_cursor(True)
# Mostra o cursor do terminal 

"""

def mdl_cursor(option):
    if option:
        sys.stdout.write("\033[?25h") # Sequência ANSI para mostrar o cursor
        sys.stdout.flush() # faz a saída ser exibida imediatamente
    else:
        sys.stdout.write("\033[?25l") # Sequência ANSI para esconder o cursor
        sys.stdout.flush() # faz a saída ser exibida imediatamente

if __name__ == "__main__":
    mdl_cursor(False)
    input("Pressione Enter para mostrar o cursor...")
    mdl_cursor(True)

# Anderson_Tsunami.M3_E36

# Revision: 06/10/2026
