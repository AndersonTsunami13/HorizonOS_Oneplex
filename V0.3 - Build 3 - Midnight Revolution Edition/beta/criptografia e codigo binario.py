def bin(texto):
    return " ".join(format(byte, "08b") for byte in texto.encode("utf-8"))


def unbin(binary):
    numeros = binary.split()
    dados = bytes(int(numero, 2) for numero in numeros)
    return dados.decode("utf-8")
    
codigo = bin("Hello")

print(codigo)

print(unbin(codigo))

from cryptography.fernet import Fernet

chave = Fernet.generate_key()

cripto = Fernet(chave)

mensagem = b"Hello mundo!"

codigo = cripto.encrypt(mensagem)

print("Criptografado:")
print(codigo)

original = cripto.decrypt(codigo)

print("Original:")
print(original.decode())