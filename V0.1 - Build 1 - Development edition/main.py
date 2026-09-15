# main.py
# HorizonOS Oneplex
# V0.1 - build 1 - Development edition
# construído por Anderson_Tsunami.11Xx

# Melhor exagerar no comentário agora, do que chorar no futuro tentando entender... "Pagar 1 hoje é melhor do que pagar 2 amanhã." – Hacker filósofo 🕶️

# Inportações das bibliotecas
import os
import sys

from Kernel.horizon import start_system
from UI.system.SystemFailed_screen import tela_da_morte

if __name__ == "__main__" :

    TF_T = 1
    TF_F = True

    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear") 
            start_system()

        except Exception as erro:
            import traceback
            erro_completo = traceback.format_exc()

            if TF_T == 2:
                TF_F = True
            else:
                TF_T += 1

            tela_da_morte(
                CD="System-failed-ini",

                AA="Main.py", 

                C="O erro geralmente acontece no arquivo principal ou em arquivos que travam.", 

                L="start_system()",

                TF = TF_F,

                erroname =  str(erro),

                errocomplet = erro_completo
            )