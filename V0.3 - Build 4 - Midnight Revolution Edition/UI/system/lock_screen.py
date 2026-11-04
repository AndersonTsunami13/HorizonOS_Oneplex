# lock_screen.py
# HorizonOS Oneplex - Horizon Security / IDLE LOCK

import time

from Engine.MDL_escrever import mdl_escrever as escrever
from Engine.MDL_limpar import mdl_limpar as limpar
from Engine.MDL_janela_terminal import mdl_janela_terminal as janela_terminal
from Engine.MDL_cursor_posicionar import mdl_cursor_posicionar as cursor_posicionar
from Engine.MDL_cursor import mdl_cursor as cursor
from Engine.MDL_perguntar import mdl_perguntar as perguntar
from Engine.MDL_time_s import mdl_time_s as time_s
from Engine.Sys_sair import sys_sair as sair

from UI.system.Error_screen import error_screen

from Information.devmode import limite_tentativas, limite_atigido
from Information.dados import senha_correta
from Security.securitymodule_verification import verificar_senha


# Mantém as tentativas entre chamadas de lock_screen_2().
tentativas = 0
limite_lock = 0

def lock_screen():
    """Desenha a tela principal de bloqueio."""

    limpar()
    cursor(False)

    janela_terminal(1, 1, 40, 18, "Locked", anim=True)

    cursor_posicionar(12, 5)
    escrever("TERMINAL BLOQUEADO", "RED", "destaque", "WHITE")

    cursor_posicionar(8, 7)
    escrever("Sua sessão está em espera.", "BLUE", "destaqueS", "WHITE")

    janela_terminal(11, 2, 38, 6, anim=True)

    cursor_posicionar(11, 13)
    escrever("[ Sistema protegido ]", "GREEN")

    cursor_posicionar(5, 14)
    escrever("Pressione ENTER para desbloquear", "WHITE")

    cursor_posicionar(3, 17)
    escrever("Horizon Security - IDLE LOCK", "WHITE", "apagado")

    cursor(False)

    input()
    cursor(True)
    lock_screen_2()


def lock_screen_2():
    global tentativas, limite_lock

    while True:

        # Redesenha a janela interna e substitui as mensagens anteriores.
        janela_terminal(11, 2, 38, 6, anim=True)
        cursor_posicionar(4, 13)

        senha = perguntar("Senha: ")

        if verificar_senha(senha, senha_correta):
            cursor_posicionar(4, 14)
            escrever(f"Acesso concedido!", "GREEN")

            time.sleep(1)
            cursor_posicionar(1, 21)
            break

        else: 
            tentativas += 1

            cursor_posicionar(3, 14)
            escrever(
                f"Senha incorreta! Tentativas: {tentativas}",
                "RED"
            )

            if tentativas >= limite_tentativas:
                janela_terminal(11, 2, 38, 6, anim=True)

                cursor_posicionar(4, 13)
                escrever("Limite de tentativas atingido!", "RED")

                cursor_posicionar(4, 14)
                escrever("Sessão mantida bloqueada por 1min.", "RED")
                time_s(1)

                seg = 59

                while True:
                    cursor_posicionar(3, 14)
                    escrever(f"Sessão mantida bloqueada por {seg}seg. ", "RED", performance=True)

                    if seg == 0:
                        break
                    else:
                        seg -= 1

                    time_s(1)

                tentativas = 0
                limite_lock += 1

                if limite_lock >= limite_atigido:
                    janela_terminal(11, 2, 38, 6, anim=True)

                    cursor_posicionar(3, 15)
                    escrever("Sessão bloqueada.", "RED")
                    error_screen(1000, 29, 12)
                    sair()



# Anderson_Tsunami.M3_E36
# Revision 31/10/2026

