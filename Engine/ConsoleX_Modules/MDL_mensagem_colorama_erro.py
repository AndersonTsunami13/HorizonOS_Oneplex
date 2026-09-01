# MDL_mensagem_colorama_erro.py

# é chamado para ocultar o cursor para mostrar a mensagem limpa na tela caso tiver faltando a biblioteca colorama.
from Engine.ConsoleX_Modules.MDL_cursor import code_ag as cursor

def code_ad():
    print("""
        ===================================
         HorizonOS Professional XWin One
         Biblioteca ausente detectada

        Infelizmente a biblioteca:

        [ Colorama ]

        não foi encontrada no sistema.

        Para instalar:
        
        pip install colorama

        Motivo:
        Alguns recursos visuais dependem dela.
        
        O sistema não podera ser execultado corretamente 
        caso voce tente rodar sem essa biblioteca.

        Pressione ENTER para continuar...
    """ 
    )
    cursor(False)
    input()

# Anderson_Tsunami.11Xx