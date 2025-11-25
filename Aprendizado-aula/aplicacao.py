from typing import Protocol, Optional


class CoffeMachineProtocol(Protocol):
    def start(self) -> None: ...
    def create(self, coffeNome: str) -> str: ...
    def end(self) -> None: ...


class CoffeeApp:
    # erro: era __ini__, o correto é __init__
    def __init__(self, delegate: CoffeMachineProtocol):
        self.delegate = delegate

    # precisa ter 'self' como primeiro parâmetro
    def order(self, coffeNome: str):
        # usar self.delegate (não apenas delegate)
        self.delegate.start()
        self.delegate.create(coffeNome=coffeNome)
        self.delegate.end()


class JoaquinMachineCoffe:
    def start(self):
        print("Joaquin's Coffee starting.......vrrrruuuuuuuuuuuu")

    def create(self, coffeNome: str):
        print("Verificando o café solicitado")

        # operador correto: 'or', não '|'
        if coffeNome == "espresso" or coffeNome == "capuccino":
            print("Café saindo, aguarde um pouco!")
        else:
            print("Café não encontrado - ERROU HAHA")

    def end(self):
        print("Power off")


class CachorroMachineCoffe:
    def start(self):
        print("Cachorro's Coffee AUAUAUUAUAUAUAUAUUAUAUAU starting.......vrrrruuuuuuuuuuuu")

    def create(self, coffeNome: str):
        print("Verificando o café solicitado")

        # operador correto: 'or', não '|'
        if coffeNome == "Pingado":
            print("Café saindo, aguarde um pouco!")
        else:
            print("Café não encontrado - ERROU HAHA")

    def end(self):
        print("Power off")



# Nome da Classe e Instância
cachorroMachine = CachorroMachineCoffe()
joaquinMachine = JoaquinMachineCoffe()
app = CoffeeApp(delegate = cachorroMachine)
app.order("pingado") 
