### Aplicações de Conceitos em Python

>   Aprendizado em Python, usando classes e herança de classes.

**Classes e Objetos**

    -Abstract Methods -Factory
    -Builder        -observer
    -Singleton      -staticmethod
    -Delegate       - Strategy 
    -Notification   - Facade
    - Adapter        - Decorator
    - Dependecy Injection

**OBJETOS INCONSISTENTES- É aquele distinto da realidade,
Não pode ter um objeto inconsistente!**
    
---

# O Tema Escolhido do Projeto

**Um Game em Python**

*Nome:* 

**Battle  Simulator**

É um jogo construído na linguagem Python com o intuito de simular uma batalha entre personagens.

### V1 Goku vs Naruto

---

## Estrutura do Projeto

O projeto está organizado em módulos, cada um responsável por uma parte da lógica:

- **main.py**: ponto de entrada do jogo, integra Tkinter (menu) e Pygame (jogo).
- **facade.py**: aplica o padrão *Facade*, centralizando a inicialização e execução do jogo.
- **game_manager.py**: implementa o padrão *Singleton* para controlar o estado global do jogo.
- **events.py**: aplica o padrão *Observer* para notificação de eventos (como perda de vida).
- **strategies.py**: implementa o padrão *Strategy* para diferentes formas de movimentação dos personagens.
- **characters.py**: define personagens usando *Factory Method* e abstrações.
- **assets/**: contém imagens utilizadas no jogo (cenário e personagens).

---

## Conceitos de POO Aplicados

- **Factory Method**: criação dos personagens (Goku e Naruto).
- **Strategy**: diferentes estratégias de movimento (normal e rápido).
- **Observer**: notificação de eventos como perda de vida ou ataques.
- **Singleton**: gerenciamento do estado do jogo.
- **Facade**: simplificação da inicialização e execução do jogo.
- **Decorator / Adapter / Builder / Dependency Injection**: conceitos estudados e aplicados em diferentes partes do código como forma de aprendizado e prática.

---

## Funcionalidades Implementadas

- **Menu inicial em Tkinter** com opções de iniciar jogo e sair.
- **Integração com Pygame** para renderização da batalha.
- **HUD (Heads-Up Display)** mostrando:
  - Barras de vida dos personagens.
  - Pontuação acumulada.
- **Movimentação dos personagens** controlada pelo teclado.
- **Ataques especiais**:
  - Goku: Kamehameha.
  - Naruto: Rasengan.
- **Eventos notificados no console** (Observer).
- **Cenário de fundo** e sprites dos personagens.

---

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/GabrielGGC18/Game-battle-POO.git
   cd Game-battle-POO
****

