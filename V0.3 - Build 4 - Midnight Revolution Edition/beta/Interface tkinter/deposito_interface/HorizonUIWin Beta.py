import os
import random
import time
import tkinter as tk

# ==========================
# CONFIGURAÇÕES
# ==========================

LARGURA_JANELA = 1350
ALTURA_JANELA = 940
ALTURA_BARRA = 42

PAPEL_DE_PAREDE = "wallpaper.png"  # opcional, PNG/GIF
STATUS_PADRAO = "Sistema pronto."

COR_FUNDO = "#202020"
COR_BARRA = "#101010"
COR_TEXTO = "#FFFFFF"
COR_ICONE = "#2A2A2A"
COR_ICONE_HOVER = "#3A3A3A"
COR_MENU = "#1B1B1B"
COR_MENU_BORDA = "#3A3A3A"
COR_DESTAQUE = "#2D2D2D"
COR_BOTAO = "#252525"
COR_BOTAO_HOVER = "#343434"

FONT_PADRAO = ("Arial", 11)
FONT_TEXTO = ("Arial", 10)
FONT_RELOGIO = ("Arial", 10, "bold")

GHOST_MESSAGES = [
    "O Ghost está de olho, meu nobre.",
    "Nem toda quietude é paz.",
    "Sistema estável.",
    "Tudo sob controle.",
    "O silêncio tá estranho hoje.",
    "Nenhum erro detectado.",
]

# ==========================
# VARIÁVEIS GLOBAIS
# ==========================

janela = None
barra = None
relogio = None
status_label = None
botao_iniciar = None
menu_frame = None
fundo_widget = None

menu_visivel = False
status_estado = "idle"      # idle | temp | ghost
status_restore_job = None


# ==========================
# STATUS BAR
# ==========================

def restaurar_status_padrao():
    global status_estado, status_restore_job
    status_estado = "idle"
    status_restore_job = None
    status_label.config(text=STATUS_PADRAO)


def status(texto, tempo=3000):
    global status_estado, status_restore_job

    status_estado = "temp"

    if status_restore_job is not None:
        try:
            janela.after_cancel(status_restore_job)
        except Exception:
            pass
        status_restore_job = None

    status_label.config(text=texto)
    status_restore_job = janela.after(tempo, restaurar_status_padrao)


def atualizar_ghost():
    global status_estado, status_restore_job

    if status_estado == "idle" and not menu_visivel:
        status_estado = "ghost"
        status_label.config(text=random.choice(GHOST_MESSAGES))

        if status_restore_job is not None:
            try:
                janela.after_cancel(status_restore_job)
            except Exception:
                pass

        status_restore_job = janela.after(3500, restaurar_status_padrao)

    janela.after(15000, atualizar_ghost)


# ==========================
# RELÓGIO
# ==========================

def atualizar_relogio():
    relogio.config(text=time.strftime("%H:%M:%S"))
    janela.after(1000, atualizar_relogio)


# ==========================
# PROGRAMAS
# ==========================

def abrir_meu_pc():
    print("Meu PC")
    status("Meu PC aberto.")


def abrir_terminal():
    print("Terminal")
    status("Terminal iniciado.")


def abrir_navegador():
    print("Navegador")
    status("Navegador iniciado.")


def abrir_lixeira():
    print("Lixeira")
    status("Lixeira aberta.")


def fechar_sistema():
    janela.destroy()


# ==========================
# ÍCONES
# ==========================

def criar_icone(nome, x, y, comando):
    bloco = tk.Frame(
        janela,
        bg=COR_ICONE,
        width=96,
        height=70,
        highlightthickness=1,
        highlightbackground=COR_MENU_BORDA
    )
    bloco.place(x=x, y=y)
    bloco.pack_propagate(False)

    texto = tk.Label(
        bloco,
        text=nome,
        bg=COR_ICONE,
        fg=COR_TEXTO,
        font=FONT_PADRAO,
        cursor="hand2"
    )
    texto.pack(expand=True, fill="both")

    def entrar(_event):
        bloco.config(bg=COR_ICONE_HOVER)
        texto.config(bg=COR_ICONE_HOVER)

    def sair(_event):
        bloco.config(bg=COR_ICONE)
        texto.config(bg=COR_ICONE)

    def clicar(_event):
        comando()

    for widget in (bloco, texto):
        widget.bind("<Enter>", entrar)
        widget.bind("<Leave>", sair)
        widget.bind("<Button-1>", clicar)


# ==========================
# PAPEL DE PAREDE
# ==========================

def criar_papel_de_parede():
    global fundo_widget

    if os.path.exists(PAPEL_DE_PAREDE):
        try:
            imagem = tk.PhotoImage(file=PAPEL_DE_PAREDE)
            fundo_widget = tk.Label(janela, image=imagem, bg=COR_FUNDO)
            fundo_widget.image = imagem
            fundo_widget.place(x=0, y=0, relwidth=1, relheight=1)
            fundo_widget.lower()
            return
        except Exception:
            pass

    janela.configure(bg=COR_FUNDO)


# ==========================
# MENU INICIAR
# ==========================

def executar_acao_menu(acao):
    esconder_menu_iniciar()
    acao()


def criar_menu_iniciar():
    global menu_frame

    menu_frame = tk.Frame(
        janela,
        bg=COR_MENU,
        width=290,
        height=360,
        highlightthickness=1,
        highlightbackground=COR_MENU_BORDA
    )
    menu_frame.pack_propagate(False)

    titulo = tk.Label(
        menu_frame,
        text="Horizon",
        bg=COR_MENU,
        fg=COR_TEXTO,
        font=("Arial", 12, "bold"),
        anchor="w"
    )
    titulo.pack(fill="x", padx=12, pady=(10, 6))

    separador = tk.Frame(menu_frame, bg=COR_MENU_BORDA, height=1)
    separador.pack(fill="x", padx=12, pady=(0, 10))
    
    area_rolavel = tk.Frame(
        menu_frame,
        bg=COR_MENU
    )

    area_rolavel.pack(
        fill="both",
        expand=True
    )

    # ==========================
    # ÁREA ROLÁVEL
    # ==========================
    menu_canvas = tk.Canvas(
        area_rolavel,
        bg=COR_MENU,
        highlightthickness=0,
        bd=0
    )

    scrollbar = tk.Scrollbar(
        area_rolavel,
        orient="vertical",
        command=menu_canvas.yview,
        bg="#303030",
        troughcolor="#1B1B1B",
        activebackground="#505050",
        width=10
    )

    menu_interno = tk.Frame(
        menu_canvas,
        bg=COR_MENU
    )

    menu_canvas.create_window(
        (0, 0),
        window=menu_interno,
        anchor="nw"
    )

    menu_canvas.configure(
        yscrollcommand=scrollbar.set
    )

    def ajustar_scrollregion(_event):
        menu_canvas.configure(
            scrollregion=menu_canvas.bbox("all")
        )

    menu_interno.bind("<Configure>", ajustar_scrollregion)

    menu_canvas.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 2)
    )

    scrollbar.pack(
        side="right",
        fill="y",
        padx=(0, 2)
    )

    botoes = [
        ("Meu PC", abrir_meu_pc),
        ("Terminal", abrir_terminal),
        ("Navegador", abrir_navegador),
        ("Lixeira", abrir_lixeira),

        ("Programa 1", abrir_meu_pc),
        ("Programa 2", abrir_meu_pc),
        ("Programa 3", abrir_meu_pc),
        ("Programa 4", abrir_meu_pc),
        ("Programa 5", abrir_meu_pc),
        ("Programa 6", abrir_meu_pc),
        ("Programa 7", abrir_meu_pc),
        ("Programa 8", abrir_meu_pc),

        ("Desligar", fechar_sistema),
    ]

    for texto, acao in botoes:
        botao = tk.Button(
            menu_interno,
            text=texto,
            command=lambda a=acao: executar_acao_menu(a),
            bg=COR_BOTAO,
            fg=COR_TEXTO,
            activebackground=COR_BOTAO_HOVER,
            activeforeground=COR_TEXTO,
            relief="flat",
            bd=0,
            font=FONT_TEXTO,
            anchor="w",
            padx=12
        )
        botao.pack(fill="x", padx=12, pady=4)

    fechar = tk.Button(
        menu_interno,
        text="Fechar menu",
        command=esconder_menu_iniciar,
        bg=COR_DESTAQUE,
        fg=COR_TEXTO,
        activebackground=COR_BOTAO_HOVER,
        activeforeground=COR_TEXTO,
        relief="flat",
        bd=0,
        font=FONT_TEXTO
    )
    fechar.pack(fill="x", padx=12, pady=(10, 12))


def mostrar_menu_iniciar():
    global menu_visivel

    if menu_visivel:
        esconder_menu_iniciar()
        return

    janela.update_idletasks()

    largura_menu = 240
    altura_menu = 260

    x_botao = botao_iniciar.winfo_rootx() - janela.winfo_rootx()
    y_botao = botao_iniciar.winfo_rooty() - janela.winfo_rooty()

    x = max(8, x_botao)
    y = y_botao - altura_menu - 8

    if x + largura_menu > janela.winfo_width() - 8:
        x = janela.winfo_width() - largura_menu - 8

    if y < 8:
        y = 8

    menu_frame.place(x=x, y=y, width=largura_menu, height=altura_menu)
    menu_frame.lift()
    menu_visivel = True


def esconder_menu_iniciar():
    global menu_visivel
    menu_frame.place_forget()
    menu_visivel = False


def alternar_menu_iniciar():
    if menu_visivel:
        esconder_menu_iniciar()
    else:
        mostrar_menu_iniciar()


def eh_descendente(widget, possivel_ancestro):
    while widget is not None:
        if widget == possivel_ancestro:
            return True
        widget = widget.master
    return False


def clicou_fora_do_menu(event):
    if not menu_visivel:
        return

    widget = event.widget

    if eh_descendente(widget, menu_frame) or eh_descendente(widget, botao_iniciar):
        return

    esconder_menu_iniciar()


# ==========================
# JANELA PRINCIPAL
# ==========================

janela = tk.Tk()
janela.title("HorizonUI 3")
janela.geometry(f"{LARGURA_JANELA}x{ALTURA_JANELA}")
janela.configure(bg=COR_FUNDO)
janela.minsize(900, 600)
janela.protocol("WM_DELETE_WINDOW", fechar_sistema)

criar_papel_de_parede()

# ==========================
# DESKTOP
# ==========================

criar_icone("Meu PC", 30, 30, abrir_meu_pc)
criar_icone("Terminal", 30, 120, abrir_terminal)
criar_icone("Navegador", 30, 210, abrir_navegador)
criar_icone("Lixeira", 30, 300, abrir_lixeira)
# ==========================
# BARRA DE TAREFAS
# ==========================

barra = tk.Frame(
    janela,
    bg=COR_BARRA,
    height=ALTURA_BARRA
)

barra.pack(
    side="bottom",
    fill="x"
)

barra.pack_propagate(False)

# --------------------------
# BOTÃO INICIAR
# --------------------------

botao_iniciar = tk.Button(
    barra,
    text="Horizon",
    command=alternar_menu_iniciar,
    bg=COR_BOTAO,
    fg=COR_TEXTO,
    activebackground=COR_BOTAO_HOVER,
    activeforeground=COR_TEXTO,
    relief="flat",
    bd=0,
    cursor="hand2",
    font=FONT_TEXTO
)

botao_iniciar.pack(
    side="left",
    padx=8,
    pady=5
)

# --------------------------
# STATUS BAR
# --------------------------

status_label = tk.Label(
    barra,
    text=STATUS_PADRAO,
    bg=COR_BARRA,
    fg=COR_TEXTO,
    anchor="w",
    font=FONT_TEXTO
)

status_label.pack(
    side="left",
    padx=15,
    fill="x",
    expand=True
)

# --------------------------
# RELÓGIO
# --------------------------

relogio = tk.Label(
    barra,
    text="",
    bg=COR_BARRA,
    fg=COR_TEXTO,
    font=FONT_RELOGIO
)

relogio.pack(
    side="right",
    padx=10
)
# ==========================
# MENU + EVENTOS
# ==========================

criar_menu_iniciar()

janela.bind_all("<Button-1>", clicou_fora_do_menu, add="+")

# ==========================
# INICIAR ROTINAS
# ==========================

atualizar_relogio()
atualizar_ghost()
status("Horizon iniciado com sucesso.", 2500)

janela.mainloop()