# MDL_player_music.py
# Módulo simples de reprodução de música para o easter egg do HorizonOS Oneplex.

try:
    import pygame
except ImportError:
    from .Sys_sair import sys_sair as sair
    from .MDL_time_s import mdl_time_s as time_s
    
    print("HorizonMusic: Módulo 'pygame' não encontrado. Por favor, instale-o para usar o player de música.")
    time_s(3)
    sair()

pausado = False
inicializado = False

# Inicializa o mixer de áudio.
def mdl_player_on():
    global inicializado

    if not inicializado:
        pygame.mixer.init()
        inicializado = True

    print("[ Log ] Player de música ligado.")

# Reproduz um arquivo de música.
def mdl_player_play_music(caminho):
    mdl_player_on()

    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

    print(f"[ Log ] Tocando: {caminho}")

# Pausa a música atual.
def mdl_player_pause_music():
    global pausado

    if inicializado:
        pygame.mixer.music.pause()
        pausado = True

    print("[ Log ] Música pausada.")

# Retoma a música pausada.
def mdl_player_resume_music():
    global pausado

    if inicializado:
        pygame.mixer.music.unpause()
        pausado = False

    print("[ Log ] Música retomada.")

# Alterna entre pausa e reprodução.
def mdl_player_toggle_pause():
    global pausado

    if not inicializado:
        return

    if pausado:
        pygame.mixer.music.unpause()
        pausado = False
        estado = "tocando"
    else:
        pygame.mixer.music.pause()
        pausado = True
        estado = "pausada"

    print(f"[ Log ] Estado alterado: {estado}")

# Ajusta o volume de reprodução.
def mdl_player_set_volume(volume_percent):
    volume = max(0, min(100, int(volume_percent)))

    if inicializado:
        pygame.mixer.music.set_volume(volume / 100)

    print(f"[ Log ] Volume ajustado para: {volume}%")

# Para a reprodução de música.
def mdl_player_stop_music():
    if inicializado:
        pygame.mixer.music.stop()

    print("[ Log ] Música parada.")

# Encerra o mixer de áudio.
def mdl_player_off():
    global inicializado, pausado

    if inicializado:
        pygame.mixer.quit()
        inicializado = False
        pausado = False

    print("[ Log ] Player de música desligado.")

# Anderson_Tsunami.M3_E36
# Revision 01/11/2026