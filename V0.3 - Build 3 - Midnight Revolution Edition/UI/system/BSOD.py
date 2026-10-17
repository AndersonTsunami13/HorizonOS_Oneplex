import os
import shutil
import time

from colorama import init, Fore, Back, Style


init()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def bsod():

    # ==========================================
    # TAMANHO DO TERMINAL
    # ==========================================

    terminal = shutil.get_terminal_size()

    width = terminal.columns
    height = terminal.lines


    # ==========================================
    # LIMPA A TELA
    # ==========================================

    clear_screen()


    # ==========================================
    # PRIMEIRA TELA: AZUL
    # ==========================================

    print(Back.BLUE + Fore.WHITE, end="")

    for _ in range(height):
        print(" " * width)


    # Espera 3 segundos
    time.sleep(3)


    # ==========================================
    # SEGUNDA TELA: VERMELHA
    # ==========================================

    print(Back.RED + Fore.WHITE, end="")

    for _ in range(height):
        print(" " * width)


    # ==========================================
    # VOLTA PARA O TOPO DO TERMINAL
    # ==========================================

    print("\033[H", end="")


    # ==========================================
    # CABEÇALHO
    # ==========================================

    titulo = " HORIZON KERNEL STOP "
    versao = "BSOD V1"

    # Monta a linha inteira
    cabecalho = titulo + " " * max(
        1,
        width - len(titulo) - len(versao)
    ) + versao

    print(
        Back.RED +
        Fore.BLACK +
        cabecalho[:width]
    )


    # ==========================================
    # TEXTO DA TELA
    # ==========================================

    texto = [
        "Um problema foi encontrado e seu sistema teve que parar.",
        "Isso pode prevenir problemas maiores.",
        "",
        "Se essa for a sua primeira vez vendo a tela da morte,",
        "reinicie o sistema e veja se resolve, se não siga essas",
        "três dicas:",
        "",
        "Verifique se o código foi modificado depois da data de",
        "lançamento dessa versão.",
        "Se disponível, atualize seu sistema para a última versão",
        "estável.",
        "Caso você esteja modificando o sistema, verifique o erro",
        "no log do sistema.",
        "",
        "Caso você consiga acessar a BIOS, digite os comandos para",
        "resetar as opções disponíveis.",
        "",
        "Informações técnicas:",
        "",
        "*** Parada: 0x00000000 (0xA0A0A000, 0xA0000000,",
        "0x00000000, 0x00000000)",
        "O código de parada às vezes pode não ser preciso..."
    ]


    # ==========================================
    # ESCREVE O TEXTO
    # ==========================================

    for linha in texto:

        # Impede que o texto ultrapasse a tela
        print(linha[:width - 1])


    # ==========================================
    # ESPAÇO ATÉ O FINAL DA TELA
    # ==========================================

    espacos = max(
        0,
        height - len(texto) - 4
    )

    print("\n" * espacos, end="")


    # ==========================================
    # MENSAGEM DE REINICIALIZAÇÃO
    # ==========================================

    print("Press ENTER to restart...", end="", flush=True)


    # ==========================================
    # AGUARDA ENTER
    # ==========================================

    input()


    # ==========================================
    # RESTAURA O TERMINAL
    # ==========================================

    print(Style.RESET_ALL, end="")

    clear_screen()


# ==========================================
# EXECUÇÃO
# ==========================================

if __name__ == "__main__":
    bsod()
