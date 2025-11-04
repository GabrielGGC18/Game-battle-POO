from typing import Protocol, Optional 


class CoffeMachineProtocol(Protocol):
    def start(self) -> None: ...
    def create(self, coffeNome: str) -> str: ...
    def end(self) -> None: ...


class CoffeeApp:
    def __ini__(self, delegate: CoffeMachineProtocol):
        self.delegate = delegate     