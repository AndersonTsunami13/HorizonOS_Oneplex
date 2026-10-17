# securitymodule_verification.py

import hashlib

def gerar_hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

def verificar_senha(senha, hash_salvo):
    return gerar_hash(senha) == hash_salvo
    
"""
hash_bios = "hash_salvo_aqui"

senha = input("Senha: ")

if verificar_senha(senha, hash_bios):
    print("Inicializando HorizonOS...")
else:
    print("Acesso negado!")
"""
# Anderson_Tsunami.11Xx