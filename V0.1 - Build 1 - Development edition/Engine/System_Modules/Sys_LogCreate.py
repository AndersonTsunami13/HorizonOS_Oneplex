# log_create.py

# Inportações
import datetime, time, os

from Information.info import LOG_FILE # Inportação do info.py para saber o nome do arquivo.

# Esse modulo é responsavel por criar os logs do sistema.
def escrever_log(texto, log=LOG_FILE):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # pega o tempo atual.

    with open(log, "a") as arquivo:
        arquivo.write(f"[log] - [{agora}] - {texto}\n")     # modelo de escrita do log: 
                                                            # "log.txt - 21/03/2021 11:30:42 - texto do log"

# Anderson_Tsunami.11Xx