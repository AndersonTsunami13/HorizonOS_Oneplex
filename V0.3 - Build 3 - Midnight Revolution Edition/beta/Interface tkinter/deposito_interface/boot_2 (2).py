import tkinter as tk

# =====================================
# HorizonOS Boot Animation - Sistema de Cores
# =====================================
#
# 📝 COMO MUDAR AS CORES:
# Todas as cores estão no dicionário CORES abaixo. Edite os valores HEX.
# =====================================

CORES = {
    "fundo_inicio": "#1a001a",
    "fundo_meio": "#2E00FD",
    "fundo_final": "#000000",
    "texto_branco": "#ffffff",
    "texto_escuro": "#000000",
    "barra_progresso": "#2E00FD",
    "contorno": "#444444",
    "texto_status": "#aaaaaa",
}

BARRA_CONFIG = {
    "margem_esquerda_percentual": 0.05,
    "margem_direita_percentual": 0.05,
    "altura": 25,
    "posicao_y_offset": 90,
}

# ---- Estado global (tudo começa vazio; só é preenchido dentro de boot_sequence) ----
root = None
canvas = None
LARGURA = ALTURA = 0
BARRA_X1 = BARRA_Y1 = BARRA_X2 = BARRA_Y2 = 0
BARRA_LARGURA_MAX = 0

barra = None
progresso = 0
texto_horizon = None
texto_ui = None
alpha_texto = 0
fade_saida = 255
fade_ui = 0
fade_ui_saida = 255


def calcular_coordenadas_barra():
    margem_esq = int(LARGURA * BARRA_CONFIG["margem_esquerda_percentual"])
    margem_dir = int(LARGURA * BARRA_CONFIG["margem_direita_percentual"])
    x1 = margem_esq
    x2 = LARGURA - margem_dir
    y_base = ALTURA - BARRA_CONFIG["posicao_y_offset"]
    y1 = y_base - BARRA_CONFIG["altura"] // 2
    y2 = y_base + BARRA_CONFIG["altura"] // 2
    return x1, y1, x2, y2


def hex_para_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_para_hex(r, g, b):
    return f"#{int(r):02x}{int(g):02x}{int(b):02x}"


def transicao_cor(cor_inicial, cor_final, passos, callback_funcao, intervalo=10, on_complete=None):
    """
    Transição suave entre duas cores. Ao terminar, chama on_complete()
    (em vez de depender de um delay fixo externo, evitando dessincronia).
    """
    r1, g1, b1 = hex_para_rgb(cor_inicial)
    r2, g2, b2 = hex_para_rgb(cor_final)
    passo_atual = [0]

    def animar():
        if passo_atual[0] < passos:
            p = passo_atual[0] / passos
            r = r1 + (r2 - r1) * p
            g = g1 + (g2 - g1) * p
            b = b1 + (b2 - b1) * p
            callback_funcao(rgb_para_hex(r, g, b))
            passo_atual[0] += 1
            root.after(intervalo, animar)
        else:
            callback_funcao(cor_final)
            if on_complete:
                on_complete()

    animar()


def mudanca_cor_background(cor):
    canvas.configure(bg=cor)


def boot_sequence_2():
    """Transição de fundo -> ao terminar, mostra o texto HorizonOS."""
    transicao_cor(
        CORES["fundo_meio"],
        CORES["fundo_final"],
        passos=130,
        callback_funcao=mudanca_cor_background,
        intervalo=5,
        on_complete=mostrar_horizon,   # encadeado, sem delay "no chute"
    )


def mostrar_horizon():
    global texto_horizon, alpha_texto
    alpha_texto = 0
    texto_horizon = canvas.create_text(
        LARGURA // 2, ALTURA // 2,
        text="HorizonOS",
        fill=CORES["texto_escuro"],
        font=("Consolas", 42, "bold"),
    )
    fade_texto_horizon()


def fade_texto_horizon():
    global alpha_texto
    valor = min(alpha_texto, 255)
    canvas.itemconfig(texto_horizon, fill=rgb_para_hex(valor, valor, valor))
    if alpha_texto < 255:
        alpha_texto += 4
        root.after(20, fade_texto_horizon)
    else:
        root.after(1200, apagar_horizon)


def apagar_horizon():
    global fade_saida
    valor = max(fade_saida, 0)
    canvas.itemconfig(texto_horizon, fill=rgb_para_hex(valor, valor, valor))
    if fade_saida > 0:
        fade_saida -= 4
        root.after(20, apagar_horizon)
    else:
        fade_saida = 255
        mostrar_ui()


def mostrar_ui():
    global texto_ui, fade_ui
    fade_ui = 0
    texto_ui = canvas.create_text(
        LARGURA // 2, ALTURA // 2,
        text="HorizonUI Z1",
        fill=CORES["texto_escuro"],
        font=("Consolas", 38, "bold"),
    )
    animar_ui()


def animar_ui():
    global fade_ui
    valor = min(fade_ui, 255)
    canvas.itemconfig(texto_ui, fill=rgb_para_hex(valor, valor, valor))
    if fade_ui < 255:
        fade_ui += 4
        root.after(20, animar_ui)
    else:
        root.after(1200, apagar_ui)


def apagar_ui():
    global fade_ui_saida
    valor = max(fade_ui_saida, 0)
    canvas.itemconfig(texto_ui, fill=rgb_para_hex(valor, valor, valor))
    if fade_ui_saida > 0:
        fade_ui_saida -= 4
        root.after(20, apagar_ui)
    else:
        fade_ui_saida = 255
        desenhar_boot()


def desenhar_boot():
    global barra
    canvas.delete("all")

    canvas.create_text(
        LARGURA // 2, 250,
        text="HorizonOS Professional XWin One",
        fill=CORES["texto_branco"],
        font=("Consolas", 34, "bold"),
    )
    canvas.create_text(
        40, ALTURA - 120, anchor="w",
        text="Inicializando sistema...",
        fill=CORES["texto_status"],
        font=("Consolas", 12),
    )

    barra = canvas.create_rectangle(
        BARRA_X1, BARRA_Y1, BARRA_X1, BARRA_Y2,
        fill=CORES["barra_progresso"], width=0,
    )
    canvas.create_rectangle(
        BARRA_X1, BARRA_Y1, BARRA_X2, BARRA_Y2,
        outline=CORES["contorno"],
    )

    atualizar_boot()


def atualizar_boot():
    global progresso
    progresso += 1
    percentual = min(progresso, 300) / 300
    largura_atual = int(BARRA_LARGURA_MAX * percentual)
    canvas.coords(barra, BARRA_X1, BARRA_Y1, BARRA_X1 + largura_atual, BARRA_Y2)

    if progresso < 300:
        root.after(15, atualizar_boot)
    else:
        finalizar()


def finalizar():
    canvas.create_text(
        LARGURA // 2, ALTURA - 140,
        text="Sistema carregado!",
        fill=CORES["barra_progresso"],
        font=("Consolas", 12),
    )
    root.after(1500, root.destroy)


def boot_sequence():
    """
    Ponto único de entrada: cria a janela, o canvas, calcula as
    coordenadas e SÓ ENTÃO dispara a animação. Nada acontece antes
    de chamar esta função.
    """
    global root, canvas, LARGURA, ALTURA
    global BARRA_X1, BARRA_Y1, BARRA_X2, BARRA_Y2, BARRA_LARGURA_MAX

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg=CORES["fundo_inicio"])
    root.title("HorizonOS Boot")

    # ESC pra sair rápido durante os testes
    root.bind("<Escape>", lambda e: root.destroy())

    LARGURA = root.winfo_screenwidth()
    ALTURA = root.winfo_screenheight()

    canvas = tk.Canvas(root, bg=CORES["fundo_inicio"], highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    BARRA_X1, BARRA_Y1, BARRA_X2, BARRA_Y2 = calcular_coordenadas_barra()
    BARRA_LARGURA_MAX = BARRA_X2 - BARRA_X1

    boot_sequence_2()
    root.mainloop()


if __name__ == "__main__":
    boot_sequence()