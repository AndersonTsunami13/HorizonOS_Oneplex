# credits_easter_egg.py
# Tela independente de créditos do HorizonOS Oneplex.
# Coloque este arquivo, mdl_player_music.py e a música na mesma pasta.

from pathlib import Path
import tkinter as tk
from tkinter import messagebox

try:
    import mdl_player_music as player
except SyntaxError as exc:
    raise SystemExit(
        "Não foi possível importar mdl_player_music.py: há um erro de sintaxe "
        "nesse arquivo. Corrija-o ou use a versão corrigida que acompanha este pacote."
    ) from exc
except ImportError as exc:
    raise SystemExit(
        "Não encontrei mdl_player_music.py na mesma pasta. "
        "Coloque os dois arquivos juntos."
    ) from exc


PASTA = Path(__file__).resolve().parent
EXTENSOES_AUDIO = {".mp3", ".ogg", ".wav", ".flac", ".mid", ".midi"}
NOME_MUSICA_PREFERIDO = "credits.mp3"


def localizar_musica():
    """Prioriza credits.mp3; caso não exista, procura áudio na pasta."""
    preferida = PASTA / NOME_MUSICA_PREFERIDO
    if preferida.is_file():
        return preferida

    arquivos = sorted(
        arquivo for arquivo in PASTA.iterdir()
        if arquivo.is_file() and arquivo.suffix.lower() in EXTENSOES_AUDIO
        and arquivo.name != Path(__file__).name
    )
    return arquivos[0] if arquivos else None


class CreditsScreen:
    def __init__(self, root):
        self.root = root
        self.musica = localizar_musica()
        self.audio_pronto = False
        self.tocando = False

        root.title("HorizonOS Oneplex — Credits")
        root.geometry("760x520")
        root.minsize(620, 450)
        root.configure(bg="#101214")
        root.protocol("WM_DELETE_WINDOW", self.fechar)

        self._montar_interface()

        if self.musica:
            self.status_var.set(f"Faixa encontrada: {self.musica.name}")
        else:
            self.status_var.set("Nenhuma música encontrada nesta pasta.")

    def _montar_interface(self):
        fundo = "#101214"
        painel = "#181c1f"
        verde = "#9bd36a"
        texto = "#e8ece8"
        secundario = "#9aa59d"

        topo = tk.Frame(self.root, bg=fundo, padx=30, pady=24)
        topo.pack(fill="x")

        tk.Label(
            topo, text="HORIZONOS", bg=fundo, fg=verde,
            font=("Consolas", 12, "bold")
        ).pack(anchor="w")

        tk.Label(
            topo, text="ONEPLEX", bg=fundo, fg=texto,
            font=("Consolas", 30, "bold")
        ).pack(anchor="w", pady=(3, 0))

        tk.Label(
            topo, text="Uma pequena homenagem a quem construiu esta experiência.",
            bg=fundo, fg=secundario, font=("Segoe UI", 10)
        ).pack(anchor="w", pady=(7, 0))

        tk.Frame(self.root, bg=verde, height=2).pack(fill="x", padx=30)

        corpo = tk.Frame(self.root, bg=painel, padx=24, pady=20)
        corpo.pack(fill="both", expand=True, padx=30, pady=22)

        tk.Label(
            corpo, text="CRÉDITOS", bg=painel, fg=verde,
            font=("Consolas", 14, "bold")
        ).pack(anchor="w")

        tk.Label(
            corpo, text="Desenvolvimento", bg=painel, fg=secundario,
            font=("Segoe UI", 9)
        ).pack(anchor="w", pady=(12, 0))

        tk.Label(
            corpo, text="Anderson_Tsunami", bg=painel, fg=texto,
            font=("Consolas", 18, "bold")
        ).pack(anchor="w", pady=(2, 8))

        tk.Label(
            corpo,
            text="HorizonOS Oneplex • Projeto independente • Obrigado por usar.",
            bg=painel, fg=secundario, font=("Segoe UI", 9),
            wraplength=620, justify="left"
        ).pack(anchor="w")

        controles = tk.Frame(corpo, bg=painel)
        controles.pack(fill="x", pady=(22, 0))

        self._botao(controles, "▶  Reproduzir", self.reproduzir).pack(side="left", padx=(0, 8))
        self._botao(controles, "⏯  Pausar / continuar", self.alternar_pausa).pack(side="left", padx=(0, 8))
        self._botao(controles, "■  Parar", self.parar).pack(side="left")

        volume_linha = tk.Frame(corpo, bg=painel)
        volume_linha.pack(fill="x", pady=(20, 0))

        tk.Label(
            volume_linha, text="VOLUME", bg=painel, fg=secundario,
            font=("Consolas", 9, "bold")
        ).pack(side="left")

        self.volume_var = tk.IntVar(value=70)
        tk.Scale(
            volume_linha, from_=0, to=100, orient="horizontal",
            variable=self.volume_var, command=self.ajustar_volume,
            bg=painel, fg=texto, troughcolor="#30383b",
            activebackground="#9bd36a", highlightthickness=0,
            bd=0, showvalue=True, length=220
        ).pack(side="right")

        self.status_var = tk.StringVar(value="Preparando player...")
        tk.Label(
            self.root, textvariable=self.status_var, bg=fundo,
            fg=secundario, font=("Consolas", 9), anchor="w",
            padx=30, pady=0
        ).pack(fill="x", pady=(0, 18))

    def _botao(self, parent, texto, comando):
        return tk.Button(
            parent, text=texto, command=comando,
            bg="#252c2f", fg="#e8ece8", activebackground="#35433a",
            activeforeground="#ffffff", relief="flat", bd=0,
            padx=12, pady=9, cursor="hand2",
            font=("Segoe UI", 9, "bold")
        )

    def reproduzir(self):
        if not self.musica:
            messagebox.showwarning(
                "Música não encontrada",
                "Coloque um arquivo .mp3, .ogg ou .wav na mesma pasta "
                "do credits_easter_egg.py."
            )
            return
        try:
            player.mpv_on()
            player.mpv_set_volume(self.volume_var.get())
            player.mpv_play_music(str(self.musica))
            self.audio_pronto = True
            self.tocando = True
            self.status_var.set(f"Reproduzindo: {self.musica.name}")
        except Exception as exc:
            messagebox.showerror(
                "Falha no player",
                f"Não foi possível reproduzir a música.\n\n{exc}\n\n"
                "Verifique se o pygame está instalado e se o arquivo de áudio é compatível."
            )
            self.status_var.set("Falha ao iniciar o áudio.")

    def alternar_pausa(self):
        if not self.audio_pronto:
            self.reproduzir()
            return
        try:
            player.mpv_toggle_pause()
            self.tocando = not self.tocando
            self.status_var.set("Música em reprodução." if self.tocando else "Música pausada.")
        except Exception as exc:
            messagebox.showerror("Falha no player", str(exc))

    def parar(self):
        try:
            player.mpv_stop_music()
            self.tocando = False
            self.status_var.set("Reprodução parada.")
        except Exception as exc:
            messagebox.showerror("Falha no player", str(exc))

    def ajustar_volume(self, valor):
        try:
            player.mpv_set_volume(int(float(valor)))
        except Exception:
            # O controle de volume não deve derrubar a interface.
            pass

    def fechar(self):
        try:
            player.mpv_stop_music()
            player.mpv_off()
        except Exception:
            pass
        self.root.destroy()


def abrir_tela():
    root = tk.Tk()
    CreditsScreen(root)
    root.mainloop()


if __name__ == "__main__":
    abrir_tela()
