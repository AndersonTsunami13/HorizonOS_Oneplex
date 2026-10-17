import tkinter as tk
import time

bios_version_system = "V1.0"
RAM_TOTAL = 4096

neo = r"""
 /\_/\\
( o.o )
 > ^ <
"""

# =========================================
# BIOS
# =========================================

def boot_sequence(main_root=None):

    # =========================================
    # SISTEMA DE JANELA
    # =========================================

    criado_localmente = False

    if main_root is None:
        main_root = tk.Tk()
        main_root.withdraw()
        criado_localmente = True

    bios = tk.Toplevel(main_root)

    bios.title("Horizon Megatrends")
    bios.attributes("-fullscreen", True)
    bios.configure(bg="black")

    # =========================================
    # FINALIZAR
    # =========================================

    def finalizar():
        bios.destroy()

        if criado_localmente:
            main_root.destroy()

    # =========================================
    # TERMINAL
    # =========================================

    terminal = tk.Text(
        bios,
        bg="black",
        fg="#00ff00",
        insertbackground="#00ff00",
        font=("Consolas", 14),
        bd=0
    )

    terminal.pack(fill="both", expand=True)

    # =========================================
    # ESCREVER TEXTO
    # =========================================

    def escrever(texto, delay=0.02, quebra=True):

        for letra in texto:
            terminal.insert("end", letra)
            terminal.see("end")
            bios.update()
            time.sleep(delay)

        if quebra:
            terminal.insert("end", "\n")
            terminal.see("end")

    # =========================================
    # BARRA DE CARREGAMENTO
    # =========================================

    def barra_carregando(tamanho=40):

        terminal.insert("end", "\n[")

        for _ in range(tamanho):
            terminal.insert("end", "█")
            terminal.see("end")
            bios.update()
            time.sleep(0.05)

        terminal.insert("end", "] OK\n\n")

    # =========================================
    # INÍCIO DA BIOS
    # =========================================

    escrever("    (◔‿◔) Horizon Megatrends - New Era", 0.01)
    escrever(f"    ( ͡° ͜ʖ ͡°) BIOS {bios_version_system}", 0.01)
    escrever("    ಠ_ಠ Copyright (C) 2024-2026\n", 0.01)

    escrever(neo, 0.001)

    escrever("Deseja entrar no Setup? [S/N]\n", 0.01)

    entrada = tk.Entry(
        bios,
        bg="black",
        fg="#00ff00",
        insertbackground="#00ff00",
        font=("Consolas", 14),
        bd=0
    )

    terminal.window_create("end", window=entrada)
    terminal.insert("end", "\n")

    # =========================================
    # RESPOSTA
    # =========================================

    def responder(event=None):

        resposta = entrada.get().lower().strip()

        entrada.destroy()

        # =====================================
        # SETUP
        # =====================================

        if resposta == "s":

            escrever("\nEntrando no setup...", 0.02)

            time.sleep(1)

            escrever("\n[ Horizon BIOS Setup Utility ]", 0.01)
            escrever("----------------------------------", 0.01)
            escrever("CPU: Horizon Quantum Core", 0.01)
            escrever(f"RAM: {RAM_TOTAL}MB", 0.01)
            escrever("Secure BIOS: ENABLED", 0.01)
            escrever("Developer Mode: OFF", 0.01)

            escrever("\nPressione ENTER para continuar...", 0.01)

            entrada2 = tk.Entry(
                bios,
                bg="black",
                fg="#00ff00",
                insertbackground="#00ff00",
                font=("Consolas", 14),
                bd=0
            )

            terminal.window_create("end", window=entrada2)

            def sair_setup(event=None):
                finalizar()

            entrada2.bind("<Return>", sair_setup)
            entrada2.focus()

        # =====================================
        # BOOT NORMAL
        # =====================================

        else:

            escrever("\nCerto! Aguarde...\n", 0.02)

            escrever("> DevMessage:")
            escrever("~" * 50)
            escrever("A BIOS agora suporta modificações via sistema")
            escrever("~" * 50)

            escrever("\nInitializing hardware...", 0.02)
            time.sleep(0.5)

            escrever("Detecting drives...", 0.02)
            time.sleep(0.5)

            escrever("C: Fixed Disk Drive", 0.02)
            time.sleep(0.3)

            escrever("D: CD-ROM Drive", 0.02)
            time.sleep(0.3)

            escrever(f"Memory Test: {RAM_TOTAL}MB OK", 0.02)
            time.sleep(0.5)

            escrever("Loading Operating System...", 0.02)

            barra_carregando()

            escrever("Boot complete.", 0.02)

            bios.after(1500, finalizar)

    entrada.bind("<Return>", responder)
    entrada.focus()

    # =========================================
    # MAINLOOP
    # =========================================

    bios.mainloop()