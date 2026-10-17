# securitymodule_createpassword.py 

# inportação 
import hashlib
import time

def create_password_one():
    # Pergunta simples...
    password = input("Digite a sua senha: ")
    print("Criando...")
    time.sleep(1)

    # o início dos caos... -_  -
    print(hashlib.sha256(password.encode()).hexdigest())
    input()
    
def create_password_two(password):
    hash_gerado = hashlib.sha256(password.encode()).hexdigest()
    return hash_gerado # <-- Isso envia o hash de volta

if __name__ == "__main__":
    create_password_one()
# Anderson_Tsunami.11Xx