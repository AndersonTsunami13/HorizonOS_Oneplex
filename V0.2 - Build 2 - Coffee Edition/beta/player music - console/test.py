import pygame
import time

# Inicializa o player
pygame.mixer.init()

# ---------------------------------------------------------
# Funções de Controle da Música
# ---------------------------------------------------------

def mpv_play_music(caminho):
    """Inicia a reprodução de um arquivo."""
    print(f"🎵 Tocando: {caminho}")
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

def mpv_pause_music():
    """Pausa a música atual."""
    print("⏸️ Música pausada.")
    pygame.mixer.music.pause()

def mpv_resume_music():
    """Despausa / Continua a reprodução."""
    print("▶️ Continuando a música...")
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

# ---------------------------------------------------------
# Execução do Script
# ---------------------------------------------------------

pausado = False

caminho_da_musica = 'Tuesday (Slowed Reverb).mp3'

# 1. Toca a música
mpv_play_music(caminho_da_musica)

time.sleep(5)

# 2. Ajusta o volume para 50%
mpv_set_volume(50)

# 3. Pausa
mpv_pause_music()
pausado = True

time.sleep(3)

# 4. Continua
mpv_resume_music()
pausado = False

time.sleep(120)

# 5. Pausa usando toggle
#mpv_toggle_pause()

time.sleep(1)

# 6. Para
#mpv_stop_music()

#pygame.mixer.quit()