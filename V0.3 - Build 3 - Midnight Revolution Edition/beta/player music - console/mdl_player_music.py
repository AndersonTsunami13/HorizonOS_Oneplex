# mdl_player_music.py

import pygame

# ---------------------------------------------------------
# Funções de Controle da Música
# ---------------------------------------------------------

pausado = False

def mpv_on():
    """Liga o player de música."""
    print("🔊 Player de música ligado.")
    pygame.mixer.init()

def mpv_play_music(caminho):
    """Inicia a reprodução de um arquivo."""
    print(f"🎵 Tocando: {caminho}")
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

def mpv_pause_music():
    """Pausa a música atual."""
    print("⏸️ Música pausada.")

    global pausado
    pausado = True

    pygame.mixer.music.pause()

def mpv_resume_music():
    """Despausa / Continua a reprodução."""
    print("▶️ Continuando a música...")

    global pausado
    pausado = False

    pygame.mixer.music.unpause()

def mpv_toggle_pause():
    """Inverte o estado: se tá tocando pausa, se tá pausado toca."""
    global pausado

    if pausado:
        pygame.mixer.music.unpause()
        pausado = False
        estado = "tocando"
    else:
        pygame.mixer.music.pause()
        pausado = True
        estado = "pausada"

    print(f"🔄 Estado alterado: {estado}")

def mpv_set_volume(volume_percent):
    """Ajusta o volume de 0 a 100."""
    volume = max(0, min(100, volume_percent))
    pygame.mixer.music.set_volume(volume / 100)
    print(f"🔊 Volume ajustado para: {volume}%")

def mpv_stop_music():
    """Para a reprodução completamente."""
    print("⏹️ Parando a reprodução.")
    pygame.mixer.music.stop()

def mpv_off():
    """Desliga o player de música."""
    print("🛑 Desligando o player de música.")
    pygame.mixer.quit()

# Anderson_Tsunami.M3_E36