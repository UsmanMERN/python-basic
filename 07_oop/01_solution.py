class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "  !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "petrol or Deisel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    # @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Modal S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.general_description())
# print(Car.general_description())

# my_tesla.model = "IDK"
# print(my_tesla.model())
# print(my_tesla.fuel_type())

# safari = Car("Tata", "Safari")
# safari3 = Car("Tata", "Nexon")
# print(safari.fuel_type())
# print(Car.total_car)

# print(my_tesla.full_name())


# my_car = Car("Toyota", "Corolla")
# my_new_car = Car("TATA", "Safari")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())


class Battery:
    def batter_info(self):
        return "This is battery class"


class Engine:
    def engine_info(self):
        return "This is Engine class"


class ElectriCarTwo(Battery, Engine, Car):
    pass


my_new_tesla = ElectriCarTwo("Tesla", "Model S")

print(my_new_tesla.batter_info())
print(my_new_tesla.engine_info())
