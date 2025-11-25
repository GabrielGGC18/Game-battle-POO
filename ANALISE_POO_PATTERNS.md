#  Análise de Conceitos POO e Padrões de Projeto

##  Conceitos Fundamentais de POO Implementados

### 1. **HERANÇA DE CLASSE** ✓
```python
# Em characters.py
class Character(ABC):  # Classe base abstrata
    def __init__(self, name, img, power, life, strategy: MoveStrategy):
        self.name = name
        self.image = ...

class Goku(Character):  # Herança de Character
    def special_move(self):
        return "Kamehameha 10x!"

class Naruto(Character):  # Herança de Character
    def special_move(self):
        return "Odama Rasengan!"
```
**Conceito**: Goku e Naruto herdam atributos e métodos de Character, evitando duplicação de código.

---

### 2. **ABSTRAÇÃO** ✓
```python
# Em characters.py
from abc import ABC, abstractmethod

class Character(ABC):  # Classe abstrata
    @abstractmethod
    def special_move(self): pass  # Método abstrato obrigatório
```
**Conceito**: Character é abstrata e não pode ser instanciada diretamente. Força subclasses a implementar `special_move()`.

---

### 3. **POLIMORFISMO** ✓
```python
# Polimorfismo de método (Override)
class Goku(Character):
    def special_move(self):  # Implementação diferente
        return "Kamehameha 10x!"

class Naruto(Character):
    def special_move(self):  # Implementação diferente
        return "Odama Rasengan!"

# Uso polimórfico
character: Character = Goku(...)
character.special_move()  # Chama o método de Goku

character: Character = Naruto(...)
character.special_move()  # Chama o método de Naruto (diferente)
```
**Conceito**: Mesmo método, comportamentos diferentes dependendo da classe.

---

### 4. **ENCAPSULAMENTO** ✓
```python
# Em characters.py
class Character(ABC):
    def __init__(self, name, img, power, life, strategy):
        self.name = name              # Atributo
        self.power = power            # Atributo
        self.life = life              # Atributo (modificável)
        self.strategy = strategy      # Composição

    def move(self, x, y, keys):
        return self.strategy.move(x, y, keys)  # Método público
```
**Conceito**: Atributos e métodos encapsulados na classe. Estratégia delegada ao objeto `strategy`.

---

### 5. **ATRIBUTOS** ✓
```python
class Character(ABC):
    # Atributos de instância
    self.name: str
    self.image: pygame.Surface
    self.power: int
    self.life: int              # Mutável (pode receber dano)
    self.max_life: int          # Imutável (valor máximo)
    self.strategy: MoveStrategy
    self.special_move_text: str
    self.special_move_timer: int
```

---

### 6. **MÉTODOS** ✓
```python
class Character(ABC):
    # Métodos
    def __init__(self, ...):        # Construtor
    @abstractmethod
    def special_move(self): pass    # Método abstrato
    
    def move(self, x, y, keys):     # Método concreto (composição)
        return self.strategy.move(x, y, keys)
```

---

##  Padrões de Projeto Implementados

### 1. **SINGLETON** ✓
**Arquivo**: `game_manager.py`
```python
class GameManager:
    _instance = None  # Variável de classe
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # Uma única instância
            cls._instance.running = True
        return cls._instance
    
    def stop(self):
        self.running = False
```
**Uso em facade.py**:
```python
self.manager = GameManager()  # Sempre mesma instância
```
**Conceito**: Garante que exista apenas uma instância de GameManager em toda a aplicação.

---

### 2. **FACTORY** ✓
**Arquivo**: `characters.py`
```python
class CharacterFactory:
    @staticmethod
    def create(type_, strategy):  # Método factory
        if type_ == "goku":
            return Goku("Goku", "assets/goku.png", 100, 200, strategy)
        elif type_ == "naruto":
            return Naruto("Naruto", "assets/naruto.png", 90, 180, strategy)
        else:
            raise ValueError("Personagem desconhecido")
```
**Uso em facade.py**:
```python
self.goku = CharacterFactory.create("goku", NormalMove())
self.naruto = CharacterFactory.create("naruto", FastMove())
```
**Conceito**: Centraliza a criação de objetos Character, permitindo adicionar novos personagens sem modificar o código cliente.

---

### 3. **STRATEGY** ✓
**Arquivo**: `strategies.py`
```python
from abc import ABC, abstractmethod

class MoveStrategy(ABC):  # Interface
    @abstractmethod
    def move(self, x, y, keys, screen_width=800, screen_height=369): pass

class NormalMove(MoveStrategy):  # Estratégia 1
    def move(self, x, y, keys, screen_width=800, screen_height=369):
        vel = 10
        # Implementação específica
        return x, y

class FastMove(MoveStrategy):  # Estratégia 2
    def move(self, x, y, keys, screen_width=800, screen_height=369):
        vel = 20
        # Implementação diferente
        return x, y
```
**Uso em characters.py**:
```python
class Character(ABC):
    def __init__(self, name, img, power, life, strategy: MoveStrategy):
        self.strategy = strategy  # Composição com estratégia

    def move(self, x, y, keys):
        return self.strategy.move(x, y, keys)  # Delegação
```
**Uso em facade.py**:
```python
self.goku = CharacterFactory.create("goku", NormalMove())      # Goku lento
self.naruto = CharacterFactory.create("naruto", FastMove())    # Naruto rápido
```
**Conceito**: Encapsula diferentes algoritmos de movimento. Pode-se trocar estratégias em runtime.

---

### 4. **OBSERVER** ✓
**Arquivo**: `events.py`
```python
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message): pass  # Interface do observador

class ConsoleNotifier(Observer):  # Observador concreto
    def update(self, message):
        print(f"[EVENTO]: {message}")

class GameEvent:  # Subject/Publicador
    def __init__(self):
        self._observers = []  # Lista de observadores
    
    def add_observer(self, obs):
        self._observers.append(obs)  # Registra observador
    
    def notify(self, msg):
        [o.update(msg) for o in self._observers]  # Notifica todos
```
**Uso em facade.py**:
```python
# Inicialização
self.events = GameEvent()
self.events.add_observer(ConsoleNotifier())

# Notificação quando evento ocorre
self.events.notify(f"Goku usou Kamehameha! Naruto recebeu 20 de dano!")
```
**Conceito**: Desacopla o sistema de eventos (GameEvent) dos observadores (ConsoleNotifier). Permite adicionar novos observadores sem modificar GameEvent.

---

### 5. **FACADE** ✓
**Arquivo**: `facade.py`
```python
class GameFacade:
    """Fornece interface simplificada para o jogo complexo"""
    
    def __init__(self, surface):
        # Integra múltiplos componentes
        self.bg = pygame.image.load("assets/cenario.jpg")
        self.events = GameEvent()              # Observer
        self.manager = GameManager()            # Singleton
        self.goku = CharacterFactory.create()  # Factory
        self.naruto = CharacterFactory.create() # Factory
        self.hud = HUD(surface)                # Subsistema
    
    def run(self):
        """Executa todo o jogo com uma chamada simples"""
        # Encapsula toda a lógica de game loop
        while True:
            # Trata eventos, atualiza estado, renderiza
            pygame.display.update()
```
**Uso em main.py**:
```python
def start_game():
    game = GameFacade(screen)  # Interface simples
    game.run()  # Abstrai toda complexidade
```
**Conceito**: Fornece uma interface simplificada (GameFacade) para um subsistema complexo contendo vários padrões.

---

##  Diagrama de Relacionamentos

```
┌─────────────────────────────────────────────────────┐
│                    GameFacade                        │
│  (Facade - Orquestra todos os componentes)          │
└─────────────────────────────────────────────────────┘
           │                      │                │
           ▼                      ▼                ▼
    ┌──────────────┐      ┌──────────────┐   ┌──────────┐
    │ GameManager  │      │  GameEvent   │   │   HUD    │
    │ (Singleton)  │      │  (Observer)  │   │ (Helper) │
    └──────────────┘      └──────────────┘   └──────────┘
                                   │
                                   ▼
                           ┌───────────────┐
                           │ConsoleNotifier│
                           └───────────────┘

    ┌─────────────────────────────────────────────┐
    │  CharacterFactory  (Factory Pattern)        │
    └─────────────────────────────────────────────┘
              │                    │
              ▼                    ▼
        ┌──────────┐        ┌──────────┐
        │  Goku    │        │ Naruto   │
        │(herança) │        │(herança) │
        └──────────┘        └──────────┘
              △                    △
              │                    │
              └────────┬───────────┘
                       │
            ┌──────────▼───────────┐
            │ Character (Abstrata) │
            │ (Polimorfismo)       │
            └──────────┬───────────┘
                       │
                       ▼
            ┌────────────────────┐
            │ MoveStrategy (ABC) │
            │ (Strategy Pattern) │
            └────────────────────┘
              │                  │
              ▼                  ▼
        ┌──────────┐       ┌──────────┐
        │NormalMove│       │ FastMove │
        └──────────┘       └──────────┘
```

---

##  Resumo de Conformidade

| Conceito/Padrão | Status | Arquivo | Descrição |
|---|---|---|---|
| **Herança** | ✅ | characters.py | Goku, Naruto herdam de Character |
| **Abstração** | ✅ | characters.py, strategies.py, events.py | Classes ABC e métodos abstratos |
| **Polimorfismo** | ✅ | characters.py | special_move() implementado diferente |
| **Encapsulamento** | ✅ | characters.py | Atributos e métodos encapsulados |
| **Atributos** | ✅ | characters.py | name, life, power, strategy, etc |
| **Métodos** | ✅ | Todos | Construtores, métodos públicos/abstratos |
| **Singleton** | ✅ | game_manager.py | GameManager única instância |
| **Factory** | ✅ | characters.py | CharacterFactory cria Character |
| **Strategy** | ✅ | strategies.py | MoveStrategy com variações |
| **Observer** | ✅ | events.py | GameEvent com observadores |
| **Facade** | ✅ | facade.py | GameFacade orquestra tudo |

---

##  Conclusão

✅ **SIM, o código mantém TODOS os conceitos de POO e padrões de projeto solicitados:**

1. **Polimorfismo**: Método `special_move()` implementado diferente em Goku e Naruto
2. **Herança**: Goku e Naruto herdam de Character (abstrata)
3. **Atributos**: life, power, name, image, strategy, etc
4. **Métodos**: special_move(), move(), __init__()
5. **Padrões**:
   - ✅ **Observer**: Sistema de eventos com ConsoleNotifier
   - ✅ **Abstract**: Classe Character abstrata com métodos abstratos
   - ✅ **Factory**: CharacterFactory para criar personagens
   - ✅ **Strategy**: MoveStrategy para diferentes tipos de movimento
   - ✅ **Facade**: GameFacade orquestra todos os componentes
   - ✅ **Singleton**: GameManager garante única instância

O código é um **exemplo excelente de aplicação real de POO** com padrões de projeto bem implementados! 🎉
