import tkinter as tk

# ===========================
# Configurações
# ===========================

TEXTO = "Aproveite a vida enquanto pode.\n\nDesligando o sistema..."

FADE_IN_VELOCIDADE = 4
FADE_OUT_VELOCIDADE = 4

ESPERA = 2000  # tempo antes de desaparecer (ms)

# ===========================

alpha = 0
fade_out = 255

root = None
canvas = None
texto = None

def iniciar_desligamento():
    global root, canvas, texto
    
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="black")
    root.config(cursor="none")

    canvas = tk.Canvas(
        root,
        bg="black",
        highlightthickness=0
    )

    canvas.pack(fill="both", expand=True)

    largura = root.winfo_screenwidth()
    altura = root.winfo_screenheight()

    texto = canvas.create_text(
        largura // 2,
        altura // 2,
        text=TEXTO,
        fill="#000000",
        font=("Consolas", 26),
        justify="center"
    )
    
    aparecer()
    root.mainloop()

def rgb(valor):
    valor = max(0, min(255, valor))
    return f"#{valor:02x}{valor:02x}{valor:02x}"


def aparecer():
    global alpha

    canvas.itemconfig(texto, fill=rgb(alpha))

    if alpha < 255:
        alpha += FADE_IN_VELOCIDADE
        root.after(20, aparecer)
    else:
        root.after(ESPERA, desaparecer)


def desaparecer():
    global fade_out

    valor = max(fade_out, 0)

    canvas.itemconfig(texto, fill=rgb(valor))

    if valor > 0:
        fade_out -= FADE_OUT_VELOCIDADE
        root.after(20, desaparecer)
    else:
        root.destroy()

if __name__ == "__main__":
    iniciar_desligamento()