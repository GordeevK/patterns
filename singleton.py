class GameSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.volume = 50  # Значение по умолчанию
            cls._instance.difficulty = "Medium"  # Значение по умолчанию
        return cls._instance

    @classmethod
    def get_instance(cls):
        """Альтернативный способ получения экземпляра"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


if __name__ == "__main__":
    settings1 = GameSettings.get_instance()
    settings2 = GameSettings.get_instance()

    print(settings1 is settings2)

    settings1.volume = 70
    settings1.difficulty = "Hard"

    print(settings2.volume)
    print(settings2.difficulty)
