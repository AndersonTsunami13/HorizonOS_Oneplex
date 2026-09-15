# UI_ENGINE_XConsole.py — Sistema de escrita do HorizonUI

"""
~~~ Estrutura de construção do código ~~~
    // V4

       AVISO!!!!!!!!!!!!!!!!!!!!!!!!
   > Se você alterar esse arquivo:
    > faça backup!
     > reze!
      > peça desculpas antecipadamente ☠️
      
>>> A ideia do code_aa e para usar um conceito de otimização simples. provavelmente sera substituido para o padrao normal caso isso quebre coisas do sistema.
"""

# importações 
import sys, time

# Modulos por arquivos
try:
    from Engine.ConsoleX_Modules.loading.MDL_loading1 import mdl_loading1
    from Engine.ConsoleX_Modules.loading.MDL_loading2 import mdl_loading2
    from Engine.ConsoleX_Modules.loading.MDL_loading3 import mdl_loading3
    from Engine.ConsoleX_Modules.loading.MDL_loading4 import mdl_loading4
    from Engine.ConsoleX_Modules.loading.MDL_loading5 import mdl_loading5
    from Engine.ConsoleX_Modules.loading.MDL_loading6 import mdl_loading6
    from Engine.ConsoleX_Modules.loading.MDL_loading7 import mdl_loading7
    from Engine.ConsoleX_Modules.MDL_cursor_posicionar import mdl_cursor_posicionar
    from Engine.ConsoleX_Modules.MDL_cursor import mdl_cursor
    from Engine.ConsoleX_Modules.MDL_dynamic_bar import mdl_dynamic_bar, mdl_dynamic_bar_start, mdl_dynamic_bar_finish
    from Engine.ConsoleX_Modules.MDL_enter import mdl_enter
    from Engine.ConsoleX_Modules.MDL_escrever_piscando import mdl_escrever_piscando
    from Engine.ConsoleX_Modules.MDL_escrever import mdl_escrever
    from Engine.ConsoleX_Modules.MDL_input_silencioso import mdl_input_silencioso
    from Engine.ConsoleX_Modules.MDL_janela_terminal import mdl_janela_terminal
    from Engine.ConsoleX_Modules.MDL_limpar import mdl_limpar
    from Engine.ConsoleX_Modules.MDL_pular_linha import mdl_pular_linha
    from Engine.ConsoleX_Modules.MDL_status_bar import mdl_status_bar_system_start, mdl_status_bar_log_start, mdl_status_bar_message_start, mdl_status_bar_system, mdl_status_bar_message, mdl_status_bar_log, mdl_status_bar_system_finish, mdl_status_bar_message_finish, mdl_status_bar_log_finish
    from Engine.ConsoleX_Modules.MDL_texto_rolando import mdl_texto_rolando
    from Engine.ConsoleX_Modules.MDL_time_s import mdl_time_s
    from Engine.ConsoleX_Modules.MDL_titulo_console import mdl_titulo_console
    from Engine.ConsoleX_Modules.MDL_perguntar import mdl_perguntar

except ImportError as e:
    print(f"Erro ao importar módulos: {e}")
    time.sleep(2)
    sys.exit()

# =======================
#    Funções da engine
# =======================  

# =============================================================
# Animações de carregamento

def loading1(text="Carregando"):
    mdl_loading1(text)

def loading2(duracao=3):
    mdl_loading2(duracao)

def loading3(duracao=3, text="Carregando", cor="GREEN"):
    mdl_loading3(duracao, text, cor)

def loading4(duracao=3, cor="GREEN"):
    mdl_loading4(duracao, cor)

def loading5(duracao=3, text="Carregando", cor="GREEN"):
    mdl_loading5(duracao, text, cor)

def loading6(duracao=3, delay=0.01):
    mdl_loading6(duracao, delay)

def loading7(duracao=5):
    mdl_loading7(duracao)

# =============================================================


# =============================================================
# Funções de escrita e manipulação do console

def cursor_posicionar(linha, coluna):
    mdl_cursor_posicionar(linha, coluna)

def cursor(option):
    mdl_cursor(option)

# ============================================================


# ============================================================
# Dynamic_bar

def dynamic_bar_start():
    mdl_dynamic_bar_start()

def dynamic_bar(message):
    mdl_dynamic_bar(message)

def dynamic_bar_finish():
    mdl_dynamic_bar_finish()

# ============================================================


# ============================================================
# Funções de escrita e manipulação do console

def enter(message="Pressione enter para continuar..."):
    mdl_enter(message)

def escrever_piscando(text="test", x=1, y=1, vezes=5, delay=0.5):
    mdl_escrever_piscando(text, x, y, vezes, delay)

def escrever(text="   Olá, mundo!   ", cor="WHITE", estilo="destaque", fundo="BLACK", velocidade=0.1, pular_linha=True, performance=False, mesma_linha=False, COLORAMA_OK=True):
    mdl_escrever(text, cor, estilo, fundo, velocidade, pular_linha, performance, mesma_linha, COLORAMA_OK)

def input_silencioso(prompt=""): 
    mdl_input_silencioso(prompt)

def janela_terminal(linha=5, coluna=10, largura=30, altura=10, titulo="Janela de Teste", anim=True, delay=0.05):
    mdl_janela_terminal(linha, coluna, largura, altura, titulo, anim, delay)

def limpar():   
    mdl_limpar()

def pular_linha():
    mdl_pular_linha()

# ============================================================


# ============================================================
# Status bar

def status_bar_system_start():
    mdl_status_bar_system_start()

def status_bar_message_start():
    mdl_status_bar_message_start()

def status_bar_log_start():
    mdl_status_bar_log_start()

def status_bar_system(message):
    mdl_status_bar_system(message)

def status_bar_message(message):
    mdl_status_bar_message(message)

def status_bar_log(message):    
    mdl_status_bar_log(message)

def status_bar_system_finish():
    mdl_status_bar_system_finish()

def status_bar_message_finish():
    mdl_status_bar_message_finish()

def status_bar_log_finish():
    mdl_status_bar_log_finish()

# ============================================================


# ============================================================
# outras funções
def texto_rolando(texto, largura=30, posicao=0,temp=5000, limpar=True):
    mdl_texto_rolando(texto, largura, posicao, temp, limpar)

def time_s(tempo=5):
    mdl_time_s(tempo)

def titulo_console(titulo="HorizonOS Oneplex"):
    mdl_titulo_console(titulo)

def perguntar(texto, x=1, y=1, cor=None, fundo=None, tipo=str, xy=True):
    return mdl_perguntar(texto, x, y, cor, fundo, tipo, xy)

# ============================================================

# ============================================================
# Teste rapido - debug

if __name__ == "__main__":
    loading1("carregando")
    loading2(3)
    loading3(3, "carregando", "GREEN")
    loading4(3, "GREEN")
    loading5(3, "carregando", "GREEN")
    loading6(30, 0.1)
    loading7(5)
    cursor_posicionar(3, 4)
    cursor(False)  # Mostra o cursor
    input("Pressione Enter para mostrar o cursor...")
    cursor(True)  # Oculta o cursor
    dynamic_bar_start()
    time_s(5)
    dynamic_bar("Nova mensagem na Dynamic Bar!")
    time_s(5)
    dynamic_bar_finish()
    enter("Pressione enter para continuar...")
    escrever("   Olá, mundo!   ", cor="RED", estilo="destaque", fundo="WHITE", velocidade=0.1, pular_linha=True, performance=False, mesma_linha=False, COLORAMA_OK=True)
    text = mdl_input_silencioso("Digite alguma coisa: ")
    print(f"Você digitou: {text}")
    janela_terminal(5, 10, 30, 10, "Janela de Teste", anim=True, delay=0.05)
    janela_terminal(16, 10, 40, 10, "Janela de Teste sem animação", anim=False, delay=0.05)
    limpar()
    pular_linha()
    status_bar_system_start()
    status_bar_log_start()
    status_bar_message_start()
    time_s(5)
    status_bar_system("Nova mensagem na barra de status!")
    status_bar_message("Nova mensagem na barra de mensagens!")
    status_bar_log("Novo log registrado!") 
    time_s(5)
    status_bar_system_finish()
    status_bar_message_finish()
    status_bar_log_finish()
    texto_rolando("Este é um exemplo de texto rolando na tela. Aperte Ctrl+C para interromper a rolagem.", 30)
    titulo_console("Anderson_Tsunami.M3_E36")
    time_s(5)
    pular_linha
    pergunta = perguntar("digite algo ", x=4, y=8, cor="BLUE", fundo="WHITE", tipo=int)
    print(f"Você digitou: {pergunta}")
    enter()

    limpar()
    escrever("esse é um teste simples da engine, o real erro que pode ocorrer é na hora de importar os modulos, caso algum não seja encontrado, o programa irá avisar e encerrar. Em breve o debug mais sofisticado estará disponível.", cor="YELLOW", estilo="destaque", fundo="BLACK", velocidade=0.1, pular_linha=True, performance=False, mesma_linha=False, COLORAMA_OK=True)
    enter()

# ============================================================

# Anderson_Tsunami.M3_E36