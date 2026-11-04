# Easter_Egg_terminal.py
# Easter egg de créditos do HorizonOS Oneplex.

from pathlib import Path
import os
import sys
import time

from Information.info import developer, versao_system, build_system, name_system, name_music_credits
from Information.devmode import name_DEV

from Engine.MDL_player_music import (
    mdl_player_on, 
    mdl_player_play_music, 
    mdl_player_set_volume,
    mdl_player_stop_music, 
    mdl_player_off
)

from Engine.MDL_escrever import mdl_escrever as escrever
from Engine.MDL_limpar import mdl_limpar as limpar
from Engine.MDL_time_s import mdl_time_s as time_s
from Engine.MDL_enter import mdl_enter as enter

nome_da_musica = "Credits"
volume = 80

def procurar_musica(nome_da_musica):
    pasta_music = Path(__file__).resolve().parents[2] / "Music"

    for arquivo in pasta_music.iterdir():
        if arquivo.is_file():
            if arquivo.stem.lower() == nome_da_musica.lower():
                return str(arquivo)

    return None

def easteregg():
    limpar()

    mdl_player_on()
    musica = procurar_musica(nome_da_musica)
    mdl_player_play_music(musica)
    mdl_player_set_volume(volume)
    time_s(1)

    limpar()

    escrever(f"""
        
          +--------------------------------------------------------------+
          |                    HORIZONOS ONEPLEX                         |
          |                      C R E D I T S                           |
          +--------------------------------------------------------------+
        
          [ CRÉDITOS DO PROJETO ]
        
          Desenvolvido por : {developer}
          Projeto          : {name_system}
          Versão           : {versao_system}
          Build            : {build_system}
          Desenvolvedor    : {name_DEV}

          Obrigado por explorar este pequeno universo.
          Cada linha de código faz parte da jornada.
        
          +--------------------------------------------------------------+
          Música : {name_music_credits}
          Volume : {volume}%
        
          +--------------------------------------------------------------+
""", "RED", "destaque", velocidade=0.01)

    enter()

    mdl_player_stop_music()
    mdl_player_off()
