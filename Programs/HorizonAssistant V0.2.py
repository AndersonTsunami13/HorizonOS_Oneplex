# HorizonAssistant - v0.2

from Engine.UI_Engine_ConsoleX import escrever

def responder(pergunta):
    pergunta = pergunta.lower().strip()

    # Cores
    if "cor" in pergunta and "fonte" in pergunta:
        return (
            "Você pode usar um dicionário de cores junto com o Colorama.\n"
            "Exemplo:\n"
            "CORES = {'alerta': Fore.RED, 'seguro': Fore.GREEN}"
        )

    # RAM
    elif "ram" in pergunta or "memória" in pergunta:
        return "Use simular_hardware() para visualizar RAM, VRAM, CPU e Disco."

    # Logs
    elif "log" in pergunta:
        return "Use escrever_log() para registrar ou limpar logs."

    # Reiniciar
    elif "reiniciar" in pergunta:
        return "Use iniciar_terminal() para reiniciar o Horizon."

    # Ajuda
    elif pergunta in ["ajuda", "help", "?"]:
        return (
            "Posso ajudar com:\n"
            "- RAM\n"
            "- Logs\n"
            "- Reiniciar sistema\n"
            "- Cor da fonte"
        )

    return "Ainda não sei responder isso. 😅"

def horizon_assistant():

    escrever("====================================", "CYAN")
    escrever("     HorizonAssistant v0.2", "MAGENTA")
    escrever("====================================", "CYAN")
    escrever("Digite 'ajuda' para ver exemplos.", "YELLOW")
    escrever("Digite 'sair' para fechar.", "YELLOW")

    while True:

        pergunta = input("\n👤 Você > ")

        if pergunta.lower() in ["sair", "exit", "quit"]:
            escrever("Até mais! 👋", "GREEN")
            break

        escrever("\n🤖 Horizon >", "CYAN")
        escrever(responder(pergunta), "WHITE")

horizon_assistant()