# ==== Navegador ====
historico = []

paginas = {
    "horizon.net": "Bem-vindo ao HorizonNet!\n1. Notícias\n2. Jogos\n3. Sobre",
    "horizon.net/noticias": "Últimas notícias:\n- Sistema X Ultra lançado!\n- Bugs resolvidos!",
    "horizon.net/jogos": "Jogos disponíveis:\n- Horizon Tetris\n- Ping Pong Mobile\n- Hackeando o Sistema",
    "horizon.net/sobre": "HorizonNet: navegador textual do HorizonOS.\nPara estudos e diversão."
}

def barra_carregamento():
    for i in range(1, 21):
        print(f"\rCarregando: [{'='*i}{' '*(20-i)}] {i*5}%", end="")
        time.sleep(0.03)
    print()

def abrir_pagina(url):
    barra_carregamento()
    if url in paginas:
        historico.append(url)
        print("\n" + paginas[url])
        if url == "horizon.net":
            escolha = input("Escolha um número> ").strip()
            if escolha == "1":
                abrir_pagina("horizon.net/noticias")
            elif escolha == "2":
                abrir_pagina("horizon.net/jogos")
            elif escolha == "3":
                abrir_pagina("horizon.net/sobre")
            else:
                print("Opção inválida!")
    else:
        print("\n404 Not Found!")

def navegador():
    while True:
        print("\n=== HorizonNet ===")
        print("Digite 'sair' para fechar o navegador.")
        url = input("URL> ").strip()
        if url.lower() == "sair":
            break
        abrir_pagina(url)
    print("Fechando HorizonNet...")