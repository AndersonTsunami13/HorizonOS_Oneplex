import time

from mdl_player_music import (
    mpv_on,
    mpv_play_music,
    mpv_pause_music,
    mpv_resume_music,
    mpv_toggle_pause,
    mpv_set_volume,
    mpv_stop_music,
    mpv_off
)

mpv_on()

caminho_da_musica = "base para mega funk.mp3"

# 1. Toca a música
mpv_play_music(caminho_da_musica)

time.sleep(5)

# 2. Ajusta o volume para 50%
mpv_set_volume(50)

# 3. Pausa
mpv_pause_music()

time.sleep(3)

# 4. Continua
mpv_resume_music()

time.sleep(120)

# 5. Pausa usando toggle
mpv_toggle_pause()

time.sleep(1)

# 6. Para
mpv_stop_music()

# 7. Desliga
mpv_off()