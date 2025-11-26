#  Fluxo de Execução - Padrões de Projeto em Ação

## 1️ SINGLETON - Garantindo Uma Única Instância

```
main.py
  │
  ├─► start_game()
  │     │
  │     └─► GameFacade(screen)
  │           │
  │           └─► GameManager()  ◄─── SINGLETON
  │                 │
  │                 ├─ Primeira chamada: Cria _instance
  │                 │
  │                 └─ Próximas chamadas: Retorna _instance existente
  │
  └─ self.manager.stop()  ◄─── Sempre a mesma instância!
```

**Resultado**: Há apenas um GameManager em toda a aplicação 

---

## 2️ FACTORY - Criação Centralizada de Personagens

```
GameFacade.__init__()
  │
  ├─ CharacterFactory.create("goku", NormalMove())
  │   │
  │   ├─ Verifica tipo: "goku"
  │   │
  │   └─► return Goku(
  │           name="Goku",
  │           img="assets/goku.png",
  │           power=100,
  │           life=200,
  │           strategy=NormalMove()  ◄─ Strategy injetada
  │       )
  │
  └─ CharacterFactory.create("naruto", FastMove())
      │
      ├─ Verifica tipo: "naruto"
      │
      └─► return Naruto(
              name="Naruto",
              img="assets/naruto.png",
              power=90,
              life=180,
              strategy=FastMove()
          )
```

**Vantagem**: Adicionar novo personagem não requer mudança no GameFacade 

---

## 3️ STRATEGY - Delegação de Algoritmos

```
Character (Abstrata)
  │
  ├─ Goku
  │   └─ strategy: NormalMove()  ◄─ Velocidade = 10
  │       │
  │       └─ move(x, y, keys)
  │           └─ return (x ± 10, y ± 10)
  │
  └─ Naruto
      └─ strategy: FastMove()  ◄─ Velocidade = 20
          │
          └─ move(x, y, keys)
              └─ return (x ± 20, y ± 20)
```

**Em tempo de execução**:
```
keys[pygame.K_UP] = True

# Goku se move 10 pixels
self.goku_x, self.goku_y = self.goku.move(...)
# Internamente: self.goku.strategy.move(...)
# Resultado: y -= 10

# Naruto se move 20 pixels
self.naruto_x, self.naruto_y = self.naruto.move(...)
# Internamente: self.naruto.strategy.move(...)
# Resultado: y -= 20
```

**Vantagem**: Trocar estratégia em runtime sem alterar a classe 

---

## 4️ OBSERVER - Sistema de Eventos

```
GameFacade.__init__()
  │
  ├─ GameEvent() criado
  │   │
  │   └─ self._observers = []  ◄─ Lista vazia
  │
  └─ ConsoleNotifier() criado
      │
      └─ self.events.add_observer(ConsoleNotifier())
          │
          └─ self._observers = [ConsoleNotifier()]

Durante o jogo (quando ataque especial acontece):
  │
  ├─ if keys[pygame.K_z] and self.goku_attack_cooldown == 0:
  │   │
  │   ├─ self.goku.special_move()  ◄─ Ativa ataque
  │   │
  │   ├─ self.naruto.life -= 20  ◄─ Aplica dano
  │   │
  │   └─ self.events.notify(f"Goku usou Kamehameha!")
  │       │
  │       └─ [o.update(msg) for o in self._observers]
  │           │
  │           └─ ConsoleNotifier.update(msg)
  │               │
  │               └─ print("[EVENTO]: Goku usou Kamehameha!")
```

**Fluxo**:
1. Evento ocorre (ataque)
2. GameEvent notifica observadores registrados
3. Cada observador reage independentemente
4. Fácil adicionar novos observadores sem modificar GameEvent

**Vantagem**: Desacoplamento entre eventos e reações 

---

## 5️ ABSTRACT & POLIMORFISMO

```
┌─────────────────────────────────┐
│ Character (ABC)                 │
│ ─────────────────────────────   │
│ + name: str                     │
│ + life: int                     │
│ + power: int                    │
│ + strategy: MoveStrategy        │
│ ─────────────────────────────   │
│ + move(x, y, keys)              │
│ + special_move() → ABSTRACT     │ ◄─ Obrigatório
└─────────────────────────────────┘
        △                △
        │                │
     ┌──┴──┐          ┌──┴──┐
     │     │          │     │
     │  Goku        Naruto  │
     │     │          │     │
     └──┬──┘          └──┬──┘
        │                │
   ┌────▼─────────────────┴────────┐
   │ Implementam special_move()    │
   │ diferente                     │
   └───────────────────────────────┘

Goku.special_move():
  └─ return "Kamehameha 10x!"
     └─ Inflige 20 de dano

Naruto.special_move():
  └─ return "Odama Rasengan!"
     └─ Inflige 15 de dano
```

**Resultado**: Mesmo tipo (Character), comportamentos diferentes 

---

## 6️ FACADE - Orquestração Complexa

```
main.py (Cliente simples)
  │
  └─ game = GameFacade(screen)  ◄─ Interface única
      │
      └─ game.run()  ◄─ Chamada simples
          │
          ├─ Cria GameManager (Singleton)
          ├─ Cria GameEvent (Observer)
          ├─ Cria Goku via Factory
          ├─ Cria Naruto via Factory
          ├─ Usa Strategy para movimento
          ├─ Renderiza gráficos
          ├─ Gerencia colisões
          ├─ Controla dano
          └─ Trata eventos

ANTES (sem Facade):
  game = GameManager()
  game.start()
  events = GameEvent()
  notifier = ConsoleNotifier()
  events.add_observer(notifier)
  goku = CharacterFactory.create("goku", NormalMove())
  ... (muito mais código)

DEPOIS (com Facade):
  game = GameFacade(screen)
  game.run()
```

**Vantagem**: Main.py é simples e limpo 

---

## 7️ COMPOSIÇÃO SOBRE HERANÇA

```
Character
  │
  ├─ Usa composição com Strategy
  │   └─ self.strategy: MoveStrategy
  │       ├─ Implementação separada
  │       ├─ Fácil trocar em runtime
  │       └─ Mais flexível que herança múltipla
  │
  └─ Herança de ABC
      └─ Define contrato (special_move abstrato)
          ├─ Força implementação em subclasses
          └─ Define interface comum
```

---

##  Benefícios Alcançados

| Padrão | Benefício |
|--------|-----------|
| **Singleton** | GameManager é único, consistente |
| **Factory** | Novos personagens sem alterar GameFacade |
| **Strategy** | Diferentes movimentos independentes |
| **Observer** | Sistema de eventos desacoplado |
| **Abstract** | Contrato claro para subclasses |
| **Facade** | Interface simplificada para cliente |
| **Polimorfismo** | special_move() se comporta diferente |

---

##  Exemplo Completo de Execução

```python
# 1. Main inicia
if __name__ == "__main__":
    root = tk.Tk()
    
# 2. Usuário clica "Iniciar Jogo"
def start_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 369))
    
    # 3. Facade criada (orquestra tudo)
    game = GameFacade(screen)
    #     ├─ Singleton criado
    #     ├─ Observer setup
    #     ├─ Factory cria personagens com Strategy
    #     └─ HUD pronto
    
    # 4. Game loop começa
    game.run()
    #    ├─ Lê inputs (Setas para Goku, WASD para Naruto)
    #    ├─ Aplica Strategy de movimento
    #    ├─ Processa ataques especiais
    #    ├─ Notifica Observer (console print)
    #    ├─ Renderiza
    #    └─ Repete até vida = 0

# 5. Personagem morre
if self.naruto.life <= 0:
    self.events.notify("Goku venceu!")  # Observer notificado
    break  # Sai do loop

# 6. Volta ao menu
return  # Saída graceful
```

---

##  Conclusão

O código implementa **6 padrões de projeto** trabalhando juntos:

```
Main  
  │
  └─► Facade ◄─────────────────┐
       │                        │
       ├─► Singleton ────────────┤
       │                        │
       ├─► Factory ─────────────┼─► Strategy (NormalMove, FastMove)
       │                        │
       ├─► Observer ────────────┤
       │                        │
       ├─► Abstract ────────────┼─► Polimorfismo
       │                        │
       └─► Composição ──────────┘
```

**Resultado**: Código **flexível**, **manutenível** e **extensível** 

