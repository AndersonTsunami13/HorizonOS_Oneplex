# UI/bios.py

import time

from Engine.UI_Engine_ConsoleX import escrever, limpar, enter, pular_linha, perguntar, time_s, loading1, loading3, loading5, loading7
from Kernel.hardware import *
from Information.info import *
from Information.dados import assist
from Information.devmode import *

from UI.bios.bios_1_dados.beta_painel import beta_painel
from UI.bios.bios_1_dados.console_bios import console_bios
from UI.bios.bios_1_dados.terminal_simples import terminal_simples

# ==== bios ====
def bios_sequence():
    limpar()

    escrever(f"""
//    Horizon Megatreads - New era
//    BIOS {bios_version_system}
//    Copyright (C) 2024-2026
""", "MAGENTA", "destaque", "BLACK")

    if bios_message:
        escrever(assist)
        escrever("Deseja entra nas configurações da BIOS? (S/N)", "YELLOW")
        resposta = perguntar("> ", cor="YELLOW", xy=False)
        if resposta in ["S", "s"]:
            pular_linha()
            loading3(3, "Entrando no setup...")
            bios_system_0()
        elif resposta in ["N", "n"]:
            pular_linha()
            loading3(3, "Certo! Aguarde...")
            pular_linha()
        else:
            escrever("Comando nao reconhecido! tente novamente.", "RED")
            time_s(1)
            bios_sequence()
    else:
        pular_linha()
        
    if dev_message:
        escrever("> DevMessage:")
        escrever("O modo dev está chegando...", "GREEN")
        pular_linha()
    else:
        pular_linha()

    loading5(3, "Initializing hardware", "GREEN")
    if PORT_message:
        loading1("Detecting drives")

        loading5(4, "A: Disquete Drive ", "YELLOW")
        escrever("Failed!", cor="RED", mesma_linha=True)
        pular_linha()
        loading5(4, "B: Memory Card ", "YELLOW")
        escrever("Error!", "RED", mesma_linha=True)
        pular_linha()
        loading5(4, "C: Fixed Disk Drive ", "YELLOW")
        escrever("Ok!", "GREEN", mesma_linha=True)
        pular_linha()
        loading5(4, "D: CD-ROM Drive ", "YELLOW")
        escrever("Error!", "RED", mesma_linha=True)
        pular_linha()
        loading5(4, "Memory Test: ", "YELLOW")
        escrever(f"{RAM_TOTAL}MB OK", "GREEN", mesma_linha=True)
    else:
        pular_linha()

    pular_linha()
    escrever("Loading Operating System")
    loading7(10)
    pular_linha()
    loading5(3, "iniciando", "GREEN")
    time.sleep(0.4)
            
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
    loading5(3, "Carregando informações", "GREEN")
    loading5(3, "Verificando informacoes de seguranca", "BLUE")
    if enable_bios_access:
        escrever("Permissao ativada!", "GREEN")
        loading5(3, "Aguarde", "YELLOW")
        bios_system()
    else:
        escrever("\nfuncao indisponivel!", "RED")
        enter()

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
    resposta = input("> ")
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

# Anderson_Tsunami.M3_E36