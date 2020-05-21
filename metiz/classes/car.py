"""Класс для представления автомобиля"""


class Car():
    """Простая модель автомобиля."""

    def __init__(self, make: str, model: str, year: int):
        """Инициализирует атрибуты описания автомобиля.
        :type make: str
        :type model: str
        :type year: int
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """ Устанавливает на одометре заданное значение.
        При попытке обратной подкрутки изменение отклоняется. """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading += miles



