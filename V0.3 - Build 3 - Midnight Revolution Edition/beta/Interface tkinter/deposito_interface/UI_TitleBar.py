import tkinter as tk
import time
import random

# =====================================
# CONFIG BASE
# =====================================

COR_FUNDO = "#111111"
COR_TEXTO = "white"

COR_INFO = "#00ffaa"
COR_ERRO = "#ff4444"
COR_SUCESSO = "#44ff44"
COR_ALERTA = "#ffaa00"

FONTE = ("Consolas", 10)

# =====================================
# VARIÁVEIS
# =====================================

barra = None
titulo_label = None
status_label = None
relogio_label = None


FRASES = [
    "Frio. Calculado.",
    "Todos os sistemas operacionais.",
    "Silêncio. Eficiência.",
    "Nenhum erro. Nenhuma desculpa.",
    "Precisão acima de tudo.",
    "O sistema observa.",
    "Kernel sincronizado.",
    "Processos sob controle.",
    "Nada além do necessário.",
    "Executando sem hesitar.",
    "Cada ciclo importa.",
    "Menos espera. Mais execução.",
    "Pronto para qualquer comando.",
    "Eficiência é prioridade.",
    "Não desperdice recursos.",
    "Estado: Inabalável.",
    "Pensando em baixo nível.",
    "Boot concluído. Missão iniciada.",
    "Sem promessas. Apenas resultados.",
    "CPU sincronizada.",
    "Memória íntegra.",
    "Kernel operacional.",
    "Cache otimizado.",
    "Threads estáveis.",
    "Clock sincronizado.",
    "Sistema em execução."
]

def atualizar_frase():
    set_status(random.choice(FRASES))
    status_label.after(10000, atualizar_frase)
    
# =====================================
# CRIAR TITLE BAR
# =====================================

def criar_titlebar(root, titulo="HorizonOS"):

    global barra
    global titulo_label
    global status_label
    global relogio_label

    barra = tk.Frame(
        root,
        bg=COR_FUNDO,
        height=30
    )

    barra.pack(fill="x", side="top")

    # ===== TÍTULO =====

    titulo_label = tk.Label(
        barra,
        text=titulo,
        fg=COR_TEXTO,
        bg=COR_FUNDO,
        font=FONTE
    )

    titulo_label.pack(side="left", padx=20)

    # ===== STATUS =====

    status_label = tk.Label(
        barra,
        text="Sistema iniciado",
        fg=COR_INFO,
        bg=COR_FUNDO,
        font=FONTE
    )

    status_label.pack(side="left", padx=20)

    # ===== RELÓGIO =====

    relogio_label = tk.Label(
        barra,
        text="00:00:00",
        fg=COR_TEXTO,
        bg=COR_FUNDO,
        font=FONTE
    )

    relogio_label.pack(side="right", padx=10)

    atualizar_relogio()

# =====================================
# RELÓGIO
# =====================================

def atualizar_relogio():

    hora = time.strftime("%H:%M:%S")

    relogio_label.config(text=hora)

    relogio_label.after(1000, atualizar_relogio)

# =====================================
# FUNÇÕES DE STATUS
# =====================================

def set_titulo(texto):

    titulo_label.config(text=texto)

def set_status(texto):

    status_label.config(
        text=texto,
        fg=COR_INFO
    )

def set_erro(texto):

    status_label.config(
        text=f"⚠ {texto}",
        fg=COR_ERRO
    )

def set_sucesso(texto):

    status_label.config(
        text=f"✔ {texto}",
        fg=COR_SUCESSO
    )

def set_alerta(texto):

    status_label.config(
        text=f"⚠ {texto}",
        fg=COR_ALERTA
    )

# =====================================
# STATUS TEMPORÁRIO
# =====================================

def status_temporario(texto, tempo=3000):

    set_status(texto)

    status_label.after(
        tempo,
        lambda: set_status(random.choice(FRASES))
    )