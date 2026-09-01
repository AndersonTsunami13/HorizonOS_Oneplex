import random
import time
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def to_ascii(valor):
    if 32 <= valor <= 126:
        return chr(valor)
    return "."

def scan_loop():
    endereco = 0x000000

    while True:
        limpar()

        print("=== HORIZON MEMORY SCANNER ===\n")
        print("[Ghost Layer Active]\n")

        for _ in range(16):
            valor = random.randint(0, 255)

            hex_val = f"{valor:02X}"
            bin_val = f"{valor:08b}"
            ascii_val = to_ascii(valor)

            print(f"0x{endereco:06X}  |  {hex_val}  |  {bin_val}  |  {ascii_val}")

            endereco += 1

        print("\nScanning memory...\n")

        time.sleep(0.3)

try:
    scan_loop()
except KeyboardInterrupt:
    print("\nScan interrompido.")