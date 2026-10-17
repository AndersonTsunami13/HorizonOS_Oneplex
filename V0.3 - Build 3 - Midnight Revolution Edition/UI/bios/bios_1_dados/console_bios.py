# console_bios.py

from Engine.MDL_perguntar import mdl_perguntar as perguntar
from Engine.MDL_limpar import mdl_limpar as limpar
from Engine.MDL_escrever import mdl_escrever as escrever

def console_bios():
    while True:
        limpar()
        escrever("O console por enquanto está desativado! digite exit para sair!")
        r = perguntar("> ", xy=False)
        if r == "exit":
            break
        else:
            escrever("Comando não reconhecido! tente novamente.", "RED")
            input()

# Anderson_Tsunami.M3_E36