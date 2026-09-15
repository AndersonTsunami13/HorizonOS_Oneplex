# info.py

from Information.animations import *
from Information.dados import *
from Information.devmode import *
from Information.info import *
from Information.tema import *
from Information.users import *

from Engine.UI_Engine_ConsoleX import escrever

def f_info(argumento):
    escrever(f"""

animations.py

    animações: {animations_enable}

dados.py

    senha (hash): {senha_correta}
    assistente: {assist}
    nome do assistente: {name_assist}
    UI_engine: {UI_ENGINE}
    nome de usuario: {name_user}

devmode.py

    senha do devmode (hash): {senha_devmode}
    nome do desenvolvedor do sistema: {name_DEV}

    limpar: {limpar_on}
    colorama: {COLORAMA_OK}
    limite de tentativa: {limite_tentativas}
    time_e: {time_e}
    bios message: {bios_message}
    dev message: {dev_message}
    PORT message: {PORT_message}
    assist message: {assist_message}
    delay da status bar: {delay_status_bar}

    name teg do modo dev: {name_tegs_system_dev}

info.py

    senha da bios: {senha_bios}

    nome do sistema: {name_system}
    versão do sistema: {versao_system}
    build do sistema: {build_system}

    nome da UI: {name_ui}
    versao da UI: {versao_ui}

    versao da bios: {bios_version_system}
    nome da bios: {bios_name}

    versao da engine: {versao_engine_console}
    versao do debug: {debug_version}

    copyright: {copyright_horizon}

    acesso da bios: {enable_bios_access}
    modo dev: {modo_dev}
    comando da morte: {command_kill}

    arquivo de log:  {LOG_FILE}
    pasta de projetos: {PASTA_PROJETOS}

    name teg do sistema: {name_tegs_system}

    inicio do sistema: {inicio_sistema}

tema.py
    bios screen: {bios_screen}
    boot screen: {boot_screen}

users.py
    usuario logado: {usuario_logado}

    usuarios: {usuarios}
""")