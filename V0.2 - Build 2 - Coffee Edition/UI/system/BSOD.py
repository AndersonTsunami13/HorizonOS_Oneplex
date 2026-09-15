import os
import shutil
import sys
from colorama import init, Fore, Back, Style

init()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def bsod():
    # Descobre o tamanho atual do terminal
    terminal = shutil.get_terminal_size()
    width = terminal.columns
    height = terminal.lines

    # Limpa a tela
    clear_screen()

    # Cor da BSOD
    sys.stdout.write(Back.BLUE + Fore.WHITE)

    # Preenche toda a tela com azul
    for _ in range(height):
        sys.stdout.write(" " * width + "\n")

    # Volta para o canto superior esquerdo
    sys.stdout.write("\033[H")

    texto = [
        "A problem has been detected and Windows has been shut down",
        "to prevent damage to your computer.",
        "",
        "If this is the first time you've seen this Stop error screen,",
        "restart your computer. If this screen appears again, follow",
        "these steps:",
        "",
        "Check to make sure any new hardware or software is properly",
        "installed. If this is a new installation, ask your hardware",
        "or software manufacturer for any Windows updates you might",
        "need.",
        "",
        "If problems continue, disable or remove any newly installed",
        "hardware or software. Disable BIOS memory options such as",
        "caching or shadowing. If you need to use Safe Mode to remove",
        "or disable components, restart your computer, press F8 to",
        "select Advanced Startup Options, and then select Safe Mode.",
        "",
        "Technical information:",
        "",
        "*** STOP: 0x0000007B (0xF7C7A524, 0xC0000034,",
        "0x00000000, 0x00000000)"
    ]

    # Limita o texto à largura disponível
    for linha in texto:
        sys.stdout.write(linha[:width - 1] + "\n")

    # Mantém a tela aberta
    sys.stdout.write("\n" * max(0, height - len(texto) - 2))
    sys.stdout.write("Press ENTER to restart...")
    sys.stdout.flush()

    input()

    # Restaura o terminal
    sys.stdout.write(Style.RESET_ALL)
    clear_screen()


if __name__ == "__main__":
    bsod()