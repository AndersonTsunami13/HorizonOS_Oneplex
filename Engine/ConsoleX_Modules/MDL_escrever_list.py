# MDL_escrever_list.py

# esse arquivo é apenas um complemento do MDL_escreve.py

from colorama import init, Fore, Back, Style

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

# =======================
# Função única
# =======================
TEMA_ATUAL = { # Configurações padrão da escrita
    "cor": "CYAN", # Azul claro
    "estilo": "normal", # Deixa em destaque 
    "fundo": "BLACK", # o fundo preto é o normal em vários terminais... 
    "velocidade": 0.04, # velocidade confortavel
    "pular_linha": True, # padrão 
    "performance": False, # ative apenas se for desativar o efeito de digitação 
    "mesma_linha": False, # faz o terminal continuar normalmente
    "COLORAMA_OK": True # se o colorama estiver instalado, ele vai funcionar normalmente
}


# Anderson_Tsunami.11Xx