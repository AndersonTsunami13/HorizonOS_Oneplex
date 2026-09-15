# MDL_escrever.py

# Importações
import sys, time, re

def cursor(o):
    if o:
        sys.stdout.write("\033[?25h") # Sequência ANSI para mostrar o cursor
    else:
        sys.stdout.write("\033[?25l") # Sequência ANSI para esconder o cursor
    sys.stdout.flush() # faz a saída ser exibida imediatamente


# Importação do colorama
try:
    from colorama import init, Fore, Back, Style
    
    # Inicializa o Colorama
    init(autoreset=False, strip=False)

except ImportError: # caso o colorama nao esteja instalado, mostra a mensagem de erro.
    print("""
        ===================================
                HorizonOS Oneplex
         Biblioteca faltando!

        Infelizmente a biblioteca:

        [ Colorama ]

        não foi encontrada no sistema.

        Para instalar:
            pip install colorama
        
        Motivo:
        Alguns recursos visuais dependem dela.

        Pressione ENTER para continuar...
    """ 
    )
    cursor(False)
    input()
    sys.exit()

# =======================
# Texto (Fore)
# =======================
TEXTOS = {
    "BLACK": Fore.BLACK, # Preto
    "RED": Fore.RED, # Vermelho 
    "GREEN": Fore.GREEN, # Verde
    "YELLOW": Fore.YELLOW, # Amarelo
    "BLUE": Fore.BLUE, # Azul
    "MAGENTA": Fore.MAGENTA, # Rosa
    "CYAN": Fore.CYAN, # Azul claro
    "WHITE": Fore.WHITE # Branco
}

# =======================
# Fundo (Back)
# =======================
FUNDOS = {
    "BLACK": Back.BLACK, # Preto
    "RED": Back.RED, # Vermelho
    "GREEN": Back.GREEN, # Verde
    "YELLOW": Back.YELLOW, # Amarelo
    "BLUE": Back.BLUE, # Azul 
    "MAGENTA": Back.MAGENTA, # Rosa
    "CYAN": Back.CYAN, # Azul claro
    "WHITE": Back.WHITE # Branco
}

# =======================
# Estilos (Style)
# =======================
ESTILOS = {
    "normal": Style.NORMAL, # Texto normal
    "destaque": Style.BRIGHT, # Texto em negrito "destacado"
    "apagado": Style.DIM, # Texto apagado "podendo ser usado para destaques mais simples..."
    "reset": Style.RESET_ALL # resetar tudo no final "isso é usado só no escrever!"
}

def mdl_escrever(texto, cor="CYAN", estilo="normal", fundo="BLACK", velocidade=0.04, pular_linha=True, performance=False, mesma_linha=False, COLORAMA_OK=True):
    """Sistema de escrita inteligente"""

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

if __name__ == "__main__":
    # Teste da função mdl_escrever
    mdl_escrever("   Olá, mundo!   ", cor="RED", estilo="destaque", fundo="WHITE", velocidade=0.1, pular_linha=True, performance=False, mesma_linha=False, COLORAMA_OK=True)

# Anderson_Tsunami.M3_E36