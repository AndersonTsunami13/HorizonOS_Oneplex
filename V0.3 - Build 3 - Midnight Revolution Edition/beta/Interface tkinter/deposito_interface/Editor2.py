import tkinter as tk
from tkinter import filedialog

# =========================
# JANELA
# =========================

root = tk.Tk()
root.title("Horizon Editor")
root.geometry("900x600")
root.configure(bg="#1e1e1e")

# =========================
# FUNÇÕES
# =========================

arquivo_atual = None

def novo_arquivo():

    global arquivo_atual

    arquivo_atual = None

    editor.delete("1.0", tk.END)

    status.config(text="Novo arquivo")

def abrir_arquivo():

    global arquivo_atual

    caminho = filedialog.askopenfilename(
        filetypes=[("Python", "*.py"), ("Texto", "*.txt")]
    )

    if not caminho:
        return

    arquivo_atual = caminho

    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read()

    editor.delete("1.0", tk.END)
    editor.insert(tk.END, conteudo)

    status.config(text=f"Aberto: {caminho}")

def salvar_arquivo():

    global arquivo_atual

    if not arquivo_atual:

        caminho = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("Python", "*.py"), ("Texto", "*.txt")]
        )

        if not caminho:
            return

        arquivo_atual = caminho

    with open(arquivo_atual, "w", encoding="utf-8") as f:
        f.write(editor.get("1.0", tk.END))

    status.config(text=f"Salvo: {arquivo_atual}")

# =========================
# TOPO
# =========================

topbar = tk.Frame(root, bg="#111111", height=40)
topbar.pack(fill="x")

btn_novo = tk.Button(
    topbar,
    text="Novo",
    command=novo_arquivo,
    bg="#222",
    fg="white",
    relief="flat"
)

btn_novo.pack(side="left", padx=5, pady=5)

btn_abrir = tk.Button(
    topbar,
    text="Abrir",
    command=abrir_arquivo,
    bg="#222",
    fg="white",
    relief="flat"
)

btn_abrir.pack(side="left", padx=5)

btn_salvar = tk.Button(
    topbar,
    text="Salvar",
    command=salvar_arquivo,
    bg="#222",
    fg="white",
    relief="flat"
)

btn_salvar.pack(side="left", padx=5)

# =========================
# EDITOR
# =========================

editor = tk.Text(
    root,
    bg="#1e1e1e",
    fg="#00ff88",
    insertbackground="white",
    font=("Consolas", 11),
    undo=True
)

editor.pack(fill="both", expand=True)

# =========================
# STATUS BAR
# =========================

status = tk.Label(
    root,
    text="Horizon Editor iniciado",
    anchor="w",
    bg="#111111",
    fg="white"
)

status.pack(fill="x")

# =========================
# START
# =========================

root.mainloop()