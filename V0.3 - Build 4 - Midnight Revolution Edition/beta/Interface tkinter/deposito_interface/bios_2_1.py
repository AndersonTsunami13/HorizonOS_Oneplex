import tkinter as tk
import time

# =========================================
# Horizon BIOS - America Megatrends Style
# =========================================

bios_version = "V1.0"
RAM_TOTAL = 4096

# =========================================
# JANELA
# =========================================

root = tk.Tk()

root.title("American Megatrends")
root.attributes("-fullscreen", True)
root.configure(bg="#0000AA")  # azul BIOS clássico

# =========================================
# ÁREA DE TEXTO
# =========================================

terminal = tk.Text(
    root,
    bg="#0000AA",
    fg="white",
    insertbackground="white",
    font=("Courier New", 14),
    bd=0
)

terminal.pack(fill="both", expand=True)

# =========================================
# ESCREVER
# =========================================

def escrever(texto="", delay=0.01):

    for letra in texto:
        terminal.insert("end", letra)
        terminal.see("end")
        root.update()
        time.sleep(delay)

    terminal.insert("end", "\n")

# =========================================
# BARRA DE LOAD
# =========================================

def barra():

    terminal.insert("end", "[")

    for i in range(30):

        terminal.insert("end", "■")
        terminal.see("end")
        root.update()

        time.sleep(0.05)

    terminal.insert("end", "]\n")

# =========================================
# BIOS
# =========================================

def bios_sequence_2():

    escrever("American Megatrends, Inc.")
    escrever(f"BIOS Revision {bios_version}")
    escrever("Copyright (C) 2024-2026")
    escrever("")

    escrever("CPU : Horizon Quantum Processor")
    escrever(f"Memory Test : {RAM_TOTAL}MB OK")
    escrever("Detecting IDE Drives ...")
    escrever("SATA Port 0 : Horizon SSD 256GB")
    escrever("USB Device(s) : 2 Keyboard, 1 Mouse")
    escrever("")

    escrever("Press DEL to run Setup")
    escrever("Press F8 for Boot Menu")
    escrever("")

    time.sleep(1)

    escrever("Initializing Horizon Hardware...")
    escrever("Checking system integrity...")
    escrever("Loading HorizonOS Professional XWin One...")
    escrever("")

    barra()

    escrever("")
    escrever("Boot successful.")
    escrever("Starting HorizonUI Z1...")
    escrever("")
    escrever("Welcome.")

# =========================================
# START
# =========================================

root.after(500, bios_sequence_2)

root.mainloop()