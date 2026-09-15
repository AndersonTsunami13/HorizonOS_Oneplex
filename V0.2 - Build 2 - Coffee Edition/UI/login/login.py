# UI/login/login.py

import time

from Engine.UI_Engine_ConsoleX import escrever, limpar, janela_terminal, perguntar, cursor_posicionar, enter
from Engine.Sys_Engine_Modularization import sair
from UI.system.Error_screen import error_screen

from Information.devmode import limite_tentativas
from Information.dados import name_user, senha_correta
from Security.securitymodule_verification import verificar_senha

# tela de login
def login():
    global usuario

    tentativas = 0

    while True:
        limpar()
        janela_terminal(linha=4, coluna=2, largura=45, altura=8, titulo="Login", anim=True, delay=0.05)
        cursor_posicionar(10, 6)
        escrever("HorizonUI LookScreen V1")

        usuario = perguntar("Usuario: ", x=4, y=6, cor="WHITE", fundo="BLACK", tipo=str)

        if name_user == usuario:

            cursor_posicionar(12, 6)
            escrever("Usuário encontrado!", "GREEN")

            senha = perguntar("Senha: ", x=4, y=7, cor="WHITE", fundo="BLACK", tipo=str)

            if verificar_senha(senha, senha_correta):
                cursor_posicionar(12, 6)
                escrever(f"Acesso concedido! Bem-vindo, {usuario}.", "YELLOW")
                time.sleep(1)
                break
            else: 
                tentativas += 1
                cursor_posicionar(12, 6)
                escrever(f"Senha incorreta! Tentativas: {tentativas}", "RED")
                if tentativas == limite_tentativas:
                    escrever("\nSuas tentativas acabaram!", "RED")
                    escrever("Seu sistema está bloqueado!", "RED")

                    ten = 0

                    while True:
                        if ten == 3:
                            limpar()
                            janela_terminal(linha=4, coluna=2, largura=45, altura=8, titulo="Login", anim=True, delay=0.05)
                            cursor_posicionar(10, 6)
                            escrever("HorizonUI LookSceren V1")
                            error_screen(1000, 37, 5)
                            sair()
                        escrever("Triste, né?", "YELLOW")
                        enter()
                        ten += 1
        else:
            cursor_posicionar(12, 6)
            escrever("usuário não encontrado! tente novamente.")
            time.sleep(1)

"""           Exemplo de saída do programa:
┌───────────────────────────────────────────┐
│                                    Error  │
│  Usuario: Admin                           │
│  Senha: 1234                              │
│                                           │
│ HorizonUI LookSceren V1                   │
└───────────────────────────────────────────┘
"""

# Anderson_Tsunami.M3_E36