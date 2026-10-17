import tkinter as tk

from Information.WinConfig import *

# =============================
# Função de inicialização (Tela de Boot)
# =============================

def boot_sequence_1():
    boot_window = tk.Tk()
    boot_window.configure(bg=TEMA_FUNDO_INI) 
    boot_window.attributes("-fullscreen", True)
    boot_window.title(f"{NAME_SYSTEM} {VERSAO_HORIZON_2}")

    logo = tk.Label(boot_window,
                    text= f"{NAME_SYSTEM}",
                    font=(f"{FONT_TEXTO}", (FONT_TEXTO_VALOR_1)),
                    fg=f"{TEMA_TEXTO_1}",
                    bg=f"{TEMA_CONTORNO_INI}")
    logo.pack(pady=200)

    mensagem_1 = tk.Label(boot_window, text=f"Base: {VERSAO_BASE}",
                          font=(f"{FONT_TEXTO}", 10), fg=f"{TEMA_TEXTO_1}", bg=f"{TEMA_CONTORNO_INI}")
    mensagem_1.place(x=10, y=10)

    mensagem_2 = tk.Label(boot_window, text=f"Inicializando {NAME_SYSTEM}...",
                          font=(f"{FONT_TEXTO}", 10), fg=f"{TEMA_TEXTO_1}", bg=f"{TEMA_CONTORNO_INI}")
    mensagem_2.place(x=10, y=30)

    mensagem_3 = tk.Label(boot_window, text="Isso pode demorar um pouco!",
                          font=(f"{FONT_TEXTO}", 10), fg=f"{TEMA_TEXTO_1}", bg=f"{TEMA_CONTORNO_INI}")
    mensagem_3.place(x=10, y=50)

    mensagem_4 = tk.Label(boot_window, text=f"versao {VERSAO_HORIZON_2}",
                          font=(f"{FONT_TEXTO}", 10), fg=f"{TEMA_TEXTO_1}", bg=f"{TEMA_CONTORNO_INI}")
    mensagem_4.place(x=10, y=70)

    loading_text = tk.Label(boot_window, text=f"{TEXTO_CARREGANDO_INI}", font=(f"{FONT_TEXTO}", (FONT_TEXTO_VALOR_2)), fg=f"{TEMA_TEXTO_1}", bg=f"{TEMA_CONTORNO_INI}")
    loading_text.pack(pady=10)

    progress_bar = tk.Canvas(boot_window, width=900, height=10, bg=f"{TEMA_FUNDO_INI}")
    progress_bar.pack(pady=10)
    progress = progress_bar.create_rectangle(0, 0, 0, 20, fill=f"{TEMA_CARREGANDO}")

    def update_progress():
        def step(i):
            progress_bar.coords(progress, 0, 0, i, 10)
            boot_window.update()

            # Se a barra não chegou ao máximo, chama a função step novamente
            if i < 900:
                boot_window.after((TEMPO_INI), step, i + 1)  # A cada 10ms, chama o step com o próximo valor
            else:
                boot_window.destroy()  # Quando chegar ao fim, fecha a janela

        step(0)  # Inicia o processo com 0%

    update_progress()
    boot_window.mainloop()