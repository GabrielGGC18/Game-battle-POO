class GameManager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.running = True
        return cls._instance
    def stop(self): self.running = False
