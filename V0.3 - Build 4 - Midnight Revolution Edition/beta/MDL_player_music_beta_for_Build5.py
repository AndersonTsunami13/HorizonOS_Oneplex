
# MDL_player_music.py
# Player de música para o HorizonOS Oneplex.
# Python 3.8.0

import os
import sys
import time
import threading

try:
    import pygame
except ImportError:
    from .Sys_sair import sys_sair as sair
    from .MDL_time_s import mdl_time_s as time_s

    print("HorizonMusic: módulo 'pygame' não encontrado.")
    time_s(3)
    sair()

try:
    from mutagen.mp3 import MP3
except ImportError:
    MP3 = None


pausado = False
inicializado = False
tocando = False

# Informações da música atual.
musica_atual = None
duracao_atual = 0
tempo_acumulado = 0
inicio_reproducao = None

# Controle da thread.
_thread_progresso = None
_evento_parar = None

# Sincronização de estado e terminal.
_lock = threading.RLock()
_lock_print = threading.Lock()


# Localiza a pasta Music ao lado do programa principal.
def mdl_player_music_folder():
    pasta_principal = os.path.dirname(
        os.path.abspath(sys.argv[0])
    )

    return os.path.join(pasta_principal, "Music")


# Lista todos os arquivos MP3.
def mdl_player_list_music(pasta=None):
    if pasta is None:
        pasta = mdl_player_music_folder()

    if not os.path.isdir(pasta):
        return []

    musicas = [
        arquivo
        for arquivo in os.listdir(pasta)
        if arquivo.lower().endswith(".mp3")
        and os.path.isfile(os.path.join(pasta, arquivo))
    ]

    return sorted(musicas, key=str.lower)


# Formata o tempo em MM:SS ou HH:MM:SS.
def _formatar_tempo(segundos):
    segundos = max(0, int(segundos))

    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60

    if horas:
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    return f"{minutos:02d}:{segundos:02d}"


# Escreve mensagens sem deixar o progresso na mesma linha.
def _log(mensagem):
    global _linha_progresso

    with _lock_print:
        if _linha_progresso:
            print()
            _linha_progresso = False

        print(mensagem)


_linha_progresso = False


# Obtém a duração do MP3.
def _obter_duracao(caminho):
    if MP3 is None:
        _log("[ Aviso ] Instale mutagen para exibir a duração das músicas.")
        return 0

    try:
        return MP3(caminho).info.length
    except Exception:
        return 0


# Calcula o tempo decorrido.
def _obter_tempo_atual():
    with _lock:
        tempo = tempo_acumulado

        if inicio_reproducao is not None:
            tempo += time.monotonic() - inicio_reproducao

        return min(tempo, duracao_atual) if duracao_atual else tempo


# Thread responsável pela exibição do progresso.
def _atualizar_progresso(evento):
    global tocando, _linha_progresso

    while not evento.is_set():
        with _lock:
            nome = musica_atual or "Desconhecida"
            duracao = duracao_atual
            tempo = _obter_tempo_atual()
            esta_pausado = pausado
            esta_tocando = tocando

        if not esta_tocando:
            break

        tempo_formatado = _formatar_tempo(tempo)

        if duracao:
            duracao_formatada = _formatar_tempo(duracao)
        else:
            duracao_formatada = "--:--"

        estado = " [PAUSADO]" if esta_pausado else ""

        mensagem = (
            f"{nome}  "
            f"{tempo_formatado}/{duracao_formatada}"
            f"{estado}"
        )

        with _lock_print:
            print("\r" + mensagem.ljust(100), end="", flush=True)
            _linha_progresso = True

        # Verifica se a reprodução terminou naturalmente.
        if not esta_pausado and not pygame.mixer.music.get_busy():
            if tempo > 0.5:
                with _lock:
                    tocando = False

                break

        evento.wait(0.5)

    with _lock_print:
        if _linha_progresso:
            print()
            _linha_progresso = False


# Encerra a thread anterior.
def _parar_atualizador():
    global _thread_progresso, _evento_parar

    evento = _evento_parar
    thread = _thread_progresso

    if evento is not None:
        evento.set()

    if thread is not None and thread is not threading.current_thread():
        thread.join(timeout=2)

    _thread_progresso = None
    _evento_parar = None


# Inicia a thread de progresso.
def _iniciar_atualizador():
    global _thread_progresso, _evento_parar

    _parar_atualizador()

    _evento_parar = threading.Event()

    _thread_progresso = threading.Thread(
        target=_atualizar_progresso,
        args=(_evento_parar,),
        daemon=True
    )

    _thread_progresso.start()


# Inicializa o mixer de áudio.
def mdl_player_on():
    global inicializado

    if not inicializado:
        pygame.mixer.init()
        inicializado = True

    _log("[ Log ] Player de música ligado.")


# Reproduz uma música.
def mdl_player_play_music(caminho):
    global pausado, tocando
    global musica_atual, duracao_atual
    global tempo_acumulado, inicio_reproducao

    mdl_player_on()

    # Permite informar apenas o nome do arquivo.
    if not os.path.isfile(caminho):
        caminho = os.path.join(
            mdl_player_music_folder(),
            caminho
        )

    if not os.path.isfile(caminho):
        _log(f"[ Erro ] Música não encontrada: {caminho}")
        return

    _parar_atualizador()

    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

    with _lock:
        musica_atual = os.path.basename(caminho)
        duracao_atual = _obter_duracao(caminho)
        tempo_acumulado = 0
        inicio_reproducao = time.monotonic()
        pausado = False
        tocando = True

    _log(f"[ Log ] Tocando: {musica_atual}")

    _iniciar_atualizador()


# Pausa a música atual.
def mdl_player_pause_music():
    global pausado, tempo_acumulado, inicio_reproducao

    if inicializado and tocando and not pausado:
        pygame.mixer.music.pause()

        with _lock:
            if inicio_reproducao is not None:
                tempo_acumulado += (
                    time.monotonic() - inicio_reproducao
                )

            inicio_reproducao = None
            pausado = True

    _log("[ Log ] Música pausada.")


# Retoma a música pausada.
def mdl_player_resume_music():
    global pausado, inicio_reproducao

    if inicializado and pausado:
        pygame.mixer.music.unpause()

        with _lock:
            inicio_reproducao = time.monotonic()
            pausado = False

        _log("[ Log ] Música retomada.")


# Alterna entre pausa e reprodução.
def mdl_player_toggle_pause():
    if pausado:
        mdl_player_resume_music()
    else:
        mdl_player_pause_music()


# Ajusta o volume.
def mdl_player_set_volume(volume_percent):
    volume = max(0, min(100, int(volume_percent)))

    if inicializado:
        pygame.mixer.music.set_volume(volume / 100)

    _log(f"[ Log ] Volume ajustado para: {volume}%")


# Para a reprodução.
def mdl_player_stop_music():
    global pausado, tocando
    global tempo_acumulado, inicio_reproducao

    _parar_atualizador()

    if inicializado:
        pygame.mixer.music.stop()

    with _lock:
        pausado = False
        tocando = False
        tempo_acumulado = 0
        inicio_reproducao = None

    _log("[ Log ] Música parada.")


# Encerra o mixer.
def mdl_player_off():
    global inicializado, pausado, tocando

    _parar_atualizador()

    if inicializado:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        inicializado = False
        pausado = False
        tocando = False

    _log("[ Log ] Player de música desligado.")


# Anderson_Tsunami.M3_E36
# Revision 04/11/2026
