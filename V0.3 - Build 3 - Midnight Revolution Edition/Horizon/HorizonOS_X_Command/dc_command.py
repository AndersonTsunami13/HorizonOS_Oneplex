# dc_command.py

# Esse arquivo é responsavel por guardar toda as ações dos comandos.

from .Commands.tempo import f_tempo
from .Commands.mostrar_ajuda import f_mostrar_ajuda
from .Commands.versao import f_versao
from .Commands.reiniciar import f_reiniciar
from .Commands.hora import f_hora
from .Commands.data import f_data
from .Commands.echo import f_echo
from .Commands.desligar import f_desligar
from .Commands.bsod import f_bsod
from .Commands.files_manager import f_listar, f_entrar, f_local, f_criar, f_ler, f_remover, f_arquivos
from .Commands.hardware import f_hardware, f_ram, f_disco, f_cpu, f_vram, f_rede
from .Commands.processos import f_processos
from .Commands.config import f_config
from .Commands.logs import f_logs
from .Commands.limpar import f_limpar
from .Commands.info import f_info
from .Commands.kill import f_kill
from .Commands.dynamicbar import f_dynamic_bar_start, f_dynamic_bar, f_dynamic_bar_finish
from .Commands.statusbar import f_status_bar_system_start, f_status_bar_system, f_status_bar_system, f_status_bar_system_finish, f_status_bar_log_start, f_status_bar_log, f_status_bar_log_finish, f_status_bar_message_start, f_status_bar_message, f_status_bar_message_finish
from .Commands.meu_pc import f_meu_pc
from .Commands.calculadora import f_calculadora
from .Commands.assistente import f_assistente
from .Commands.S8E import f_S8E
from .Commands.memory_scanner import f_memory_scanner
from .Commands.byte_inspector import f_byte_inspector
from .Commands.pydocs import f_pydocs
from .Commands.editor import f_editor
from .Commands.minerador import f_minerador
from .Commands.navegador import f_navegador
from .Commands.update_system import f_update_system
from .Commands.quebrador_senha import f_quebrador_senha
from .Commands.quebrador_numero import f_quebrador_numero
from .Commands.createpassword import f_createpassword, f_createpassword2
from .Commands.chuva import f_chuva
from .Commands.relogio import f_relogio1, f_relogio2, f_relogio3
from .Commands.ghost_clock import f_ghost_clock

# Dicionário
comandos = {

    "ajuda":f_mostrar_ajuda,
    "tempo":f_tempo,
    "versao":f_versao,
    "reiniciar":f_reiniciar,
    "hora":f_hora,
    "data":f_data,
    "echo":f_echo,
    "desligar":f_desligar,
    "bsod":f_bsod,
    "listar":f_listar,
    "entrar":f_entrar,
    "local":f_local,
    "criar":f_criar,
    "ler":f_ler,
    "remover":f_remover,
    "arquivos":f_arquivos,
    "hardware":f_hardware,
    "ram":f_ram,
    "disco":f_disco,
    "cpu":f_cpu,
    "vram":f_vram,
    "rede":f_rede,
    "processos":f_processos,
    "config":f_config,
    "logs":f_logs,
    "limpar":f_limpar,
    "info":f_info,
    "/kill":f_kill,
    "dynamic_bar_start":f_dynamic_bar_start,
    "dynamic_bar":f_dynamic_bar,
    "dynamic_bar_finish":f_dynamic_bar_finish,
    "status_bar_system_start":f_status_bar_system_start,
    "status_bar_system":f_status_bar_system,
    "status_bar_system_finish":f_status_bar_system_finish,
    "status_bar_log_start":f_status_bar_log_start,
    "status_bar_log":f_status_bar_log,
    "status_bar_log_finish":f_status_bar_log_finish,
    "status_bar_message_start":f_status_bar_message_start,
    "status_bar_message":f_status_bar_message,
    "status_bar_message_finish":f_status_bar_message_finish,
    "meu_pc":f_meu_pc,
    "calculadora":f_calculadora,
    "assistente":f_assistente,
    "S8E":f_S8E,
    "s8e":f_S8E,
    "memory_scannet":f_memory_scanner,
    "byte_inspector":f_byte_inspector,
    "pydocs":f_pydocs,
    "editor":f_editor,
    "minerador":f_minerador,
    "navegador":f_navegador,
    "update_system":f_update_system,
    "quebrador_senha":f_quebrador_senha,
    "quebrador_numero":f_quebrador_numero,
    "createpassword":f_createpassword,
    "createpassword2":f_createpassword2,
    "chuva":f_chuva,
    "relogio1":f_relogio1,
    "relogio2":f_relogio2,
    "relogio3":f_relogio3,
    "ghost_clock":f_ghost_clock
}

# Anderson_Tsunami_M3_E36