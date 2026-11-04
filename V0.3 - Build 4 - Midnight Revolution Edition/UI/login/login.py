# UI/login/login.py

import time

from Engine.MDL_escrever import mdl_escrever as escrever
from Engine.MDL_limpar import mdl_limpar as limpar
from Engine.MDL_janela_terminal import mdl_janela_terminal as janela_terminal
from Engine.MDL_perguntar import mdl_perguntar as perguntar
from Engine.MDL_cursor_posicionar import mdl_cursor_posicionar as cursor_posicionar
from Engine.MDL_enter import mdl_enter as enter
from Engine.MDL_input_silencioso import mdl_input_silencioso as input_silencioso
from Engine.Sys_sair import sys_sair as sair

from UI.system.Error_screen import error_screen

from Information.devmode import limite_tentativas, limite_atigido, modo_dev
from Information.dados import name_user, senha_correta, show_password
from Security.securitymodule_verification import verificar_senha

# tela de login
def login():
    global usuario

    tentativas = 0

    while True:
        limpar()
        janela_terminal(linha=4, coluna=2, largura=45, altura=8, titulo="Login", anim=True, delay=0.05)
        cursor_posicionar(4, 10)
        escrever("HorizonUI LookScreen V1.1")
        if modo_dev:
            cursor_posicionar (37, 10)
            escrever("DevMode", "RED")

        usuario = perguntar("Usuario: ", x=4, y=6, cor="WHITE", fundo="BLACK", tipo=str)

        if name_user == usuario:

            cursor_posicionar(6, 12)
            escrever("Usuário encontrado!", "GREEN")

            if show_password:
                senha = perguntar("Senha: ", x=4, y=7, cor="WHITE", fundo="BLACK", tipo=str)

            else:
                cursor_posicionar(4, 7)
                senha = input_silencioso("Senha: ")

            if verificar_senha(senha, senha_correta):
                cursor_posicionar(6, 12)
                escrever(f"Acesso concedido! Bem-vindo, {usuario}.", "YELLOW")
                time.sleep(1)
                break
            else: 
                tentativas += 1
                cursor_posicionar(6, 12)
                escrever(f"Senha incorreta! Tentativas: {tentativas}", "RED")
                if tentativas == limite_tentativas:
                    escrever("\nSuas tentativas acabaram!", "RED")
                    escrever("Seu sistema está bloqueado!", "RED")

                    ten = 0

                    while True:
                        if ten == limite_atigido:
                            limpar()
                            janela_terminal(linha=4, coluna=2, largura=45, altura=8, titulo="Locked", anim=True, delay=0.05)
                            cursor_posicionar(6, 10)
                            escrever("HorizonUI LookSceren V1.1")
                            error_screen(1000, 37, 10)
                            sair()
                        escrever("Triste, né?", "YELLOW")
                        enter()
                        ten += 1
        else:
            cursor_posicionar(6, 12)
            escrever("usuário não encontrado! tente novamente.")
            time.sleep(1)

"""           Exemplo de saída do programa:
┌─Login─────────────────────────────────────┐
│                                    Error  │
│  Usuario: Admin                           │
│  Senha: 1234                              │
│                                           │
│ HorizonUI LookSceren V1           DevMode │
└───────────────────────────────────────────┘
"""

# Anderson_Tsunami.M3_E36
# Revision 