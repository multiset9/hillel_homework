# Создать класс Vehicle который будет описывать аттрибуты свойственные ему.
# Создать класс Bus который будет наследоваться от класса Vehicle
# Создать класс Car который будет наследоваться от класса Vehicle
#
# Вашей задачей, при формировании классов, будет достижение следующих целей
# 1)Общие методы и аттрибуты для Bus и Car имеет смысл определять в классе
# Vehicle
# 2)Используйте модификаторы доступа для ваших аттрибутов
# 3)Используйте @property для отдельных аттрибутов(например для проверки типа)


class Vehicle:
    def __init__(self, color, type_fuel, model, wheels):
        self.__color = color
        self._speed = 0
        self.__type_fuel = type_fuel
        self.model = model
        self.wheels = wheels

    @property
    def speed(self):
        return f"The current speed is: {self._speed}"

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def type_fuel(self):
        return f"Type fuel is: {self.__type_fuel}"

    def brake(self, value):
        self._speed -= value
        return f"The current speed after brake is: {self._speed}"


class Car(Vehicle):
    def __init__(self, color, type_fuel, model, wheels, trailer):
        super().__init__(color, type_fuel, model, wheels)
        self.trailer = trailer

    @property
    def is_trailer(self):
        return f"This car has a trailer {self.trailer}"


class Bus(Vehicle):
    def __init__(self, color, type_fuel, model, wheels, excursion):
        super().__init__(color, type_fuel, model, wheels)
        self.excursion = excursion

    def start_tour(self):
        if self.excursion:
            return "Tour will be soon"
        else:
            return "I'm not touristic bus!"


car1 = Car("yellow", "gasoline", "Sedan", 4, True)
car1.speed = 100
print(car1.speed)
car1.brake(50)
print(car1.speed)
print(car1.is_trailer)

bus1 = Bus("red", "gasoline", "Tourist", 6, False)
bus1.speed = 130
bus1.brake(10)
print(bus1.speed)
print(bus1.wheels)
print(bus1.start_tour())
bus1.excursion = True
print(bus1.start_tour())
