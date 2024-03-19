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
  
my_vehicle = Vehicle("Toyota", 3456, "Blue" , "petroleum")

my_vehicle.display_info()