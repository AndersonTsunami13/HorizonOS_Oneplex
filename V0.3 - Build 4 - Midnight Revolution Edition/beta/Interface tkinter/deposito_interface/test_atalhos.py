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

# Configuração da janela principal
janela = tk.Tk()
janela.title("Janela com Ação para F1")
janela.geometry("400x300")

# Bind para a tecla F1
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

# Botão de exemplo
botao = tk.Button(janela, text="Clique aqui 1", command=lambda: print("Botão pressionado"))
botao.pack(side="left", pady=10, padx=20)

botao = tk.Button(janela, text="Clique aqui 2", command=lambda: print("Botão pressionado"))
botao.pack(side="right", pady=20, padx=10)

botao = tk.Button(janela, text="Clique aqui", command=lambda: print("Botão pressionado"))
botao.place(x=100, y=150)

# Iniciar a interface gráfica
janela.mainloop()