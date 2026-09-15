# ScreenFailed_screen.py

import sys
from Engine.UI_Engine_ConsoleX import escrever, limpar, enter

def tela_da_morte(CD="Unknown", AA="Unknown", C="Sem detalhes", L="Indefinido", TF=False, erroname = None, errocomplet = None):
    limpar()
    largura = 80
    escrever("=" * largura, "RED", performance=True)
    escrever(" " * ((largura - 30)//2) + " !!! HORIZONOS SYSTEM FAILURE !!!", "RED", performance=True)
    escrever("=" * largura, "RED", performance=True)
    
    escrever("\n[Aviso!] Um erro fatal foi detectado no sistema.")
    escrever("\n[Aviso!] O sistema foi encerrado para evitar danos.\n")
    
    escrever(f"Código do erro:    {CD}", "YELLOW")
    escrever(f"Arquivo afetado:    {AA}", "YELLOW")
    escrever(f"Comentários:    {C}", "YELLOW")
    escrever(f"Local:    {L}\n", "YELLOW")
    
    escrever(f"\nDetalhes do erro:\n{erroname}")
    
    enter()
    
    if TF:
        tela_fatal(errocomplet)

def tela_fatal(erro_texto="Erro desconhecido"):
    limpar()
    largura = 80
    frase = "!!! HORIZONOS SYSTEM FATAL ERROR !!!"
    # Linha de cima inteira vermelha
    escrever(" " * largura, "RED", "normal", "RED", performance=True)

    # Linha do meio: fundo vermelho em toda a largura, frase centralizada
    meio = frase.center(largura)  # centraliza a frase
    escrever(meio, "WHITE", "normal", "RED", performance=True)

    # Linha de baixo inteira vermelha
    escrever(" " * largura, "RED", "normal", "RED", performance=True)
    
    escrever("# Recomenda-se fechar e reabrir o sistema.", "YELLOW", performance=True)
    escrever("# Se o problema persistir, infelizmente tem problemas no código.", "YELLOW", performance=True)
    
    escrever("\n[Detalhes do problema]:", "CYAN", performance=True)
    escrever(erro_texto, performance=True)

    enter()

    sys.exit()
    
# Anderson_Tsunami.11Xx