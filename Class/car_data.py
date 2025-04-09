class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = modelz
        self.year = year

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now running!")

    def stop_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now off!")

# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2022)

# Call methods on the object
my_car.start_engine()
my_car.stop_engine()
