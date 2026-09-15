# HorizonAssistant - Assistente virtual para o HorizonOS

from Engine.UI_Engine_ConsoleX import escrever

# Dicionário de perguntas e respostas
respostas = {
    "como trocar a cor da fonte": "Crie um dicionário de cores e use Fore do Colorama, por exemplo: CORES = {'alerta': Fore.RED, 'seguro': Fore.GREEN}. Depois use print(CORES['alerta'] + 'Mensagem' + Style.RESET_ALL).",
    "como limpar os logs": "Use a função escrever_log('texto', 'nivel') para registrar ou limpar logs.",
    "como ver o status da ram": "Use a função simular_hardware() para ver RAM, VRAM, disco e CPU.",
    "como reiniciar o sistema": "Use iniciar_terminal() para reiniciar o terminal do HorizonOS."
}

# Loop de interação
def horizon_assistant():
    escrever("HorizonAssistant - pronto para te ajudar!", "MAGENTA")
    
    while True:
        pergunta = input("Pergunta > ").lower().strip()
        if pergunta in ["sair", "exit", "quit"]:
            escrever("Assistente encerrado. Até mais!", "CYAN")
            break
        resposta = respostas.get(pergunta, "Desculpa, ainda não sei responder isso. Mas tô aprendendo!")
        escrever(resposta, "YELLOW")

horizon_assistant()