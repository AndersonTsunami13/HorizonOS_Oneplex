# debug1.py

from Information.info import *
from Information.dados import *
from Information.devmode import *

from Engine.UI_Engine_ConsoleX import escrever, enter, limpar, titulo_console, input_silencioso, time_s, cursor

def debug1(): # Information/info.py
    titulo_console("Debug - Information/info.py")

    limpar()

    cursor(False)

    escrever(f"""
===== Sistema de Dados HNDX =====

>>> Senhas
senha_bios = {senha_bios}
senha_devmode = {senha_devmode}

# >>> Desenvolvedor
name_DEV = {name_DEV}
limpar_on = {limpar_on}
COLORAMA_OK = {COLORAMA_OK}
limite_tentativas = {limite_tentativas}
time_e = {time_e}

# ---------- Informações do Sistema ----------
name_system = {name_system}
versao_system = {versao_system}
name_ui = {name_ui}
versao_ui = {versao_ui}
bios_version_system = {bios_version_system}
versao_engine_console = {versao_engine_console}        
debug_version = {debug_version}

# ---------- Controle de Permissões ----------
enable_bios_access = {enable_bios_access}
modo_dev = {modo_dev}
command_kill = {command_kill}

# ---------- Arquivo de Dados ----------
LOG_FILE = {LOG_FILE}

# ---------- Pastas ----------
PASTA_PROJETOS = {PASTA_PROJETOS}

# ---------- NameTegs do Sistema ----------
# NameTeg padrão do usuário
name_tegs_system = {name_tegs_system}

# NameTegs para DevMode
name_tegs_system_dev = {name_tegs_system_dev}    
""", velocidade=0.01)
    
    cursor(True)
    enter()

# Anderson_Tsunami.11Xx