# 🎮 Jogo do Gabriel - Guia de Instalação e Execução

## 📋 Requisitos do Sistema

- Python 3.7+
- pip (gerenciador de pacotes Python)
- Sistema operacional: Windows, macOS ou Linux

---

## 🚀 Instalação das Dependências

### 1. **Clone o repositório** (se ainda não fez)
```bash
git clone https://github.com/GabrielGGC18/POO-Aulas-Aplica-o.git
cd POO-Aulas-Aplica-o
```

### 2. **Crie um ambiente virtual** (recomendado)

#### No Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

---

## 📦 Dependências do Projeto

| Pacote | Versão | Propósito |
|--------|--------|----------|
| **pygame** | ≥2.1.0 | Engine gráfica para o jogo |
| **pillow** | ≥9.0.0 | Processamento de imagens (usado pelo pygame) |

---

## ▶️ Como Executar o Jogo

### Linux/macOS:
```bash
python3 main.py
```

### Windows:
```bash
python main.py
```

---

## 🎮 Controles do Jogo

### **Goku** (Esquerda)
- ⬆️ **Seta para Cima** - Se move para cima
- ⬇️ **Seta para Baixo** - Se move para baixo
- ⬅️ **Seta para Esquerda** - Se move para esquerda
- ➡️ **Seta para Direita** - Se move para direita
- **Z** - Ativa Kamehameha (20 de dano) ⚡

### **Naruto** (Direita)
- **W** - Se move para cima
- **A** - Se move para esquerda
- **S** - Se move para baixo
- **D** - Se move para direita
- **X** - Ativa Odama Rasengan (15 de dano) 🌀

### **Geral**
- **ESC** - Sair do jogo
- Fechar janela - Retorna ao menu

---

## 📁 Estrutura do Projeto

```
POO-Aulas-Aplica-o/
├── main.py                      # Ponto de entrada (Menu)
├── facade.py                    # Padrão Facade (orquestra o jogo)
├── characters.py                # Personagens (Goku, Naruto)
├── strategies.py                # Padrão Strategy (movimentos)
├── events.py                    # Padrão Observer (sistema de eventos)
├── game_manager.py              # Padrão Singleton (gerenciador do jogo)
├── requirements.txt             # Dependências do projeto
├── SETUP.md                     # Este arquivo
├── ANALISE_POO_PATTERNS.md      # Análise de padrões de projeto
├── FLUXO_EXECUCAO_PATTERNS.md   # Fluxo de execução
├── assets/                      # Pasta com recursos gráficos
│   ├── cenario.jpg             # Imagem de fundo
│   ├── goku.png                # Sprite do Goku
│   └── naruto.png              # Sprite do Naruto
└── Aprendizado-aula/           # Exemplos adicionais
```

---

## 🐛 Solução de Problemas

### Erro: `ModuleNotFoundError: No module named 'pygame'`
**Solução**:
```bash
pip install pygame
```

### Erro: `FileNotFoundError: assets/cenario.jpg`
**Solução**: Certifique-se de estar na pasta correta
```bash
cd /home/gabriel/POO-Aulas-Aplica-o
python3 main.py
```

### Erro: `ImportError` ao executar
**Solução**: Verifique se todas as dependências estão instaladas
```bash
pip install -r requirements.txt
```

### Jogo muito lento
**Solução**: Feche outros programas e tente novamente. O jogo roda a 60 FPS.

---

## 🎓 Conceitos de POO Implementados

✅ **Herança** - Goku e Naruto herdam de Character  
✅ **Polimorfismo** - special_move() implementado diferente  
✅ **Abstração** - Classes abstratas com métodos abstratos  
✅ **Encapsulamento** - Atributos e métodos encapsulados  

---

## 🎨 Padrões de Projeto Implementados

✅ **Singleton** - GameManager (uma única instância)  
✅ **Factory** - CharacterFactory (criação centralizada)  
✅ **Strategy** - MoveStrategy (diferentes algoritmos)  
✅ **Observer** - GameEvent + ConsoleNotifier (eventos)  
✅ **Facade** - GameFacade (interface simplificada)  
✅ **Abstract** - Classes abstratas com contratos  

---

## 📝 Notas Importantes

- O jogo roda a **60 FPS** para melhor performance
- O movimento é limitado à tela de 800x369 pixels
- Cada ataque especial tem um cooldown de 30 frames
- O jogo mostra eventos no console (vencedores, danos, etc)

---

## 👨‍💻 Autor

**Gabriel Gomes Cardoso**  
Projeto de aplicação de conceitos de POO e Padrões de Projeto

---

## 📚 Documentação Adicional

- 📄 [ANALISE_POO_PATTERNS.md](ANALISE_POO_PATTERNS.md) - Análise detalhada de cada padrão
- 📄 [FLUXO_EXECUCAO_PATTERNS.md](FLUXO_EXECUCAO_PATTERNS.md) - Como os padrões funcionam em execução

