# console_bios.py

from Engine.UI_Engine_ConsoleX import limpar, escrever, perguntar

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