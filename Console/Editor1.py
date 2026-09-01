import os

PASTA_PROJETOS = "Projetos"

# =========================
# SISTEMA BASE
# =========================

if not os.path.exists(PASTA_PROJETOS):
    os.makedirs(PASTA_PROJETOS)

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def escrever(texto):
    print(texto)

# =========================
# EDITOR
# =========================

def editor():

    limpar()

    escrever("=== Horizon Editor ===")

    nome_arquivo = input("Nome do arquivo: ")

    caminho = os.path.join(PASTA_PROJETOS, nome_arquivo)

    escrever("\nDigite seu código.")
    escrever("Use ::salvar para finalizar.\n")

    linhas = []

    while True:

        linha = input()

        if linha.strip() == "::salvar":
            break

        linhas.append(linha)

    with open(caminho, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))

    escrever(f"\nArquivo salvo em: {caminho}")

# =========================
# EXECUTAR ARQUIVO
# =========================

def rodar_arquivo():

    arquivos = os.listdir(PASTA_PROJETOS)

    if not arquivos:
        escrever("Nenhum arquivo encontrado.")
        return

    escrever("\n=== Arquivos ===")

    for i, arq in enumerate(arquivos):
        escrever(f"{i+1} - {arq}")

    try:

        idx = int(input("\nNúmero do arquivo: ")) - 1

        caminho = os.path.join(PASTA_PROJETOS, arquivos[idx])

        escrever(f"\nExecutando {arquivos[idx]}...\n")

        os.system(f'python "{caminho}"')

    except:
        escrever("Arquivo inválido.")

# =========================
# DELETAR
# =========================

def deletar_arquivo():

    arquivos = os.listdir(PASTA_PROJETOS)

    if not arquivos:
        escrever("Nenhum arquivo encontrado.")
        return

    escrever("\n=== Arquivos ===")

    for i, arq in enumerate(arquivos):
        escrever(f"{i+1} - {arq}")

    try:

        idx = int(input("\nNúmero do arquivo: ")) - 1

        caminho = os.path.join(PASTA_PROJETOS, arquivos[idx])

        os.remove(caminho)

        escrever("Arquivo deletado.")

    except:
        escrever("Arquivo inválido.")

# =========================
# HUB
# =========================

def hub():

    while True:

        limpar()

        escrever("=== Horizon Hub ===\n")

        escrever("[1] Criar arquivo")
        escrever("[2] Rodar arquivo")
        escrever("[3] Deletar arquivo")
        escrever("[4] Sair")

        escolha = input("\n> ")

        if escolha == "1":
            editor()

        elif escolha == "2":
            rodar_arquivo()

        elif escolha == "3":
            deletar_arquivo()

        elif escolha == "4":
            break

        input("\nPressione ENTER...")

# =========================
# START
# =========================

if __name__ == "__main__":
    hub()