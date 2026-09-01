import time
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def animacao_inicio():
    limpar()
    msg = "Inicializando Horizon Byte Inspector..."
    for c in msg:
        print(c, end="", flush=True)
        time.sleep(0.03)
    time.sleep(0.4)
    print("\n")

def barra_do_bit(bit):
    return "█" if bit == "1" else " "

def inspecionar(numero):
    binario = format(numero, "08b")
    hex_val = format(numero, "02X")

    print(f"\n=== HORIZON BYTE INSPECTOR 2.0 ===")
    print(f"Decimal:     {numero}")
    print(f"Hexadecimal: 0x{hex_val}")
    print(f"Binário:      {binario}\n")

    print("Mapa visual dos bits:")
    print(" ".join(list(binario)))
    print(" ".join([barra_do_bit(b) for b in binario]))
    print()

    for i in range(8):
        print(f"bit {7 - i}: {binario[i]}  | {('ON ' if binario[i]=='1' else 'OFF')}")

    print("\nScan completo.\n")

def main():
    animacao_inicio()

    while True:
        try:
            numero = int(input("Digite um valor (0 a 255) ou -1 para sair: "))
        except:
            print("Entrada inválida.")
            continue

        if numero == -1:
            print("Encerrando inspector... adeus, operador.")
            time.sleep(0.5)
            break

        if numero < 0 or numero > 255:
            print("Valor fora do range de 8 bits.")
            continue

        inspecionar(numero)
        time.sleep(0.5)

main()