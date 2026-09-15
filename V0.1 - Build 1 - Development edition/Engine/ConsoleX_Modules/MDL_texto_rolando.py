# MDL_texto_rolando.py

def code_au(texto, largura, posicao=0):
    if len(texto) <= largura: # Se cabe na barra, não anima.
        return texto.ljust(largura), 0

    # Espaços antes e depois para dar efeito de entrada e saída.
    texto_animado = (" " * largura) + texto + (" " * largura)
    
    if posicao >= len(texto_animado): # Reinicia quando terminar toda a animação.
        posicao = 0

    trecho = texto_animado[posicao:posicao + largura] # Pega apenas a parte visível.

    if len(trecho) < largura: # Caso esteja no final da animação.
        trecho = trecho.ljust(largura)

    return trecho, posicao + 1

# Anderson_Tsunami.11Xx