# Ghost clock "relogio fantasma" V1

# importações
import time
import random

from Engine.UI_Engine_ConsoleX import limpar, titulo_console, time_s, escrever, cursor

# as frases que vão aparecer no relogio
frases = {
    1: "No frio da noite, será que você está sozinho?",
    2: "O tempo passa. Você percebe?",
    3: "Nem toda presença faz barulho.",
    4: "Você confia no silêncio?",
    5: "Enquanto você observa, algo observa você.",
    6: "Ghost, o assistente que te observa no silêncio da madrugada..."
}


def Ghost_Clock():

    largura = 60  # aumenta isso pra ficar bonito

    frase_atual = random.choice(list(frases.values()))
    ultima_troca = time.strftime("%M")

    cursor(False) # desativa o cursor
    try:
        while True:

            limpar() # LImpa a tela

            hora_atual = time.strftime("%H:%M:%S") 
            minuto_atual = time.strftime("%M") # Captura a hora e a data

            # troca frase por minuto
            if minuto_atual != ultima_troca:
                frase_atual = random.choice(list(frases.values()))
                ultima_troca = minuto_atual

            # ==== simplificação =====
            titulo = "========== Ghost Clock =========="
            hora = f"[ {hora_atual} ]"
            # ========================

            titulo_console(f"title Ghost Clock - {hora_atual}")

            # interface
            print("V1 - Ctrl+C para sair...")
            print("\n" * 2)

            print(titulo.center(largura))
            print(hora.center(largura))

            print("\n")

            print(frase_atual.center(largura))

            print("\n" * 2)

            time.sleep(1)


    except KeyboardInterrupt: # Ctrl+c para fechar
        cursor(True) # ativa o cursor denovo
        escrever("\nEncerrando o Ghost Clock... Até logo.")
        time_s(1)

# rodar o teste do ghost clock
if __name__ == "__main__":
    Ghost_Clock()
    
# Anderson_Tsunami.11x