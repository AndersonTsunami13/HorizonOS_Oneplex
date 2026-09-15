# beta_painel.py

from Engine.UI_Engine_ConsoleX import escrever, limpar, enter, time_s, perguntar
from Information.dados import assist_name

def beta_painel():
    while True:
        limpar()
        escrever("""
    Bem-vindo ao painel de recursos betas do HorizonOS Oneplex.

    Os recursos sao para fazer testes, se não tiver necessidade não use eles aqui! eles serão liberados assim que possível para o sistema limpo.

    Escolha o recuso que você deseja usar:
        1. O relógio fantasma (Ghost clock)
        2. A nova linguagem do Horizon (HotScript)
        3. o teste de multitarefas (vários processos abertos na mesma janela
""", cor="YELLOW")
        
        r = perguntar("> ", xy=False)
        
        if r == "1":
            time_s(1)
            #Ghost_Clock()
        elif r == "2":
            time_s(1)
           # Hotlinguage()
        elif r == "3":
            time_s(1)
           # test1()
        else:
            escrever(f"[{assist_name}] Esse comando não e o certo nobre!")
            enter()

# Anderson_Tsunami.M3_E36