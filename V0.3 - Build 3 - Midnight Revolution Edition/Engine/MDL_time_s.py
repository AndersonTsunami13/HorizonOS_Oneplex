# MDL_time_s.py

# Importação
import time, sys

# Serve para saber se o sistema pode fazer o usuario esperar ou não, feito especialmente para debug
try:
    from Information.devmode import time_e
except ImportError:
    time_e = True

# essa funcão substitui o time.sleep() para uma tecnica de escrita melhor
def mdl_time_s(t):
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    if time_e:
        time.sleep(t)
    else:
        time.sleep(0)
    
    sys.stdout.write("\033[?25h") # Sequência ANSI para mostrar o cursor
    sys.stdout.flush() # faz a saída ser exibida imediatamente

if __name__ == "__main__":
    mdl_time_s(1) # chama a função para testar o tempo de espera

# Anderson_Tsunami.M3_E36