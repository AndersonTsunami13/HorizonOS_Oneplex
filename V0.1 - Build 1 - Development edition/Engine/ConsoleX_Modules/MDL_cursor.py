# MDL_cursor.py

# Importações
import sys

# Esse modulo é responsavel por mostrar ou ocultar o cursor do console.

def code_ag(o):
    if o:
        sys.stdout.write("\033[?25h") # Sequência ANSI para mostrar o cursor
        sys.stdout.flush() # faz a saída ser exibida imediatamente
    else:
        sys.stdout.write("\033[?25l") # Sequência ANSI para esconder o cursor
        sys.stdout.flush() # faz a saída ser exibida imediatamente

# Anderson_Tsunami.11Xx