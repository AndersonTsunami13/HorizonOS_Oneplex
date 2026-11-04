import tkinter as tk

bios_name = "HorizonOS BIOS"
bios_version_system = "v0.3 - Build 3 - Midnight Revolution Edition"
copyright_horizon = "2024 HorizonOS. All rights reserved."

RAM_TOTAL = 512

CORES = {
    "fundo": "#02020a",
    "texto": "#ffffff",
}

LINHAS_BIOS = [
    f"{bios_name}",
    f"BIOS {bios_version_system}",
    f"Copyright (C) {copyright_horizon}",
    "",
    "Initializing hardware...",
    "Detecting drives...",
    "C: Fixed Disk Drive",
    "D: CD-ROM Drive",
    f"Memory Test: {RAM_TOTAL}MB OK",
    "",
    "Loading Operating System...",
]

indice = 0
texto_bios = ""

root = None
canvas = None
item_texto = None


def mostrar_linha():
    global indice, texto_bios

    if indice >= len(LINHAS_BIOS):
        if indice >= len(LINHAS_BIOS):
            root.after(1000, root.destroy)
        return

    texto_bios += LINHAS_BIOS[indice] + "\n"

    canvas.itemconfig(item_texto, text=texto_bios)

    indice += 1

    root.after(1000, mostrar_linha)


def bios_sequence():
    global root, canvas, item_texto

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg=CORES["fundo"])
    root.title("HorizonOS BIOS")

    root.bind("<Escape>", lambda e: root.destroy())

    canvas = tk.Canvas(
        root,
        bg=CORES["fundo"],
        highlightthickness=0
    )
    canvas.pack(fill="both", expand=True)

    item_texto = canvas.create_text(
        20,
        20,
        anchor="nw",
        fill=CORES["texto"],
        font=("Consolas", 18),
        text=""
    )

    mostrar_linha()

    root.mainloop()


if __name__ == "__main__":
    bios_sequence()