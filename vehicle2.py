class Vehicle:

 def __init__(self, name, license, color, fuel):
    self.name = name
    self.license = license
    self.color = color
    self.fuel = fuel
 
 def display_info(self):
        print(f"Name: {self.name}")
        print(f"License: {self.license}")
        print(f"Color: {self.color}")
        print(f"Fuel: {self.fuel}")
  
class Car(Vehicle):
    def __init__(self, name, license, color, fuel, wheel_num):
     super().__init__(name, license, color, fuel)
     self.wheel_num = wheel_num
    
    def display_info(self):
        super().display_info()
        print(f"Number of wheels: {self.wheel_num}")
class Motorcycle(Vehicle):
    def __init__(self, name, license, color, fuel, wheel_num):
     super().__init__(name, license, color, fuel)
     self.wheel_num = wheel_num
    
    def display_info(self):
        super().display_info()
        print(f"Number of wheels: {self.wheel_num}")

my_vehicle = Vehicle("Toyota", 3456, "Blue" , "petroleum")

my_vehicle.display_info()

# Example usage:
car = Car("Toyota", "3456", "Blue", "petroleum", 4)
car.display_info()

motorcycle = Motorcycle("Honda", "7890", "Red", "gasoline", 2)
motorcycle.display_info()