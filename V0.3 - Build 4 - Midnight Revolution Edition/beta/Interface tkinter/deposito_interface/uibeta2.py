import tkinter as tk

# =============================
# APPS (MODULAR)
# =============================
def app_terminal(frame):
    tk.Label(frame, text="Terminal Horizon", fg="lime", bg="black").pack(expand=True)

def app_meu_pc(frame):
    tk.Label(frame, text="Explorador de Arquivos", fg="white", bg="#2b2b2b").pack(expand=True)

def app_navegador(frame):
    tk.Label(frame, text="Navegador Web", fg="white", bg="#2b2b2b").pack(expand=True)

APPS = {
    "Terminal": app_terminal,
    "Meu PC": app_meu_pc,
    "Navegador": app_navegador
}


# =============================
# WINDOW MANAGER
# =============================
class WindowManager:
    def __init__(self, root):
        self.root = root
        self.janelas = []
        self.janela_ativa = None
        self.taskbar = Taskbar(root, self)

    def criar_janela(self, titulo="Janela"):
        janela = AppWindow(self.root, self, titulo)
        self.janelas.append(janela)
        self.taskbar.adicionar(janela)
        self.set_ativa(janela)
        return janela

    def set_ativa(self, janela):
        self.janela_ativa = janela
        for j in self.janelas:
            j.set_foco(j == janela)


# =============================
# JANELA
# =============================
class AppWindow:
    def __init__(self, root, manager, titulo):
        self.root = root
        self.manager = manager
        self.titulo = titulo
        self.maximizado = False
        self.minimizado = False

        self.win = tk.Toplevel(root)
        self.win.overrideredirect(True)
        self.win.geometry("400x300+200+200")
        self.win.configure(bg="#1e1e1e")

        self.win.bind("<Button-1>", self.ativar)

        # TOPBAR
        self.topbar = tk.Frame(self.win, bg="#111", height=30)
        self.topbar.pack(fill="x")

        self.label = tk.Label(self.topbar, text=titulo, fg="white", bg="#111")
        self.label.pack(side="left", padx=5)

        # BOTÕES
        self.btn_min = tk.Label(self.topbar, text="—", fg="white", bg="#111", cursor="hand2")
        self.btn_max = tk.Label(self.topbar, text="⬜", fg="white", bg="#111", cursor="hand2")
        self.btn_close = tk.Label(self.topbar, text="✕", fg="white", bg="#111", cursor="hand2")

        self.btn_close.pack(side="right", padx=5)
        self.btn_max.pack(side="right")
        self.btn_min.pack(side="right")

        self.btn_close.bind("<Button-1>", lambda e: self.fechar())
        self.btn_min.bind("<Button-1>", lambda e: self.toggle_minimizar())
        self.btn_max.bind("<Button-1>", lambda e: self.maximizar())

        # ARRASTAR
        self.topbar.bind("<Button-1>", self.iniciar_arrasto)
        self.topbar.bind("<B1-Motion>", self.arrastar)

        # CONTEÚDO
        self.conteudo = tk.Frame(self.win, bg="#2b2b2b")
        self.conteudo.pack(fill="both", expand=True)

        # carregar app
        if titulo in APPS:
            APPS[titulo](self.conteudo)
        else:
            tk.Label(self.conteudo, text=f"App: {titulo}", fg="white", bg="#2b2b2b").pack(expand=True)

    def ativar(self, event=None):
        self.win.lift()
        self.manager.set_ativa(self)

    def set_foco(self, ativo):
        cor = "#1f1f1f" if ativo else "#111"
        self.topbar.config(bg=cor)
        self.label.config(bg=cor)

    def iniciar_arrasto(self, event):
        self.x = event.x
        self.y = event.y

    def arrastar(self, event):
        if not self.maximizado:
            x = event.x_root - self.x
            y = event.y_root - self.y
            self.win.geometry(f"+{x}+{y}")

    def fechar(self):
        self.win.destroy()

    def toggle_minimizar(self):
        if self.minimizado:
            self.win.deiconify()
            self.win.lift()
            self.minimizado = False
        else:
            self.win.withdraw()
            self.minimizado = True

    def maximizar(self):
        if not self.maximizado:
            self.win.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()-40}+0+0")
            self.maximizado = True
        else:
            self.win.geometry("400x300+200+200")
            self.maximizado = False


# =============================
# TASKBAR
# =============================
class Taskbar:
    def __init__(self, root, manager):
        self.root = root
        self.manager = manager

        self.frame = tk.Frame(root, bg="#111", height=40)
        self.frame.pack(side="bottom", fill="x")

        self.btn_start = tk.Label(self.frame, text="⛰", fg="white", bg="#111", cursor="hand2")
        self.btn_start.pack(side="left", padx=10)

        self.btn_start.bind("<Button-1>", lambda e: StartMenu(root, manager))

        self.area_apps = tk.Frame(self.frame, bg="#111")
        self.area_apps.pack(side="left", padx=10)

    def adicionar(self, janela):
        btn = tk.Label(self.area_apps, text=janela.titulo, fg="white", bg="#222", cursor="hand2")
        btn.pack(side="left", padx=5)

        def toggle(e):
            janela.toggle_minimizar()

        btn.bind("<Button-1>", toggle)


# =============================
# MENU INICIAR (TILES)
# =============================
class StartMenu:
    def __init__(self, root, manager):
        self.menu = tk.Toplevel(root)
        self.menu.overrideredirect(True)
        self.menu.geometry("400x500+0+300")
        self.menu.configure(bg="#0f0f0f")

        frame = tk.Frame(self.menu, bg="#0f0f0f")
        frame.pack(padx=10, pady=10)

        def tile(nome, cor):
            btn = tk.Button(frame, text=nome, bg=cor, fg="white",
                            width=12, height=5,
                            command=lambda: manager.criar_janela(nome))
            return btn

        tile("Meu PC", "#1f6aa5").grid(row=0, column=0, padx=5, pady=5)
        tile("Terminal", "#0a7a3d").grid(row=0, column=1, padx=5, pady=5)
        tile("Navegador", "#a54c1f").grid(row=1, column=0, padx=5, pady=5)


# =============================
# MAIN
# =============================
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="#000")

wm = WindowManager(root)

wm.criar_janela("Bem-vindo")

root.mainloop()