class LightingSystem:
    @staticmethod
    def turn_on_main_lights():
        return "Основное освещение включено"

    @staticmethod
    def turn_off_main_lights():
        return "Основное освещение выключено"

    @staticmethod
    def dim_lights(level):
        return f"Освещение приглушено до {level}%"

    @staticmethod
    def turn_on_night_lights():
        return "Ночное освещение включено"


class ClimateControlSystem:
    @staticmethod
    def set_comfort_temperature():
        return "Установлена комфортная температура (22°C)"

    @staticmethod
    def set_party_temperature():
        return "Установлен вечеринный режим (20°C)"

    @staticmethod
    def set_night_temperature():
        return "Установлена ночная температура (18°C)"

    @staticmethod
    def turn_off():
        return "Климат-контроль выключен"


class SecuritySystem:
    @staticmethod
    def arm():
        return "Сигнализация включена"

    @staticmethod
    def disarm():
        return "Сигнализация выключена"

    @staticmethod
    def get_status():
        return "Статус системы безопасности"


class MultimediaSystem:
    @staticmethod
    def play_music(playlist):
        return f"Включена музыка: {playlist}"

    @staticmethod
    def stop_music():
        return "Музыка выключена"

    @staticmethod
    def set_volume(level):
        return f"Громкость установлена на {level}%"


class SmartHomeFacade:
    def __init__(self):
        self.lighting = LightingSystem()
        self.climate = ClimateControlSystem()
        self.security = SecuritySystem()
        self.multimedia = MultimediaSystem()

    def home_mode(self):
        results = [
            self.lighting.turn_on_main_lights(),
            self.climate.set_comfort_temperature(),
            self.security.disarm(),
            self.multimedia.stop_music()
        ]
        return results

    def away_mode(self):
        results = [
            self.lighting.turn_off_main_lights(),
            self.climate.turn_off(),
            self.security.arm(),
            self.multimedia.stop_music()
        ]
        return results

    def party_mode(self):
        results = [
            self.lighting.dim_lights(50),
            self.climate.set_party_temperature(),
            self.security.disarm(),
            self.multimedia.play_music("Party Mix"),
            self.multimedia.set_volume(70)
        ]
        return results

    def night_mode(self):
        results = [
            self.lighting.turn_off_main_lights(),
            self.lighting.turn_on_night_lights(),
            self.climate.set_night_temperature(),
            self.security.arm(),
            self.multimedia.stop_music()
        ]
        return results

    def get_all_systems_status(self):
        return (
            "Состояние систем:\n"
            f" - {self.lighting.turn_off_main_lights()}\n"
            f" - {self.climate.turn_off()}\n"
            f" - {self.security.get_status()}\n"
            f" - {self.multimedia.stop_music()}"
        )


def main():
    print("=== Тестирование паттерна Фасад для умного дома ===")

    smart_home = SmartHomeFacade()

    print("\n1. Начальное состояние всех систем:")
    print(smart_home.get_all_systems_status())

    print("\n2. Активация режима 'Я дома':")
    home_results = smart_home.home_mode()
    for result in home_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Я дома':")
    print(smart_home.get_all_systems_status())

    print("\n3. Активация режима 'Вечеринка':")
    party_results = smart_home.party_mode()
    for result in party_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Вечеринка':")
    print(smart_home.get_all_systems_status())

    print("\n4. Активация режима 'Ночь':")
    night_results = smart_home.night_mode()
    for result in night_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Ночь':")
    print(smart_home.get_all_systems_status())

    print("\n5. Активация режима 'Я ухожу':")
    away_results = smart_home.away_mode()
    for result in away_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Я ухожу':")
    print(smart_home.get_all_systems_status())

    print("\n=== Тестирование завершено ===")


if __name__ == "__main__":
    main()
