# log_manager.py

import os, sys, time

from Engine.UI_Engine_ConsoleX import escrever, limpar, time_s, sair
from Information.info import LOG_FILE

# funcao para ler o log
def ler_log(log=LOG_FILE):
    limpar()

    escrever(f"\n>>> Conteúdo de {log}\n", "BLUE", "destaque")

    if not os.path.exists(log):
        escrever("O arquivo de log não existe no pacote ", "RED", "apagado")
        return
    
    with open(log, "r") as arquivo:
        for linha in arquivo:
            escrever(linha.strip(), "GREEN")

    escrever("\n>>> Fim do log.\n", "BLUE", "destaque")

# painel de gerenciamento do log
def log_manager():
    while True:
        limpar()

        escrever("""
        >>> [ Bem-vindo ao setor de limpeza do LogX ]
              
        Essa opção foi projetada pra limpar o LogX, por enquanto não pode limpar outros logs.
              
        Escolha uma ação:
        1. Limpar e voltar
        2. Limpar e reiniciar
        3. Limpar e desligar
        4. Escolher um log personalizado
        5. Sair
              
""", "GREEN", "destaque"         
)

        escolha = input(">")

        if escolha == "1":
            with open(LOG_FILE, "w") as arquivo:
                escrever("LogX limpo com sucesso!", "GREEN")

            time_s(0.6)

            limpar()

            break

        elif escolha == "2":
            with open(LOG_FILE, "w") as arquivo:
                escrever("LogX limpo com sucesso!", "GREEN")

            time_s(0.6)

            escrever("Reiniciando o Horizon...", "YELLOW")
            time_s(0.5)

            try:
                break
            except:
                escrever("Não foi possível reiniciar por falta do iniciar terminal().", "RED")
                time_s(0.6)

                break

        elif escolha == "3":
            with open(LOG_FILE, "w") as arquivo:
                escrever("LogX Limpo com sucesso!", "GREEN")

            time_s(0.6)

            escrever("Desligando o Horizon...", "RED")
            time_s(0.5)

            sair()

        elif escolha == "4": 
            escrever("Função ainda não liberada!", "YELLOW")

        elif escolha == "5":
            escrever("Cancelando a ação de limpeza...", "YELLOW")
            time_s(0.4)
            
            break

        else:
            escrever("Opção inválida! tente novamente.", "RED")
            time_s(0.5)

# Anderson_Tsunami.11Xx