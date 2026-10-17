# versao.py

from Information.info import *
from Engine.MDL_escrever import mdl_escrever as escrever

def f_versao(argumento):
    escrever(f"""
        Nome do sistema:           {name_system}
        Versão do sistema:         {versao_system}
        Build do sistema:          {build_system}

        Nome da interface:         {name_ui}
        Versão da interface:       {versao_ui}

        Versão da BIOS:            {bios_version_system}
        Nome da BIOS:              {bios_name}

        Versão da engine:          {versao_engine_console}
        Versão do DEBUG:           {debug_version}

        copyright:                 {copyright_horizon}
    """, velocidade=0.01)