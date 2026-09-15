# UI/login.py

import time

from Engine.UI_Engine_ConsoleX import escrever, limpar
from Information.devmode import limite_tentativas
from Information.dados import name_user, senha_correta
from UI.anim.loading import loading 
from Security.securitymodule_verification import verificar_senha

# tela de login
def login():
    global usuario
    limpar()

    escrever("\n== LOGIN ==", "GREEN", "destaque")
    tentativas = 0

    while True:
        usuario = input("Usuario: ")
        if name_user == usuario:
            escrever("Usuário encontrado!", "GREEN")

            senha = input("Senha: ")
            if verificar_senha(senha, senha_correta):
                escrever(f"Acesso concedido! Bem-vindo, {usuario}.", "YELLOW")
                time.sleep(1)
                break
            else: 
                tentativas += 1
                escrever(f"Senha incorreta! Tentativas: {tentativas}", "RED")
                if tentativas == limite_tentativas:
                    escrever("\nSuas tentativas acabaram!", "RED")
                    escrever("Seu sistema está bloqueado!", "RED")
                    escrever("Triste, né?", "YELLOW")
                    loading(999, "")
        else:
            escrever("usuário não encontrado! tente novamente.")
            time.sleep(1)