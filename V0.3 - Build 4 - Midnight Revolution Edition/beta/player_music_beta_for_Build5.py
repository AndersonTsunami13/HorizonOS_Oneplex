
# player_music.py
# Controlador de reprodução musical do HorizonOS Oneplex.
# Python 3.8.0

import sys
import importlib
from pathlib import Path


# ==========================================================
# LOCALIZAÇÃO DA ENGINE
# ==========================================================

def localizar_beta():
    candidatos = [
        Path.cwd() / "beta",
        Path(__file__).resolve().parent / "beta"
    ]

    # Procura a pasta beta nos diretórios superiores.
    for diretorio in Path(__file__).resolve().parents:
        candidatos.append(diretorio / "beta")

    for pasta in candidatos:
        if (pasta / "MDL_player_music_beta_for_Build5.py").is_file():
            return pasta

    raise ImportError(
        "HorizonMusic: não foi possível localizar "
        "beta/MDL_player_music_beta_for_Build5.py"
    )


PASTA_BETA = localizar_beta()

if str(PASTA_BETA) not in sys.path:
    sys.path.insert(0, str(PASTA_BETA))


engine = importlib.import_module(
    "MDL_player_music_beta_for_Build5"
)


# ==========================================================
# FUNÇÕES DA ENGINE
# ==========================================================

mdl_player_on = engine.mdl_player_on
mdl_player_play_music = engine.mdl_player_play_music
mdl_player_pause_music = engine.mdl_player_pause_music
mdl_player_resume_music = engine.mdl_player_resume_music
mdl_player_toggle_pause = engine.mdl_player_toggle_pause
mdl_player_set_volume = engine.mdl_player_set_volume
mdl_player_stop_music = engine.mdl_player_stop_music
mdl_player_off = engine.mdl_player_off

mdl_player_list_music = engine.mdl_player_list_music


# ==========================================================
# ESTADO DO PLAYER
# ==========================================================

nome_da_musica = ""


# ==========================================================
# LISTAGEM DE MÚSICAS
# ==========================================================

def listar_musicas():
    musicas = mdl_player_list_music()

    if not musicas:
        print("HorizonMusic: Nenhum arquivo MP3 encontrado na pasta Music!")
        return []

    print("\n========== HORIZON MUSIC ==========")

    for numero, musica in enumerate(musicas, 1):
        print(f"[{numero}] {Path(musica).stem}")

    print("===================================\n")

    return musicas


# ==========================================================
# SELEÇÃO DE MÚSICA
# ==========================================================

def selecionar_musica():
    global nome_da_musica

    musicas = listar_musicas()

    if not musicas:
        return

    escolha = input("Selecione o número ou nome da música: ").strip()

    if not escolha:
        return

    # Seleção pelo número.
    if escolha.isdigit():
        numero = int(escolha)

        if 1 <= numero <= len(musicas):
            nome_da_musica = musicas[numero - 1]
            print(f"[ Log ] Selecionada: {nome_da_musica}")
            return

        print("HorizonMusic: Número inválido!")
        return

    # Seleção pelo nome do arquivo.
    for musica in musicas:
        if Path(musica).stem.lower() == escolha.lower():
            nome_da_musica = musica
            print(f"[ Log ] Selecionada: {nome_da_musica}")
            return

    print("HorizonMusic: Música não encontrada!")


# ==========================================================
# CONTROLADOR PRINCIPAL
# ==========================================================

def player_music(argumentos):
    global nome_da_musica

    if argumentos == "start":
        mdl_player_on()

    elif argumentos == "list":
        listar_musicas()

    elif argumentos == "file":
        selecionar_musica()

    elif argumentos == "play":
        if not nome_da_musica:
            print("HorizonMusic: Selecione uma música primeiro!")
            return

        mdl_player_play_music(nome_da_musica)

    elif argumentos == "volume":
        vol = input("Digite o volume (0-100): ")

        try:
            mdl_player_set_volume(vol)
        except ValueError:
            print("HorizonMusic: Volume inválido!")

    elif argumentos == "pause":
        mdl_player_pause_music()

    elif argumentos == "resume":
        mdl_player_resume_music()

    elif argumentos == "toggle":
        mdl_player_toggle_pause()

    elif argumentos == "stop":
        mdl_player_stop_music()

    elif argumentos == "off":
        mdl_player_off()
        nome_da_musica = ""


# Anderson_Tsunami.M3_E36
# Revision 04/11/2026
