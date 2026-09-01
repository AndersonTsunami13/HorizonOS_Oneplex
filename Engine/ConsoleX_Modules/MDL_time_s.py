# MDL_time_s.py

# Importação
import time

# Serve para ocultar o cursor enquanto o tempo passa
from Engine.ConsoleX_Modules.MDL_cursor import code_ag as cursor
# Serve para saber se o sistema pode fazer o usuario esperar ou não, especialmente feito para debug
from Information.devmode import time_e

# essa funcao substitui o time.sleep() para uma tecnica de escrita melhor
def code_af(t):
    cursor(False)

    if time_e:
        time.sleep(t)
    else:
        time.sleep(0)
    
    cursor(True)

# Anderson_Tsunami.11Xx