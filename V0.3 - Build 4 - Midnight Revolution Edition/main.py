# main.py
# HorizonOS Oneplex
# V0.3 - build 4 - Coffee Edition
# construído por Anderson_Tsunami.M3_E36

# Melhor exagerar no comentário agora, do que chorar no futuro tentando entender... "Pagar 1 hoje é melhor do que pagar 2 amanhã." – Hacker filósofo 🕶️

# [ Dev ] Desconsidere os bugs, isso é uma coisa que vai demorar a ser arrumada... mas ta indo de boa por enquanto...

# Inportações das bibliotecas
import os
import sys
import time

print("[ Debug ] HorizonOS iniciando...")

try:
    from Kernel.horizon import start_system
    from UI.system.SystemFailed_screen import tela_da_morte
    
except Exception as erro:
    print("Erro ao importar arquivos...")
    time.sleep(1)
    print(f"\n{erro}")
    input("Pressione enter para continuar...")

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

            try:
                tela_da_morte(
                    CD="System_failed_Initialization",
                    AA="Main.py", 
                    C="O erro pode está relacionado ao arquivo principal ou nos arquivos do sistema..", 
                    L="system_initialization()",
                    TF = TF_F,
                    erroname =  str(erro),
                    errocomplet = erro_completo
                )
                
            except Exception as erro:
                print("Fatal error!")
                print("\nInformations:\n")
                print(erro_completo)
                input("Pressione enter para continuar...")
                sys.exit()
                
# Anderson_Tsunami.M3_E36
# Revision: 21/10/2026