# ==========================================
# HorizonOS Professional XWin One
# Exemplo de sistema JSON (Planejamento v0.3)
# ==========================================

import json
import os

ARQUIVO = "usuario.json"


# ---------------------------
# Criar arquivo padrão
# ---------------------------

def criar_padrao():
    dados = {
        "usuario": "Administrador",
        "senha_hash": "",
        "tema": "escuro",
        "volume": 80,
        "animacoes": True
    }

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            dados,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


# ---------------------------
# Carregar dados
# ---------------------------

def carregar():
    if not os.path.exists(ARQUIVO):
        criar_padrao()

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


# ---------------------------
# Salvar dados
# ---------------------------

def salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            dados,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


# ---------------------------
# Exemplo de uso
# ---------------------------

dados = carregar()

print("\n=== HORIZONOS ===")
print("Usuário:", dados["usuario"])
print("Tema:", dados["tema"])
print("Volume:", dados["volume"])

# Alterações em memória
dados["tema"] = "azul"
dados["volume"] = 50

# Salvar alterações
salvar(dados)

print("\nConfigurações atualizadas!")