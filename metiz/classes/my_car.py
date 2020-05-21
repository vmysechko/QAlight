from metiz.classes.car import Car

my_new_car = Car('mazda', '3', 2014)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 37
my_new_car.read_odometer()