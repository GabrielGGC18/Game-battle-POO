from typing import Protocol


class WeatherStationProtocol(Protocol):
    def temperatureUpdated(self, newTemperature: float) -> None: ...
    def send(self, Station: str) -> None: ...
    def end(self) -> None: ...


class WeatherStation:
    def __init__(self):
        self.observers: list[WeatherStationProtocol] = []
        self.temperature = 0.0

    def add_observer(self, observer: WeatherStationProtocol):
        self.observers.append(observer)

    def remove_observer(self, observer: WeatherStationProtocol):
        self.observers.remove(observer)

    def set_temperature(self, temperature: float ):
        if temperature != self.temperature:
            self.temperature = temperature
            self.notifyALL(temperature = self.temperature)

    def notifyALL(self, temperature: float):
        for observer in self.observers:
            observer.temperatureUpdated(newTemperature = temperature)
    

class JoaquinWeatherApp:
    def temperatureUpdated(self, newTemperature: float):
        print(f"Joaquin Mudou o tempo {newTemperature}")


class CachorroWeatherApp:
    def temperatureUpdated(self, newTemperature: float):
        print(f"O Cachorro controla o tempo! {newTemperature}" )

   

# ---- Exemplo de uso ----
station = WeatherStation()
joaquin = JoaquinWeatherApp
cachorro = CachorroWeatherApp
station.add_observer(observer = joaquin)
station.add_observer (observer  = cachorro)

station.set_temperature(temperature = 80.0)
