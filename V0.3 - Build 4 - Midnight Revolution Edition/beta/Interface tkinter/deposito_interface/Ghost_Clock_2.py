import tkinter as tk
from datetime import datetime
import random

frases = {
    1: "No frio da noite, será que você está sozinho?",
    2: "O tempo passa. Você percebe?",
    3: "Nem toda presença faz barulho.",
    4: "Você confia no silêncio?",
    5: "Enquanto você observa, algo observa você."
}

ultima_troca = None
frase_atual = random.choice(list(frases.values()))
indice_letra = 0
frase_digitando = ""
evento_ativo = False

# -----------------------
# CRT
# -----------------------

crt_ativo = False
scan_y = 0

def iniciar_crt():
    global crt_ativo, scan_y
    crt_ativo = True
    scan_y = 0
    canvas.lift()
    animar_crt()
    janela.after(3000, parar_crt)

def animar_crt():
    global scan_y

    if not crt_ativo:
        return

    canvas.delete("scan")

    canvas.create_line(
        0, scan_y,
        500, scan_y,
        fill="#888888",
        width=2,
        tags="scan"
    )

    scan_y += 0.1

    if scan_y > janela.winfo_height():
        scan_y = 0
        janela.after(2000, animar_crt)  # pausa de 2 segundos
        return

    janela.after(10, animar_crt)

def parar_crt():
    global crt_ativo
    crt_ativo = False
    canvas.delete("scan")
    canvas.lower()

# -----------------------
# Digitação
# -----------------------

def digitar():
    global indice_letra, frase_digitando

    if indice_letra < len(frase_atual):
        frase_digitando += frase_atual[indice_letra]
        label_frase.config(text=frase_digitando)
        indice_letra += 1
        janela.after(40, digitar)

# -----------------------
# Evento raro
# -----------------------

def evento_assustador():
    global evento_ativo

    evento_ativo = True

    label_relogio.config(text="")
    label_data.config(text="")
    label_frase.config(text="")

    janela.after(1000, mostrar_alerta)

def mostrar_alerta():

    label_alerta.config(text="You are being watched...")
    label_sub.config(text="SYSTEM WATCHING YOU")

    if random.randint(1,10) == 1:
        iniciar_crt()

    janela.after(10000, restaurar)

def restaurar():
    global evento_ativo

    label_alerta.config(text="")
    label_sub.config(text="")
    evento_ativo = False

# -----------------------
# Atualização
# -----------------------

def atualizar():
    global ultima_troca, frase_atual, indice_letra, frase_digitando

    if evento_ativo:
        janela.after(500, atualizar)
        return

    agora = datetime.now()

    if agora.second % 2 == 0:
        hora = agora.strftime("%H:%M:%S")
    else:
        hora = agora.strftime("%H %M %S")

    label_relogio.config(text=hora)
    label_data.config(text=agora.strftime("%d/%m/%Y"))

    if random.randint(1, 5000) == 1:
        janela.title("SYSTEM WATCHING YOU")
    else:
        janela.title("Ghost Clock")

    if random.randint(1, 10000) == 1:
        evento_assustador()

    minuto = agora.strftime("%M")
    if minuto != ultima_troca:
        frase_atual = random.choice(list(frases.values()))
        frase_digitando = ""
        indice_letra = 0
        label_frase.config(text="")
        digitar()
        ultima_troca = minuto

    janela.after(500, atualizar)

# -----------------------
# Interface
# -----------------------

janela = tk.Tk()
janela.title("Ghost Clock")
janela.attributes("-fullscreen", True)
janela.config(bg="black")

# canvas CRT
canvas = tk.Canvas(janela, bg="#000000", highlightthickness=0)
canvas.place(x=0, y=0, relwidth=1, relheight=1)

# FRASE
label_frase = tk.Label(
    janela,
    text="",
    font=("Consolas", 12),
    fg="#ff0000",
    bg="black",
    anchor="w",
    justify="left"
)

label_frase.place(x=10, y=45)

# RELÓGIO
label_relogio = tk.Label(
    janela,
    font=("Consolas", 80),
    fg="#210047",
    bg="black"
)

label_relogio.pack(expand=True)

# TEXTO VERMELHO ABAIXO
label_sub = tk.Label(
    janela,
    text="",
    font=("Consolas", 10),
    fg="red",
    bg="black"
)

label_sub.pack()

# DATA
label_data = tk.Label(
    janela,
    font=("Consolas", 12),
    fg="#ffffff",
    bg="black"
)

label_data.place(x=10, y=20)

# ALERTA CENTRAL
label_alerta = tk.Label(
    janela,
    text="",
    font=("Consolas", 22),
    fg="red",
    bg="black"
)

label_alerta.pack()

digitar()
atualizar()

janela.mainloop()