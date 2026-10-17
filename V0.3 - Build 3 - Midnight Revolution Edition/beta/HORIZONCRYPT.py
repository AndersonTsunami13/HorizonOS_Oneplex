from cryptography.fernet import Fernet


def bin_encode(dados):
    return " ".join(format(byte, "08b") for byte in dados)


def bin_decode(binary):
    numeros = binary.split()

    try:
        return bytes(int(numero, 2) for numero in numeros)
    except ValueError:
        raise ValueError("Código binário inválido.")


def carregar_chave():
    try:
        with open("horizon.key", "rb") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return None


def gerar_chave():
    chave = Fernet.generate_key()

    with open("horizon.key", "wb") as arquivo:
        arquivo.write(chave)

    print("\n✓ Nova chave criada!")
    print("A chave foi salva em: horizon.key")
    print("IMPORTANTE: compartilhe essa chave apenas com a pessoa de confiança.\n")


def criptografar():
    chave = carregar_chave()

    if chave is None:
        print("\n! Nenhuma chave encontrada.")
        print("Use a opção [3] primeiro.\n")
        return

    mensagem = input("\nMensagem: ")

    cripto = Fernet(chave)

    # Criptografa a mensagem
    codigo = cripto.encrypt(mensagem.encode("utf-8"))

    # Transforma o resultado em binário
    resultado = bin_encode(codigo)

    print("\n╭─ MENSAGEM CRIPTOGRAFADA ─╮")
    print(resultado)
    print("╰──────────────────────────╯\n")


def descriptografar():
    chave = carregar_chave()

    if chave is None:
        print("\n! Nenhuma chave encontrada.")
        print("Use a opção [3] primeiro.\n")
        return

    codigo = input("\nCole o código binário:\n")

    try:
        # Binário → bytes
        dados = bin_decode(codigo)

        cripto = Fernet(chave)

        # Descriptografa
        mensagem = cripto.decrypt(dados)

        print("\n╭─ MENSAGEM ORIGINAL ──────╮")
        print(mensagem.decode("utf-8"))
        print("╰──────────────────────────╯\n")

    except Exception:
        print("\n✗ Não foi possível descriptografar.")
        print("Verifique a chave e o código recebido.\n")


def menu():
    while True:

        print("""
╔══════════════════════════════╗
║       HORIZONCRYPT           ║
╠══════════════════════════════╣
║ [1] Criptografar mensagem    ║
║ [2] Descriptografar mensagem ║
║ [3] Gerar chave              ║
║ [4] Sair                     ║
╚══════════════════════════════╝
""")

        opcao = input("HorizonCrypt > ")

        if opcao == "1":
            criptografar()

        elif opcao == "2":
            descriptografar()

        elif opcao == "3":
            gerar_chave()

        elif opcao == "4":
            print("\nHorizonCrypt encerrado. 🔐")
            break

        else:
            print("\n! Opção inválida.\n")


menu()