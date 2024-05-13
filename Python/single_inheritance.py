class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print("Brand:", self.brand)
        print("Year:", self.year)


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def display_info(self):
        super().display_info()
        print("Model:", self.model)


# Creating an instance of the Car class
car = Car("Toyota", 2022, "Camry")

# Calling the display_info method of the Car class
car.display_info()
