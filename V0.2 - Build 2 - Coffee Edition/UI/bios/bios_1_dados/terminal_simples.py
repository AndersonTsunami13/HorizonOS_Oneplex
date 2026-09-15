# terminal_simples.py

from Engine.UI_Engine_ConsoleX import escrever, limpar

def terminal_simples():
    usuario = input("Digite seu nome:")
    limpar()
    escrever(f"Bem-vindo, {usuario}, ao Mini HorizonOS Terminal!\n")
    escrever("Comandos disponíveis:")
    escrever("  ls     → listar arquivos")
    escrever("  cd     → mudar de pasta")
    escrever("  mkdir  → criar pasta")
    escrever("  touch  → criar arquivo")
    escrever("  cat    → mostrar arquivo")
    escrever("  exit   → sair do terminal\n")
    diretorio_atual = {"nome": "/", "conteudo": {}}
    path = [diretorio_atual]

    while True:
        cmd = input(f"{usuario}@horizon:{'/'.join([d['nome'] for d in path])}$ ").strip().split()
        if not cmd:
            continue
        if cmd[0] == "exit":
            escrever("Saindo do Mini HorizonOS...")
            break
        elif cmd[0] == "ls":
            atual = path[-1]
            escrever("  ".join(atual["conteudo"].keys()) or "(vazio)")
        elif cmd[0] == "mkdir":
            if len(cmd) < 2:
                escrever("Digite o nome da pasta!")
            else:
                path[-1]["conteudo"][cmd[1]] = {"nome": cmd[1], "conteudo": {}}
                escrever(f"Pasta '{cmd[1]}' criada.")
        elif cmd[0] == "touch":
            if len(cmd) < 2:
                escrever("Digite o nome do arquivo!")
            else:
                path[-1]["conteudo"][cmd[1]] = {"nome": cmd[1], "conteudo": ""}
                escrever(f"Arquivo '{cmd[1]}' criado.")
        elif cmd[0] == "cat":
            if len(cmd) < 2:
                escrever("Digite o nome do arquivo!")
            else:
                arquivo = cmd[1]
                atual = path[-1]["conteudo"]
                if arquivo in atual and isinstance(atual[arquivo], dict):
                    escrever(f"'{arquivo}' é uma pasta, não um arquivo!")
                elif arquivo in atual:
                    escrever(atual[arquivo]["conteudo"])
                else:
                    escrever("Arquivo não encontrado.")
        elif cmd[0] == "cd":
            if len(cmd) < 2:
                escrever("Digite o destino!")
            else:
                destino = cmd[1]
                if destino == "..":
                    if len(path) > 1:
                        path.pop()
                elif destino in path[-1]["conteudo"] and isinstance(path[-1]["conteudo"][destino], dict):
                    path.append(path[-1]["conteudo"][destino])
                else:
                    escrever("Pasta não encontrada.")

# Anderson_Tsunami.M3_E36