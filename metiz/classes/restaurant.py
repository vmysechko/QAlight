class Restaurant():
    """Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant " + self.restaurant_name.title() + " is a "
              + self.cuisine_type + " restaurant.")

    def open_restaurant(self):
        print("Restaurant is open.")

    def set_number_served(self, served_guests):
        if self.number_served <= served_guests:
            self.number_served = served_guests
        else:
            print("You can`t decrease number of served guests - " + str(self.number_served))

    def increment_number_served(self, served_guests):
        self.number_served += served_guests


pashtet = Restaurant("Pashtet", "mexican")
pashtet.describe_restaurant()
pashtet.open_restaurant()
print(pashtet.number_served)

pashtet.set_number_served(10)
print(pashtet.number_served)

pashtet.increment_number_served(5)
print(pashtet.number_served)

pashtet.set_number_served(5)
