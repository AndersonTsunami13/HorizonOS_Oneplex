# UI/bios.py

import time

from Engine.UI_Engine_ConsoleX import escrever, limpar, enter, escrever_loading, pular_linha, cursor
from Kernel.hardware import *
from Information.info import *
from Information.dados import *
from Information.devmode import *
from UI.anim.loading import loading

# ==== bios ====
def bios_sequence():
    limpar()

    escrever(f"""
    Horizon Megatrends - New Era
    BIOS {bios_version_system}
    Copyright (C) 2024-2026
""", "BLUE", "destaque", "BLACK")

    if bios_message:
        escrever(assist)
        escrever("Deseja entrar no Setup? S ou N", "YELLOW")
        resposta = input("> ")
        if resposta in ["S", "s"]:
            pular_linha()
            escrever_loading(3, "Entrando no setup")
            bios_system_0()
        elif resposta in ["N", "n"]:
            pular_linha()
            escrever_loading(3, "Certo! Aguarde")
        else:
            escrever("Comando nao reconhecido! tente novamente.", "RED")
            time.sleep(1)
            bios_sequence()
    else:
        pular_linha()
        
    if dev_message:
        escrever("> DevMessage:")
        escrever("A bios agora tem suporte a modificacoes direto do sistema", "GREEN")
        pular_linha()
    else:
        pular_linha()

    loading("Initializing hardware")
    if PORT_message:
        escrever_loading(1, "Detecting drives", "GREEN")
        escrever("C: Fixed Disk Drive", "GREEN")
        escrever("D: CD-ROM Drive", "GREEN")
        escrever(f"Memory Test: {RAM_TOTAL}MB OK", "GREEN")
    else:
        pular_linha()

    pular_linha()
    escrever_loading(1, "Loading Operating System", "YELLOW")
    loading("iniciando")
    time.sleep(0.4)

def beta_painel():
    while True:
        limpar()
        escrever("Bem-vindo ao painel de recursos betas do HorizonOS Professional XWin One", "RED")
        escrever("\n    Os recursos sao para fazer testes, se não tiver necessidade não use eles aqui! eles serão liberados assim que possível pro sistema clean.", "YELLOW")
        escrever("\nEscolha o recuso que você deseja usar:", "BLUE")
        escrever("1. O relógio fantasma (Ghost clock)")
        escrever("2. A nova linguagem do Horizon (HotScript)")
        escrever("3. o teste de multitarefas (vários processos abertos na mesma janela")
        r = input(">")
        
        if r == "1":
            time.sleep(1)
            #Ghost_Clock()
        elif r == "2":
            time.sleep(1)
           # Hotlinguage()
        elif r == "3":
            time.sleep(1)
           # test1()
        else:
            escrever("[NEO] Esse comando não e o certo nobre!")
            input("Pressione enter pra continuar...")
            
def formatar_tempo(segundos):
    # Cálculos matemáticos para converter segundos
    dias = segundos // 86400
    horas = (segundos % 86400) // 3600
    minutos = (segundos % 3600) // 60
    seg_restantes = segundos % 60
    
    # Criando a lista de partes para o texto
    partes = []
    if dias > 0:
        partes.append(f"{dias}d")
    if horas > 0:
        partes.append(f"{horas}h")
    if minutos > 0:
        partes.append(f"{minutos}m")
    if seg_restantes > 0 or not partes:
        partes.append(f"{seg_restantes}s")
        
    return " ".join(partes)
    
            
def bios_system_0():
    limpar()
    escrever("Carregando informações...", "GREEN")
    time.sleep(0.8)
    escrever("Verificando informacoes de seguranca...", "BLUE")
    time.sleep(0.3)
    if enable_bios_access:
        escrever("Permissao ativada!", "GREEN")
        escrever("Aguarde...")
        time.sleep(0.3)
        bios_system()
    else:
        escrever("\nfuncao indisponivel!", "RED")
 
def console_bios():
    while True:
        limpar()
        escrever("O console por enquanto está desativado! digite exit para sair!")
        r = input(">")
        if r == "Console:EnableBeta":
            beta11 = "true"
            escrever("Recursos Beta ativado!", "GREEN")
            console_bios()
        elif r == "Console:Beta.TestMemoryCard":
            escrever("O recuso do Memory Card!", "YELLOW")
            try:
              #  mc = MemoryCard()
                escrever("Memory card inserido", "GREEN")
            except:
                escrever("Erro ao montar o memory card!", "RED")
        elif r == "exit":
            break
        else:
            escrever("Comando não reconhecido! tente novamente.", "RED")
            input()
     
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

def bios_system():
    limpar()
    escrever("/" * 75, "GREEN")
    escrever(f"Horizon Megatrends    BIOS {bios_version_system}    Copyright (C) 2024-2026    BIOS System", "BLUE")
    escrever("/" * 75, "GREEN")
    escrever("\n[System] A BIOS está ligada ao sistema.")
    escrever("\n ~~~ Control Center ~~~")
    escrever("[1] Console")
    escrever("[2] Hora e Data")
    escrever("[3] Informações do Sistema")
    escrever("[4] Terminal Simples")
    escrever("[5] Beta painel")
    escrever("[6] Voltar")
    resposta = input(">")
    if resposta == "1":
        console_bios()
    elif resposta == "2":
        hora = time.strftime(f"%H:%M:%S")
        data = time.strftime(f"%d/%m/%Y")
        uptime_segundos = int(time.time() - inicio_sistema)
        escrever(f"Hora atual: {hora}", "CYAN")
        escrever(f"Data atual: {data}", "CYAN")
        escrever(f"Iniciado às: {time.strftime('%H:%M:%S', time.localtime(inicio_sistema))}", "CYAN")
        escrever(f"Tempo ligado: {formatar_tempo(uptime_segundos)}", "CYAN")
        enter()
        bios_system()
    elif resposta == "3":
        escrever("\nCarregando informações do sistema...", "BLUE")
        time.sleep(0.7)
        escrever(f"Nome do Sistema: {name_system}")
        escrever(f"Versão do Sistema: {versao_system}")
        escrever(f"Versão da UI: {versao_ui}")
        escrever(f"Dev: {name_DEV}")
        escrever(f"bios segure: {enable_bios_access}")
        escrever(f"Modo DEV: {modo_dev}")
        enter()
        bios_system()
    elif resposta == "4":
        terminal_simples()
    elif resposta == "5":
        beta_painel()
    elif resposta == "6":
        bios_sequence()
    else:
        escrever("Comando não reconhecido. tente novamente!")
        enter() 
        bios_system()