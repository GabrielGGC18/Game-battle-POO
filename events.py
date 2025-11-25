from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message): pass

class ConsoleNotifier(Observer):
    def update(self, message): print(f"[EVENTO]: {message}")

class GameEvent:
    def __init__(self): self._observers = []
    def add_observer(self, obs): self._observers.append(obs)
    def notify(self, msg): [o.update(msg) for o in self._observers]

