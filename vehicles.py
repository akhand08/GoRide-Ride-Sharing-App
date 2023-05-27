from abc import ABC, abstractmethod

class Vehicle():
    
    speed = { "car": 50, "bike": 30, "cng": 40}
    
    def __init__(self, type,license_plate, driver, rate) -> None:
        self.type = type
        self.rate = rate
        self.driver = driver
        self.speed = Vehicle.speed[type]
        self.license_plate = license_plate
        self.status = "available"
    
    
    @abstractmethod
    def start_driving(self):
        pass
    
    
    @abstractmethod
    def trip_finished(self):
        pass
    
    
    
    
    
class Car(Vehicle):
    def __init__(self, type,license_plate, driver, rate) -> None:
        super().__init__(type, license_plate, driver, rate)
        
    
    def start_driving(self):
        print(self.type, " ", self.license_plate, " Started")
        self.status = "occupied"
        return super().start_driving()
    
    def trip_finished(self):
        print(self.type, " ", self.license_plate, " trip finished " )
        self.status = "available"
    
    
    
    
    
    
class Cng(Vehicle):
    def __init__(self, type,license_plate, driver, rate) -> None:
        super().__init__(type, license_plate, driver, rate)
        
    
    def start_driving(self):
        print(self.type, " ", self.license_plate, " Started")
        self.status = "occupied"
        return super().start_driving()
    
    def trip_finished(self):
        print(self.type, " ", self.license_plate, " trip finished " )
        self.status = "available"
    
    
    
    
    
    
    
class Bike(Vehicle):
    def __init__(self, type,license_plate, driver, rate) -> None:
        super().__init__(type, license_plate, driver, rate)
        
    
    def start_driving(self):
        print(self.type, " ", self.license_plate, " Started")
        self.status = "occupied"
        return super().start_driving()
    
    def trip_finished(self):
        print(self.type, " ", self.license_plate, " trip finished " )
        self.status = "available"
    