class GameSettings:
    _instance = None

    def __init__(self):
        self.volume = 50
        self.difficulty = "Medium"

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = GameSettings()
        return cls._instance


if __name__ == "__main__":
    settings1 = GameSettings.get_instance()
    settings2 = GameSettings.get_instance()

    print(settings1 is settings2)

    settings1.volume = 70
    settings1.difficulty = "Hard"

    print(settings2.volume)
    print(settings2.difficulty)
