# debug3.py

from Security.securitymodule_createpassword import create_password_one, create_password_two
from Engine.UI_Engine_ConsoleX import escrever, enter, input_silencioso, titulo_console, time_s, cursor

def debug3():
    titulo_console("Debug 3 ativo")

    cursor(False)
    escrever("modo 1...")
    time_s(1)
    cursor(True)
    create_password_one()

    cursor(False)
    escrever("modo 2...")
    time_s(1)
    cursor(True)
    
    # Captura a senha do usuário
    senha_usuario = input_silencioso("Digite a sua senha: ")
    
    cursor(False)

    # Chama a função e armazena o hash retornado por ela
    password_hash = create_password_two(senha_usuario)

    # Pronto! Agora a variável password_hash tem o valor do hash
    escrever(f"O hash salvo é: {password_hash}")
    enter()

# Anderson_Tsunami.11Xx