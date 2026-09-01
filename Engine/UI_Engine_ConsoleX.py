# UI_ENGINE_XConsole.py — Sistema de escrita do HorizonUI

"""
~~~ Estrutura de construção do código ~~~
    // V3

>>> Importação dos módulos
>>> Função de limpar a tela, apertar enter e input silencioso 
>>> Biblioteca de cores do escrever()
>>> Função de escrever
>>> Debug
>>> Definição do título das janela
>>> O novo time.sleep
>>> controlador do cursor
>>> Atualizar a linha sem apagar a tela toda

   AVISO!!!!!!!!!!!!!!!!!!!!!!!!
   > Se você alterar esse arquivo:
    > faça backup!
     > reze!
      > peça desculpas antecipadamente ☠️
      
>>> O novo recurso da engine é a separação das funções por arquivos, facilitando a modificação nos módulos. Esse arquivo ainda e principal!
>>> A ideia do code_aa e para usar um conceito de otimização simples. provavelmente sera substituido para o padrao normal caso isso quebre coisas do sistema.
"""

"""
code_aa = limpar
code_ab = enter
code_ac = input_silencioso
code_ad = mensagem_colorama_erro >>> Em outro lugar, mas é chamado aqui para ser usado no escrever()
code_ae = titulo_console
code_af = time_s
code_ag = cursor
code_ah = escrever_atualizar
code_ai = escrever
code_aj = sair
code_ak = escrever_loading
code_al - pular_linha
code_am = cursor_posicionar
code_an = janela_terminal
code_ao = anim_loading1
code_ap = anim_loading2
code_aq = anim_loading3
code_ar = status_bar_system_start
    code_ar2 = status_bar_system
    code_ar3 = status_bar_system_finish
code_as = status_bar_message_start
    code_as2 = status_bar_message
    code_as3 = status_bar_message_finish
code_at = status_bar_log_start
    code_at2 = status_bar_log
    code_at3 = status_bar_log_finish
code_au = texto_rodando
code_av = slide_text
code_aw = anim_box
code_ax = escrever_piscando
code_ay = progress_bar
"""

# importações 
import sys, time

# Modulos por arquivos
# fazer o teste do uso dos arquivos de funções, caso algum não seja encontrado, o programa irá avisar e encerrar
try: 
    from Engine.ConsoleX_Modules.MDL_limpar import code_aa
    from Engine.ConsoleX_Modules.MDL_enter import code_ab
    from Engine.ConsoleX_Modules.MDL_input_silencioso import code_ac
    from Engine.ConsoleX_Modules.MDL_titulo_console import code_ae
    from Engine.ConsoleX_Modules.MDL_time_s import code_af
    from Engine.ConsoleX_Modules.MDL_cursor import code_ag
    from Engine.ConsoleX_Modules.MDL_escrever_atualizar import code_ah
    from Engine.ConsoleX_Modules.MDL_escrever import code_ai
    from Engine.ConsoleX_Modules.MDL_sair import code_aj
    from Engine.ConsoleX_Modules.MDL_escrever_loading import code_ak
    from Engine.ConsoleX_Modules.MDL_pular_linha import code_al
    from Engine.ConsoleX_Modules.MDL_cursor_posicionar import code_am
    from Engine.ConsoleX_Modules.MDL_janela_terminal import code_an
    from Engine.ConsoleX_Modules.MDL_loading1 import code_ao
    from Engine.ConsoleX_Modules.MDL_loading2 import code_ap
    from Engine.ConsoleX_Modules.MDL_loading3 import code_aq
    from Engine.ConsoleX_Modules.MDL_status_bar_one import code_ar, code_ar2, code_ar3
    from Engine.ConsoleX_Modules.MDL_status_bar_two import code_as, code_as2, code_as3
    from Engine.ConsoleX_Modules.MDL_status_bar_3 import code_at, code_at2, code_at3
    from Engine.ConsoleX_Modules.MDL_texto_rolando import code_au
    from Engine.ConsoleX_Modules.MDL_anim_module import code_av, code_aw, code_ax, code_ay

except ImportError as e:
    print(f"Erro ao importar módulos: {e}")
    time.sleep(2)
    sys.exit()

# =======================
#    Funções da engine
# =======================  
  
def limpar(): # para limpar a tela
    code_aa()
    
def enter(n = "Pressione enter para continuar..."): # aperta enter para continuar
    code_ab(n)
    
def input_silencioso(p="Digite: "): # para input silencioso, sem mostrar o que é digitado
    return code_ac(p)

def escrever(texto, cor=None, estilo=None, fundo=None, velocidade=None, pular_linha=None, performance=True, mesma_linha=False): # cada opcao faz uma coisa, considere ler o MDL_escrever.py para entender melhor
    code_ai(texto, cor, estilo, fundo, velocidade, pular_linha, performance, mesma_linha)

def time_s(time): # para o time.sleep, mas com a possibilidade de ser alterado no futuro
    code_af(time)

def titulo_console(n): # para definir o título da janela do console
    code_ae(n)

def cursor(mode): # para controlar o cursor do console, esconder ou mostrar
    code_ag(mode)  

def escrever_atualizar(texto, cor=None, estilo=None, fundo=None): # atualiza a linha sem apagar a tela toda
    code_ah(texto, cor, estilo, fundo)  

def sair():
    code_aj()

def escrever_loading(a=3, b="Certo! Aguarde", c="BLUE"):
    code_ak(a, b, c)

def pular_linha():
    code_al()

def cursor_posicionar(linha, coluna):
    code_am(linha, coluna)

def janela_terminal(linha, coluna, largura, altura, titulo=""):
    code_an(linha, coluna, largura, altura, titulo)

def anim_loading1(text):
    code_ao(text)

def anim_loading2(duracao):
    code_ap(duracao)

def anim_loading3(duracao, text, cor):
    code_aq(duracao, text, cor)

def status_bar_system_start():
    code_ar()

def status_bar_system(text):
    code_ar2(text)

def status_bar_system_finish():
    code_ar3()

def status_bar_message_start():
    code_as()

def status_bar_message(text):
    code_as2(text)

def status_bar_message_finish():
    code_as3()

def status_bar_log_start():
    code_at()

def status_bar_log(text):
    code_at2(text)

def status_bar_log_finish():
    code_at3()

def texto_rodando(text, tamanho=20, pos=0):
    code_au(text, tamanho, pos)

def slide_text(text, inicio, fim, linha, delay=0.05):
    code_av(text, fim, inicio, linha, delay)

def anim_box(x, y, largura, altura, delay=0.03):
    code_aw(x, y, largura, altura, delay)

def escrever_piscando(texto="text", x=1, y=1, vezes=5, delay=0.3):
    code_ax(texto, x, y, vezes, delay)

def progress_bar(total=100, delay=0.05):
    code_ay(total, delay)

# Anderson_Tsunami.11Xx