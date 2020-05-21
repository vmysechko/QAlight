from car import Car


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery():
    """Простая модель аккумулятора"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def set_battery_size(self, battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            ev_range = 240
        elif self.battery_size > 70:
            ev_range = 270
        elif self.battery_size < 70:
            ev_range = 200

        message = "This car can drive approximately " + str(ev_range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size <= 70:
            self.battery_size = 85
        else:
            print("You have the best battery size: " + str(self.battery_size) + "kWh")
