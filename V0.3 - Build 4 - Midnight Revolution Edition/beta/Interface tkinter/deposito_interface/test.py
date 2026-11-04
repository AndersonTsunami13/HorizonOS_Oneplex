import tkinter as tk

from UI_TitleBar import *

root = tk.Tk()

root.geometry("900x500")
root.configure(bg="#1e1e1e")

criar_titlebar(root, "HorizonOS Professional")

set_status("Conectado ao HorizonNet")

root.after(3000, lambda: set_erro("config.sys não encontrado"))

root.after(6000, lambda: set_sucesso("Sistema reparado"))

root.mainloop()