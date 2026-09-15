import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_ROOT = os.path.join(BASE_DIR, "docs")   # pasta onde estão os 534 txt
pasta_atual = DOCS_ROOT
favoritos = []


def ensure_docs_root():
    if not os.path.isdir(DOCS_ROOT):
        try:
            os.makedirs(DOCS_ROOT, exist_ok=True)
            print(f"A pasta '{DOCS_ROOT}' não existia e foi criada. Coloque aqui os arquivos .txt da documentação.")
        except Exception as e:
            print("Erro ao criar a pasta docs:", e)
            return False
    return True


def caminho_rel():
    return os.path.relpath(pasta_atual, DOCS_ROOT)


def listar():
    try:
        itens = os.listdir(pasta_atual)
        if not itens:
            print("(pasta vazia)")
            return
        for i in itens:
            print(i)
    except Exception as e:
        print("Erro ao listar:", e)


def entrar(pasta):
    global pasta_atual
    novo = os.path.join(pasta_atual, pasta)

    if os.path.isdir(novo):
        pasta_atual = novo
    else:
        print("Pasta não encontrada.")


def voltar():
    global pasta_atual
    if os.path.abspath(pasta_atual) != os.path.abspath(DOCS_ROOT):
        pasta_atual = os.path.dirname(pasta_atual)


def ler_blocos(arquivo, bloco=20):
    caminho = os.path.join(pasta_atual, arquivo)

    if not os.path.isfile(caminho):
        print("Arquivo não encontrado.")
        return

    try:
        with open(caminho, "r", encoding="utf-8") as f:

            linhas = f.readlines()
            total = len(linhas)
            atual = 0

            while atual < total:

                for i in range(bloco):
                    if atual >= total:
                        break

                    print(linhas[atual].rstrip())
                    atual += 1

                print(f"\n--- {atual}/{total} linhas ---")

                if atual >= total:
                    break

                cmd = input("[ENTER continuar | q sair] ")
                if cmd.lower() == "q":
                    return

        print("\n=== FIM DO DOCUMENTO ===")

    except Exception as e:
        print("Erro ao abrir:", e)


def buscar(palavra):
    print(f"\nProcurando '{palavra}'...\n")

    encontrados = []

    for raiz, pastas, arquivos in os.walk(DOCS_ROOT):
        for arq in arquivos:
            if arq.endswith(".txt") and palavra.lower() in arq.lower():
                caminho = os.path.join(raiz, arq)
                encontrados.append(caminho)

    if not encontrados:
        print("Nada encontrado.")
        return

    for r in encontrados:
        print(os.path.relpath(r, DOCS_ROOT))


def add_fav(nome):
    caminho = os.path.join(pasta_atual, nome)

    if os.path.isfile(caminho):
        favoritos.append(caminho)
        print("Adicionado aos favoritos.")
    else:
        print("Arquivo não encontrado.")


def listar_fav():
    if not favoritos:
        print("Sem favoritos.")
        return

    print("\n=== FAVORITOS ===")
    for f in favoritos:
        print(os.path.relpath(f, DOCS_ROOT))


def ajuda():
    print("""
Comandos disponíveis:

dir                -> listar arquivos
cd <pasta>         -> entrar na pasta
back               -> voltar pasta
open <arquivo>     -> ler arquivo
search <palavra>   -> buscar arquivo
fav <arquivo>      -> adicionar favorito
favlist            -> listar favoritos
help               -> ajuda
exit               -> sair
""")


if not ensure_docs_root():
    sys.exit(1)

print("=== HORIZON PYDOCS ===")
print("Leitor offline da documentação do Python\n")

ajuda()

while True:

    cmd = input(f"\nPyDocs:{caminho_rel()}> ").split()

    if not cmd:
        continue

    c = cmd[0].lower()

    if c == "dir":
        listar()

    elif c == "cd" and len(cmd) > 1:
        entrar(cmd[1])

    elif c == "back":
        voltar()

    elif c == "open" and len(cmd) > 1:
        ler_blocos(cmd[1])

    elif c == "search" and len(cmd) > 1:
        buscar(cmd[1])

    elif c == "fav" and len(cmd) > 1:
        add_fav(cmd[1])

    elif c == "favlist":
        listar_fav()

    elif c == "help":
        ajuda()

    elif c == "exit":
        break

    else:
        print("Comando desconhecido.")