from metiz.classes.electric_car import ElectricCar

my_electric_car = ElectricCar('renault', 'zoa', 2015)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()
my_electric_car.battery.upgrade_battery()
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()
