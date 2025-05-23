# __init__ used to create an constructor for the class in python
# The __init__ method is a special method that is called when an object is created. It is used to initialize the object's attributes.   
# self is a reference to the current instance of the class. It is used to access the attributes and methods of the class.
# The self parameter is always the first parameter of the __init__ method and any other methods in the class.

class Car:
    
    total_car = 0 # Class variable to keep track of the number of car objects created
    
    def __init__(self , brand , model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        
    def getBrand(self):
        return self.__brand

    def getCarInfo(self):
        return f"{self.__brand} {self.__model}"
    
    def fuelType(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def carDescription():
        return f"car is used for transportation"
    
    @property
    def brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model


class Battery:
    def info(self):
        return "Battery information"

class Engine:
    def engineInfo(self):
        return "Engine information"


class ElecticCar(Car, Battery, Engine):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size

    def getCarInfo(self):
        return f"{super().getCarInfo()} with {self.battery_size} kWh battery"
    
    def getBatterySize(self):
        return f"{self.battery_size} kWh"
    
    def fuelType(self):
        return "Electric charge"

# my_car = Car("Toyota" , "Corolla")
# print(my_car.brand) # Toyota
# print(my_car.model) # Corolla
# print(my_car.getCarInfo()) # Toyota Corolla


my_electric_car = ElecticCar("Tesla" , "Model S" , 100)
print(my_electric_car.info())
print(my_electric_car.engineInfo())
# print(my_electric_car.brand) # Tesla    
# print(my_electric_car.model) # Model S
# print(my_electric_car.battery_size) # 100
# print(my_electric_car.getCarInfo()) # Tesla Model S with 100 kWh battery

# my_electric_car = ElecticCar("Tesla" , "Model S" , 100)
# print(my_electric_car.fuelType())
# print(isinstance(my_electric_car , Car)) # True
# print(isinstance(my_electric_car , ElecticCar)) # True


# my_car = Car("Toyota" , "Corolla")
# print(my_car.fuelType())
# print(my_car.carDescription())
# print(Car.carDescription())
# my_car.brand = "Honda" # This will raise an error because brand is a private attribute

# print(my_car.brand)
# print(my_car.model)
# print(isinstance(my_car , Car)) #- True
# print(isinstance(my_car , ElecticCar)) # - False
