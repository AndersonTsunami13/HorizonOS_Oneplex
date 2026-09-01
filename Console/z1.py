import random
import time

caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?!@#$_&-+()/*"
senha = "".join(random.choice(caracteres) for _ in range(10))

for _ in range(987100):
    tentativa = "".join(random.choice(caracteres) for _ in range(10))
    print(f"Testando: {tentativa}")
    if tentativa == senha:
        print("senha encontrada com sucesso!")
        print(f"Senha: {senha}")
    time.sleep(0.05)

print("\nAcesso negado.")