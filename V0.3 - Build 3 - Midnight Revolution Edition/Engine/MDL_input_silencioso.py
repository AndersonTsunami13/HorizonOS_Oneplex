# MDL_input_silencioao.py
# Esse modulo foi escrito especialmente para a digitação oculta da senha do sistema.

# Importação
import getpass

def mdl_input_silencioso(prompt): # escrita oculta
    return getpass.getpass(prompt)

if __name__ == "__main__":
    text = mdl_input_silencioso("Digite alguma coisa: ")
    print(f"Você digitou: {text}")
    
# Anderson_Tsunami.M3_E36