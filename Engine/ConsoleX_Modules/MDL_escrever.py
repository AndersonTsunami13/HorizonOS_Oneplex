# MDL_escrever.py

# Chamada de modulos necessario
from Engine.ConsoleX_Modules.MDL_escrever_list import * # lista do colorama
from Engine.ConsoleX_Modules.MDL_cursor import code_ag as cursor # para ocultar o cursor quando necessario
from Engine.ConsoleX_Modules.MDL_mensagem_colorama_erro import code_ad as mensagem_colorama_erro # a tela de erro caso o colorama nao esteja instalado

# Importações
import sys, time, re

# Importação do colorama
try:
    from colorama import init, Fore, Back, Style
    
    # Inicializa o Colorama
    init(autoreset=False, strip=False)
    COLORAMA_OK = True

except ImportError: # caso o colorama nao esteja instalado, mostra a mensagem de erro.
    COLORAMA_OK = False
    mensagem_colorama_erro()
    
def code_ai(
    texto,
    cor=None,
    estilo=None,
    fundo=None,
    velocidade=None,
    pular_linha=None,
    performance=None,
    mesma_linha=False,
    COLORAMA_OK=True
):
    """Sistema de escrita inteligente"""

    # usa padrão se não for passado
    cor = cor or TEMA_ATUAL["cor"]
    estilo = estilo or TEMA_ATUAL["estilo"]
    fundo = fundo or TEMA_ATUAL["fundo"]
    velocidade = velocidade if velocidade is not None else TEMA_ATUAL["velocidade"]
    pular_linha = pular_linha if pular_linha is not None else TEMA_ATUAL["pular_linha"]
    performance = performance if performance is not None else TEMA_ATUAL["performance"]
    mesma_linha = mesma_linha if mesma_linha is not None else TEMA_ATUAL["mesma_linha"]

    if not COLORAMA_OK:
        print(texto)
        return

    if performance: # desativa o efeito de digitação 
        velocidade = 0

    mensagem = f"{ESTILOS.get(estilo, Style.NORMAL)}{FUNDOS.get(fundo, Back.BLACK)}{TEXTOS.get(cor, Fore.WHITE)}{texto}{Style.RESET_ALL}"
    
    cursor(False)  # Desativa o cursor durante a escrita

    if mesma_linha:

        sys.stdout.write("\r\033[K")
        sys.stdout.write(mensagem)
        sys.stdout.flush()

    else:

        partes = re.split(
            r'(\x1b\[[0-9;]*m)',
            mensagem
        )

        for p in partes:

            if re.match(
                r'\x1b\[[0-9;]*m',
                p
            ):

                sys.stdout.write(p)
                sys.stdout.flush()
    
            else:

                for c in p:

                    sys.stdout.write(c)
                    sys.stdout.flush()

                    if velocidade > 0:
    
                        time.sleep(
                            velocidade
                        )

    if pular_linha:

        sys.stdout.write("\n")

    sys.stdout.flush() 

    cursor(True)  # Reativa o cursor após a escrita

# Anderson_Tsunami.11Xx