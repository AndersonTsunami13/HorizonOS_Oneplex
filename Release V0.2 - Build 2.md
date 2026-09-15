HorizonOS Oneplex V0.2

☕ Coffee Edition "beta"

A segunda grande versão de desenvolvimento do HorizonOS Oneplex.

A V0.2 não é apenas uma atualização da V0.1.

Ela representa uma grande evolução na arquitetura, organização e funcionamento interno do projeto.

---

⚙️ Principais mudanças

🖥️ Novo sistema de comandos

O terminal recebeu uma nova arquitetura para gerenciamento de comandos.

Os comandos passaram a ser organizados em módulos próprios, facilitando sua criação, manutenção e expansão.

Também foi adicionada a possibilidade de utilizar argumentos nos comandos.

Por exemplo:

echo Olá Horizon
calculadora 10 + 20

Essa estrutura cria uma base para comandos cada vez mais avançados nas próximas versões.

---

🧩 Evolução da Engine

A Engine passou por uma grande reorganização.

Diversos módulos foram separados, modificados ou substituídos para reduzir dependências e facilitar a expansão do sistema.

A estrutura passou a buscar uma separação mais clara entre:

- funcionalidades do sistema
- terminal
- Engine
- interface
- módulos individuais
- recursos experimentais

---

🧵 Threading

O sistema de threads passou a ser utilizado de forma mais integrada ao projeto.

Isso permite que determinados componentes funcionem em segundo plano sem bloquear completamente o terminal.

Esse conceito é utilizado principalmente em recursos relacionados a animações e elementos dinâmicos da interface.

---

📊 Status Bar e Dynamic Bar

A V0.2 trouxe uma evolução importante nos sistemas de informação exibidos no terminal.

Entre eles está a Dynamic Bar, capaz de apresentar informações de maneira dinâmica, como:

[●] HorizonOS   CPU 12%   RAM 51%   19:34

Esses sistemas fazem parte da evolução da interface do console do HorizonOS.

---

🧬 BIOS

A estrutura da BIOS também foi reorganizada.

Componentes relacionados à BIOS passaram a possuir uma organização mais modular, permitindo experimentar diferentes telas e funcionalidades sem concentrar tudo em um único componente.

---

🎞️ Sistema de animações

Os módulos relacionados a animações foram separados do núcleo principal do console.

Isso cria uma base mais adequada para futuros sistemas de:

- carregamento
- animações
- interfaces
- efeitos do terminal
- telas especiais

---

🧹 Limpeza e reorganização

Uma das mudanças menos visíveis, mas mais importantes, foi a limpeza do projeto.

Vários experimentos presentes na V0.1 foram removidos, reorganizados ou substituídos.

Nem todo código experimental precisa continuar existindo para sempre.

Algumas ideias permanecem.

Outras são descartadas.

E algumas acabam voltando anos depois com uma implementação completamente diferente.

---

🧪 Compatibilidade testada

A V0.2 foi executada e testada em diversos ambientes:

Windows

- Windows 8.1
- Windows 10
- Windows 11

Linux

- Linux Mint
- Ubuntu
- Zorin OS
- Debian

Android

- Samsung Galaxy A14 5G com Pydroid
- Samsung Galaxy A14 5G com Termux
- Samsung Galaxy J2 Prime com Termux e Python 3.8.0

Sim.

O HorizonOS chegou até um Galaxy J2 Prime. 💀📱

---

🚧 Estado atual

A V0.2 é uma versão beta de desenvolvimento.

Apesar de apresentar uma arquitetura consideravelmente mais organizada que a V0.1, ainda existem diversos componentes experimentais e áreas que podem ser aprimoradas.

Algumas das ideias futuras incluem:

- gerenciamento dos módulos da Engine
- uma API da Engine
- manipulação de arquivos
- configurações utilizando JSON
- sistema de usuários separados
- DevMode
- sistema de segurança
- filesystem simulado
- disquete simulado
- HotScript aprimorado
- emulador de CPU
- melhorias no sistema de animações
- novos comandos
- melhorias no tratamento de erros e logs
- novos recursos de hardware simulado

---

🧠 Sobre o projeto

O HorizonOS Oneplex é um projeto experimental desenvolvido para explorar conceitos de sistemas operacionais através da programação em Python.

Ele não pretende substituir um sistema operacional real.

A ideia é experimentar, testar, quebrar, consertar e aprender.

«1 ideia para infinitas possibilidades...»

---

☕ Por que "Coffee Edition"?

Porque depois de reorganizar a Engine, criar um novo sistema de comandos, integrar threads, testar em Windows, Linux e Android e fazer o projeto rodar até em um Galaxy J2 Prime...

um café parecia necessário. ☕😂

---

HorizonOS Oneplex V0.2

Mais modular.
Mais experimental.
Mais HorizonOS.

Coffee Edition "beta"
