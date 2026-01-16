
class CPU: 
    def __init__(self, cores, frequency):
        self.cores = cores 
        self.frequency = frequency 
class PowerUnit: 
    def __init__(self, capacity, voltage):
        self.capacity = capacity 
        self.voltage = voltage
class Robot: 
    def __init__(self, cores,frequency,capacity,voltage):
        
        self.frequency = CPU (cores,frequency )
        self.capacity = PowerUnit(capacity, voltage)
       
    def display_specs(self):
        print(f"Robot hasa CPU with {self.frequency.cores} cores at {self.frequency.frequency} GHz and Power Unit of {self.capacity.capacity} mAh at {self.capacity.voltage}")

robot  =  Robot (8,3.2,5000, 12)
robot.display_specs()