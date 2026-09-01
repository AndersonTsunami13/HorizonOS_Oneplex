# System/users.py

usuarios = {

    "visitante": {
        "senha":"0000",
        "nivel":1,
        "perfil":"LOW"
    },

    "anderson": {
        "senha":"1234",
        "nivel":2,
        "perfil":"DEV"
    },

    "admin": {
        "senha":"root",
        "nivel":3,
        "perfil":"GOD"
    }

}

usuario_logado=None

def login():

    global usuario_logado

    nome=input("Usuario: ")

    if nome in usuarios:

        senha=input("Senha: ")

        if senha == usuarios[nome]["senha"]:

            usuario_logado=usuarios[nome]

            print(
                f"\nPerfil: "
                f"{usuario_logado['perfil']}"
            )

            return True

    return False
    
if comando == "config":

    if usuario_logado["nivel"] < 2:

        escrever(
        "Acesso negado",
        "RED"
        )

    else:

        abrir_config()
        
# Anderson_Tsunami.11x