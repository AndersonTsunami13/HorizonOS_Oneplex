# sleep_screen.py

from datetime import datetime

from Engine.MDL_escrever import mdl_escrever as escrever
from Engine.MDL_cursor_posicionar import mdl_cursor_posicionar as cursor_posicionar
from Engine.MDL_time_s import mdl_time_s as time_s
from Engine.MDL_cursor import mdl_cursor as cursor
from Engine.MDL_limpar import mdl_limpar as limpar
from Engine.MDL_janela_terminal import mdl_janela_terminal as janela_terminal

def sleep_screen():
    # Desenhe a moldura e os elementos fixos apenas uma vez.
    try:
        cursor(False)

        limpar()

        janela_terminal(2, 3, 14, 4, "Hora")

        cursor_posicionar(18, 2)
        escrever("HorizonOS Oneplex", "GREEN")
        cursor_posicionar(18, 3)
        escrever("Modo de descanso", "CYAN")
        cursor_posicionar(18, 4)
        escrever("Pressione Ctrl+C para sair", "YELLOW")

        while True:
            agora = datetime.now().strftime("%H:%M:%S")
            cursor_posicionar(5, 4)
            escrever(f" {agora} ", "BLACK", "normal", "WHITE")

    except KeyboardInterrupt:
        cursor_posicionar(18, 5)
        cursor(True)
        escrever("Tela de descanço desativada...", "RED")
        time_s(2)
        cursor_posicionar(1, 7)

# Anderson_Tsunami.M3_E36
# Revision 31/10/2026