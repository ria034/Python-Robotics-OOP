class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power
class Wheel:
    def __init__(self, wheel_size):
        self.wheel_size= wheel_size
    
class Car:
    def __init__(self,make,model,horse_power, size ):
        self.make = make 
        self.model = model 
        self.horse_power =Engine (horse_power)
        self._size = Wheel(size)
    def disp_car(self):
        print (f"The car is {self.make} {self.model} model with {self.horse_power.horse_power}hp and wheel size of {self._size.wheel_size} inches")



car1 =Car("Ford", "Mustang",500, 18)
car2 = Car("Porsche911", "Cayenne", 800, 20)
print(car1.disp_car())
print(car2.disp_car())