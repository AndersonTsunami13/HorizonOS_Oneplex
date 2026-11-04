import tkinter as tk
from tkinter import messagebox

# Função que será chamada quando pressionar a tecla
def acao_f1(event):
    messagebox.showerror("Erro", "Não foi possivel acessar as informações necessarias. errorcode:?")
    # Aqui você pode colocar qualquer ação que queira para a tecla

def acao_f2(event):
    messagebox.showwarning("Erro", "Os arquivos de informações nao estao visiveis no sistema de...")

def acao_f3(event):
    messagebox.showinfo("aviso inportante!", "esse erros podem ser comuns em versoes betas. sertifique sua versao anrtes de qualquer coisa!")

def acao_f4(event):
    messagebox.showinfo("aviso inportante!", "esse erros podem ser comuns em versoes betas. sertifique sua versao anrtes de qualquer coisa!")

def acao_f5(event):
    messagebox.showinfo("Título", "Mensagem")
    
def acao_f6(event):
    messagebox.showwarning("Título", "Mensagem")

def acao_f7(event):
    messagebox.showerror("Título", "Mensagem")

def acao_f8(event):
    messagebox.askquestion("Título", "Pergunta?")

def acao_f9(event):
    messagebox.askokcancel("Título", "Deseja continuar?")

def acao_f10(event):
    messagebox.askyesno("Título", "Confirma?")

def acao_f11(event):
    messagebox.askretrycancel("Título", "Tentar novamente?")

def acao_f12(event):
    messagebox.showerror("Erro", "Não foi possivel acessar as informações necessarias.")

def abrir_segunda():
    def enviar_para_principal():
        valor = entrada.get()
        mensagem.set(f"Recebido da janela 2: {valor}")
        janela2.destroy()

    janela2 = tk.Toplevel(janela)
    janela2.title("Janela 2")
    tk.Label(janela2, text="Digite algo:").pack(padx=10, pady=5)
    entrada = tk.Entry(janela2)
    entrada.pack(padx=10, pady=5)
    tk.Button(janela2, text="Enviar", command=enviar_para_principal).pack(padx=10, pady=10)

def sobre():
    sobre = tk.Toplevel(janela)
    sobre.title("Sobre o teste")
    sobre.geometry("400x250")

    # Texto
    texto = """Sistema operacional
Versão: 1.0
Desenvolvido com Python e tkinter
"""

    label = tk.Label(
    sobre,
    text=texto,
    justify="left",
    padx=20,
    pady=20
    )
    label.pack()

def esconder_janela():
    janela.withdraw()   # esconde a janela

def clique_direito(event):
    menu_contexto.post(event.x_root, event.y_root)

def acao_1():
    print("numero 1")

def acao_2():
    print("numero 2")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Janela com Ação para F1")
janela.geometry("400x300")
janela.configure(bg="black")

menubar = tk.Menu(janela, bg="#000000", fg="white", activebackground="#555555", activeforeground="white")
janela.config(menu=menubar)

arquivo_menu = tk.Menu(menubar, tearoff=0)
arquivo_menu.add_command(label="Abrir")
arquivo_menu.add_command(label="Salvar")
arquivo_menu.add_separator()
arquivo_menu.add_command(label="Sair", command=janela.quit)
arquivo_menu.add_command(label="Ocultar janela", command=esconder_janela)
menubar.add_cascade(label="Arquivo", menu=arquivo_menu)

ajuda_menu = tk.Menu(menubar, tearoff=0)
ajuda_menu.add_command(label="Sobre", command=sobre)
menubar.add_cascade(label="Ajuda", menu=ajuda_menu)

menu_contexto = tk.Menu(janela, tearoff=0)
menu_contexto.add_command(label="opcao 1", command=acao_1)
menu_contexto.add_command(label="opcao 2", command=acao_2)
menu_contexto.add_separator()
menu_contexto.add_command(label="sair", command=janela.quit)

janela.bind("<Button-3>", clique_direito)

janela.bind("<F1>", acao_f1)
janela.bind("<F2>", acao_f2)
janela.bind("<F3>", acao_f3)
janela.bind("<F4>", acao_f4)
janela.bind("<F5>", acao_f5)
janela.bind("<F6>", acao_f6)
janela.bind("<F7>", acao_f7)
janela.bind("<F8>", acao_f8)
janela.bind("<F9>", acao_f9)
janela.bind("<F10>", acao_f10)
janela.bind("<F11>", acao_f11)
janela.bind("<F12>", acao_f12)

botao = tk.Button(janela, text="Clique aqui 5", command=lambda: print("Botão pressionado"))
botao.place(x=30, y=250)
botao.configure(bg="blue", fg="white")

mensagem = tk.StringVar(value="Nenhuma mensagem ainda.")
tk.Label(janela, textvariable=mensagem, bg="black", fg="white").pack(padx=10, pady=10)
tk.Button(janela, text="Abrir janela 2", command=abrir_segunda).pack(padx=10, pady=10)

barra = tk.Frame(
    janela,
    bg="#202020",
    height=40
)

barra.pack(side="bottom", fill="x")

inicio = tk.Button(barra, text="🏠")
inicio.pack(side="left")

explorer = tk.Button(barra, text="📂")
explorer.pack(side="left")

botao = tk.Button(barra, text="Clique aqui 5", command=lambda: print("Botão pressionado"))
botao.pack(side="right")
botao.configure(bg="blue", fg="white")

# Iniciar a interface gráfica 
janela.mainloop()