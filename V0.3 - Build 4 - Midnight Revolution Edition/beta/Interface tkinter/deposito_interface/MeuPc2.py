import tkinter as tk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "dados"))
from Information.configapps import *

def abrir_meu_pc():
    janela_pc = tk.Toplevel()
    janela_pc.title("Meu PC")
    janela_pc.geometry("800x600")
    janela_pc.configure(bg=f"{TEMA_FUNDO}")

    label_pc = tk.Label(janela_pc,
                        text="Dispositivos e Unidades (modifique como quiser)\n Isso não ficará salvo!",
                        fg=f"{TEMA_TEXTO_1}",
                        bg=f"{TEMA_FUNDO}",
                        font=("Arial", 14))
    label_pc.pack(pady=10)

    texto_discos = tk.Text(janela_pc, fg="white", bg="#1E1E1E", insertbackground="white",
                           font=("Consolas", 12), height=20, width=60)
    texto_discos.insert("1.0", "'SSD' C:/ Virus_Core.dll/ \n      Anti-virus.rsv \n\n'HDD' D:/ (Esse disco não está acessível.) \n\n'HDD' E: (Unidade não formatada.) \n\n'Disquete' F:/ (Sem driver.) \n\n'Pen drive USB' G:/ \nDispositivos não reconhecidos.")
    texto_discos.pack(pady=10)

    tk.Button(janela_pc, text="Fechar", fg="white", bg=f"{TEMA_FUNDO}", font=("Arial", 12),
              command=janela_pc.destroy).pack(pady=20)
