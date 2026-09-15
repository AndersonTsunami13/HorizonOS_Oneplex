import random
import time

r = input("No máximo 24 caracteres\nDigite uma senha: ")
y = 0

print("""
Que tipo de caracteres você está usando?

1. Letras
2. Números
3. Letras e números
4. Letras, números e símbolos
""")

s = input("> ")

if s == "1":
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
elif s == "2":
    caracteres = "0123456789"
elif s == "3":
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
else:
    caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?!@#$_&-+()/*"

encontrou = False

for _ in range(1000000000000000000000000000000000000):
    tentativa = "".join(
        random.choice(caracteres)
        for _ in range(random.randint(1, 24))
    )

    print(f"tentativas: {y} - Testando: {tentativa}")

    if tentativa == r:
        encontrou = True
        print(f"\nSenha encontrada com sucesso! tentativas necessarias: {y}")
        print(f"Senha: {tentativa}")
        break

    y += 1
    #time.sleep(0.05)

if not encontrou:
    print("\nAcesso negado.")