# ==========================================
# Horizon Elite T1000
# S8E Virtual CPU v0.2
# ==========================================

import string


class HElite_T1000:

    def __init__(self):

        # Memória de 8 bits
        self.memory = [0] * 256


        # Criar registradores A-Z e AA-ZZ
        self.registers = {}

        letras = string.ascii_uppercase


        # A até Z
        for letra in letras:
            self.registers[letra] = 0


        # AA até ZZ
        for primeira in letras:
            for segunda in letras:
                self.registers[primeira + segunda] = 0


        # Registrador especial
        self.PC = 0

        self.running = True



    def carregar_programa(self, programa):

        for i, instrucao in enumerate(programa):
            self.memory[i] = instrucao



    def executar(self):

        print("=== Horizon Elite T1000 ===")
        print("S8E Virtual CPU v0.2\n")


        while self.running:


            instrucao = self.memory[self.PC]

            self.PC += 1



            # LOAD registrador A
            if instrucao == 1:

                valor = self.memory[self.PC]

                self.PC += 1

                self.registers["A"] = valor



            # ADD no registrador A
            elif instrucao == 2:

                valor = self.memory[self.PC]

                self.PC += 1

                self.registers["A"] += valor



            # PRINT A
            elif instrucao == 3:

                print(
                    "S8E OUTPUT:",
                    self.registers["A"]
                )



            # INFO CPU
            elif instrucao == 4:

                print(
                    "Registradores:",
                    len(self.registers)
                )



            # HALT
            elif instrucao == 255:

                print("\nCPU parada.")

                self.running = False



            else:

                print(
                    "Erro: instrução",
                    instrucao
                )

                self.running = False





# Programa S8E

programa = [

    1, 10,     # LOAD A 10

    2, 5,      # ADD 5

    3,         # PRINT

    4,         # INFO

    255       # HALT

]



# Criar CPU

cpu = HElite_T1000()


# Carregar programa

cpu.carregar_programa(programa)


# Executar

cpu.executar()



"""
DOCUMENTAÇÃO

Horizon Elite T1000

Arquitetura:
S8E

Bits:
8-bit

Classe:
Virtual CPU

Registradores:
A-Z até AA-ZZ

Total:
702 registradores

Memória:
256 bytes

ISA:
Horizon Instruction Set

Versão:
0.2

"""