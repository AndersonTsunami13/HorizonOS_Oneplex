import tkinter as tk
from tkinter import messagebox
from turtle import delay

from Programs.Win.MeuPc2 import abrir_meu_pc
from Programs.Win.Terminal2 import abrir_terminal
from Programs.Win.Lixeira2 import abrir_lixeira
from Programs.Win.Navegador2 import abrir_navegador
from Programs.Win.TestStatusBar2 import abrir_test_statusbar

from Engine.UI_TitleBar import *
from UI.system.Shutdown_Screen import iniciar_desligamento

from Information.WinConfig import *


# =============================
# CONFIGURAÇÕES PERSONALIZÁVEIS
# =============================
DISCOS = ["C:/", "D:/", "E:/", "F:/", "G:/"]  # Edite aqui se quiser

# =============================
# Função da Área de Trabalho
# =============================
def iniciar_interface():
    janela = tk.Tk()
    janela.title(f"{NAME_SYSTEM} {VERSAO_HORIZON_2}")
    janela.attributes("-fullscreen", True)
    janela.configure(bg=f"{TEMA_FUNDO}")

    criar_titlebar(janela, "New StatusBar")
    atualizar_frase()

    set_status("Conectado ao HorizonNet")

    janela.after(3000, lambda: set_erro("config.sys não encontrado"))

    janela.after(6000, lambda: set_sucesso("Sistema reparado"))
    
    def system_shutdown():
        janela.destroy()
        iniciar_desligamento()
    
    def abrir_menu_iniciar(janela):
        global iniciar_desligamento
        
        menu = tk.Toplevel(janela)
        menu.overrideredirect(True)
        menu.resizable(False, False)
        menu.attributes("-topmost", True)
    
        menu.bind("<FocusOut>", lambda e: menu.destroy())
        menu.focus_force()
        
        largura = 250
        altura = 350
        
        x = janela.winfo_rootx()
        y = janela.winfo_rooty() + janela.winfo_height() - altura - 20
        
        menu.geometry(f"{largura}x{altura}+{x}+{y}")

        button1_menu = tk.Button(menu, text="Meu PC", bg=f"{TEMA_ICONE_6_1}", fg=f"{TEMA_ICONE_6_2}", 
                 font=(f"{FONT_TEXTO}", (FONT_TEXTO_VALOR_3)), command=abrir_meu_pc)
        button1_menu.pack(pady=10)
        button2_menu = tk.Button(menu, text="Terminal", bg=f"{TEMA_ICONE_6_1}", fg=f"{TEMA_ICONE_6_2}",
                 font=(f"{FONT_TEXTO}", (FONT_TEXTO_VALOR_3)), command=abrir_terminal)
        button2_menu.pack(pady=10)
        button3_menu = tk.Button(menu, text="Desligar", bg=f"{TEMA_ICONE_7_1}", fg=f"{TEMA_ICONE_7_2}",
                 font=(f"{FONT_TEXTO}", (FONT_TEXTO_VALOR_3)), command=system_shutdown)
        button3_menu.pack(pady=10)
        button4_menu = tk.Button(menu, text="Fechar Menu", bg=f"{TEMA_ICONE_8_1}", fg=f"{TEMA_ICONE_8_2}", 
                 font=(f"{FONT_TEXTO}", (FONT_TEXTO_VALOR_3)), command=menu.destroy)
        button4_menu.pack(pady=10)
             
    # ÍCONES
    def icone_abrir_pc():
        abrir_meu_pc()

    def icone_abrir_lixeira():
        abrir_lixeira()

    def icone_abrir_jogos():
        messagebox.showerror("Erro", "algo nao deu certo!")

    def icone_abrir_terminal():
        abrir_terminal()

    def icone_abrir_navegador():
        abrir_navegador()

    # ÍCONES NA TELA
    icone_meupc = tk.Label(janela, text="🖥️\nMeu PC", fg=f"{TEMA_ICONE_1}", bg=f"{TEMA_ICONE_2}", 
             font=(f"{FONT_ICONE}", (FONT_ICONE_VALOR)), justify="left",
             cursor="hand2")
    icone_meupc.place(x=30, y=30)
    
    icone_lixeira = tk.Label(janela, text="🗑\nLixeira", fg=f"{TEMA_ICONE_1}", bg=f"{TEMA_ICONE_2}", 
             font=(f"{FONT_ICONE}", (FONT_ICONE_VALOR)), justify="left",
             cursor="hand2")
    icone_lixeira.place(x=30, y=100)
             
    icone_jogos = tk.Label(janela, text="🕹\nMeus Jogos", fg=f"{TEMA_ICONE_1}", bg=f"{TEMA_ICONE_2}", 
             font=(f"{FONT_ICONE}", (FONT_ICONE_VALOR)), justify="left",
             cursor="hand2")
    icone_jogos.place(x=30, y=160)
             
    icone_terminal = tk.Label(janela, text="👨‍💻\nTerminal", fg=f"{TEMA_ICONE_1}", bg=f"{TEMA_ICONE_2}", 
             font=(f"{FONT_ICONE}", (FONT_ICONE_VALOR)), justify="left",
             cursor="hand2")
    icone_terminal.place(x=30, y=220)
             
    icone_navegador = tk.Label(janela, text="📶\nNavegador", fg=f"{TEMA_ICONE_1}", bg=f"{TEMA_ICONE_2}", 
             font=(f"{FONT_ICONE}", (FONT_ICONE_VALOR)), justify="left",
             cursor="hand2")
    icone_navegador.place(x=30, y=280)
             
    icone_teststatusbar = tk.Label(janela, text="➖\nTest StatusBar", fg=f"{TEMA_ICONE_1}", bg=f"{TEMA_ICONE_2}", 
             font=(f"{FONT_ICONE}", (FONT_ICONE_VALOR)), justify="left",
             cursor="hand2")
    icone_teststatusbar.place(x=30, y=340)
             

    # Associando funções
    icone_meupc.bind("<Button-1>", lambda e: icone_abrir_pc())
    icone_lixeira.bind("<Button-1>", lambda e: icone_abrir_lixeira())
    icone_jogos.bind("<Button-1>", lambda e: icone_abrir_jogos())
    icone_terminal.bind("<Button-1>", lambda e: icone_abrir_terminal())
    icone_navegador.bind("<Button-1>", lambda e: icone_abrir_navegador())
    icone_teststatusbar.bind("<Button-1>", lambda e: abrir_test_statusbar(janela))

    botao_iniciar = tk.Label(janela, text="⛰ Iniciar", fg=f"{TEMA_ICONE_3}", bg=f"{TEMA_BARRA_DE_TAREFA}", 
                             font=(f"{FONT_TEXTO}", (FONT_TEXTO_VALOR_4)), padx=20,
                             cursor="hand2")
    botao_iniciar.pack(side="bottom")
    botao_iniciar.bind("<Button-1>", lambda e: abrir_menu_iniciar(janela))