# player_music.py
# Programa de console para controlar a reprodução de música usando o módulo MDL_player_music.

from pathlib import Path

from Engine.MDL_player_music import (
    mdl_player_on,
    mdl_player_play_music,
    mdl_player_pause_music,
    mdl_player_resume_music,
    mdl_player_toggle_pause,
    mdl_player_set_volume,
    mdl_player_stop_music,
    mdl_player_off
)

nome_da_musica = ""

def procurar_musica(nome):
    pasta_music = Path(__file__).resolve().parents[2] / "Music"

    for arquivo in pasta_music.iterdir():
        if arquivo.is_file():
            if arquivo.stem.lower() == nome.lower():
                return str(arquivo)

    return None

def player_music(argumentos):
    global nome_da_musica

    if argumentos == "start":
        mdl_player_on()

    if argumentos == "file":
        nome_da_musica = input("Digite o nome do arquivo de música: ")

    if argumentos == "play":
        musica = procurar_musica(nome_da_musica)

        if musica:
            mdl_player_play_music(musica)
        else:
            print("HorizonMusic: Música não encontrada!")

    if argumentos == "volume":
        vol = input("Digite o volume (0-100): ")
        mdl_player_set_volume(vol)

    if argumentos == "pause":
        mdl_player_pause_music()

    if argumentos == "resume":
        mdl_player_resume_music()

    if argumentos == "toggle":
        mdl_player_toggle_pause()

    if argumentos == "stop":
        mdl_player_stop_music()

    if argumentos == "off":
        mdl_player_off()

# Anderson_Tsunami.M3_E36
# Revision 01/11/2026