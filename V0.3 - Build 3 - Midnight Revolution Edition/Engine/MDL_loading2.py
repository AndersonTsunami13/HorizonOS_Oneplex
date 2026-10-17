# MDL_loading2.py

import sys, time, os, platform

def limpar():
    try:
        from Information.devmode import limpar_on
    except:
        limpar_on = True
    
    if limpar_on:
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print("\n")

def mdl_loading2(duracao=3):
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    sistema = platform.system()
    if sistema == "Windows": 
        os.system(f"title _")
    else:
        print(f"\033]0;_\a", end="")

    for _ in range(duracao):

        for pontos in [
            " ",
            "_"
        ]:
            
            sys.stdout.write(f"\r{pontos}")

            sys.stdout.flush()
            time.sleep(0.5)

    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

if __name__ == "__main__":
    mdl_loading2(3)

# Anderson_Tsunami.M3_E36