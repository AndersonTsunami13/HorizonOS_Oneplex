# MDL_escrever_atualizar.py

# Importações
from Engine.ConsoleX_Modules.MDL_escrever import code_ai

# Esse modulo simplifica a chamada do escrever na mesma linha do modulo escrever.

def code_ah(texto, cor=None, estilo=None, fundo=None): # atualiza a linha sem apagar a tela toda
    code_ai(texto, cor=cor, estilo=estilo, fundo=fundo, mesma_linha=True, pular_linha=False, performance=True)

# Anderson_Tsunami.11Xx