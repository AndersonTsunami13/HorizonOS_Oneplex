import time

r = int(input("Digite um número: "))
encontrou = False

for tentativa in range(10000000000000000000000000000000000000000000000000000000000000000000000000000000):
    print(f"Testando: {tentativa}")

    if tentativa == r:
        encontrou = True
        print(f"Número encontrado: {tentativa}")
        #time.sleep(1)
        input("Pressione enter para continuar...")
        break

if not encontrou:
    print("Não encontrado.")
    input("Pressione enter para continuar...")