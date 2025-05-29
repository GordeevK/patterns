from abc import ABC, abstractmethod


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def __str__(self):
        return f"Engine: {self.engine_type}"


class Transmission:
    def __init__(self, transmission_type):
        self.transmission_type = transmission_type

    def __str__(self):
        return f"Transmission: {self.transmission_type}"


class Body:
    def __init__(self, body_type):
        self.body_type = body_type

    def __str__(self):
        return f"Body: {self.body_type}"


class Car:
    def __init__(self):
        self.brand = None
        self.model = None
        self.engine = None
        self.transmission = None
        self.body = None
        self.color = None

    def __str__(self):
        return (f"Car: {self.brand} {self.model}, "
                f"{self.engine}, {self.transmission}, "
                f"{self.body}, Color: {self.color}")


class CarBuilder(ABC):
    def __init__(self):
        self.car = Car()

    @abstractmethod
    def set_brand(self):
        pass

    @abstractmethod
    def set_model(self):
        pass

    @abstractmethod
    def set_engine(self):
        pass

    @abstractmethod
    def set_transmission(self):
        pass

    @abstractmethod
    def set_body(self):
        pass

    @abstractmethod
    def set_color(self):
        pass

    def get_car(self):
        return self.car


class SedanBuilder(CarBuilder):
    def set_brand(self):
        self.car.brand = "Toyota"

    def set_model(self):
        self.car.model = "Camry"

    def set_engine(self):
        self.car.engine = Engine("V6 3.5L")

    def set_transmission(self):
        self.car.transmission = Transmission("Automatic")

    def set_body(self):
        self.car.body = Body("Sedan")

    def set_color(self):
        self.car.color = "Silver"


class SUVBuilder(CarBuilder):
    def set_brand(self):
        self.car.brand = "Ford"

    def set_model(self):
        self.car.model = "Explorer"

    def set_engine(self):
        self.car.engine = Engine("EcoBoost 2.3L")

    def set_transmission(self):
        self.car.transmission = Transmission("Automatic 10-speed")

    def set_body(self):
        self.car.body = Body("SUV")

    def set_color(self):
        self.car.color = "Black"


class SportsCarBuilder(CarBuilder):
    def set_brand(self):
        self.car.brand = "Porsche"

    def set_model(self):
        self.car.model = "911"

    def set_engine(self):
        self.car.engine = Engine("Turbocharged Flat-6")

    def set_transmission(self):
        self.car.transmission = Transmission("PDK 7-speed")

    def set_body(self):
        self.car.body = Body("Coupe")

    def set_color(self):
        self.car.color = "Red"


class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.set_brand()
        self.builder.set_model()
        self.builder.set_engine()
        self.builder.set_transmission()
        self.builder.set_body()
        self.builder.set_color()
        return self.builder.get_car()


if __name__ == "__main__":
    sedan_builder = SedanBuilder()
    director = CarDirector(sedan_builder)
    sedan = director.construct_car()
    print("Создан седан:", sedan)

    suv_builder = SUVBuilder()
    director = CarDirector(suv_builder)
    suv = director.construct_car()
    print("Создан внедорожник:", suv)

    sports_builder = SportsCarBuilder()
    director = CarDirector(sports_builder)
    sports_car = director.construct_car()
    print("Создан спорткар:", sports_car)
