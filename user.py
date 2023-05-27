import hashlib
from brta import Brta

from vehicles import Vehicle, Car, Cng , Bike
from ride_manager import goRide
from random import random,randint




license_authority = Brta()

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd_encrypt = hashlib.md5(password.encode()).hexdigest()
        
        with open("users.text", 'a') as file:
            file.write(f"{email} {pwd_encrypt} \n")
        file.close()
        print(self.name, "user created")
        
        
    @staticmethod
    def log_in(email, password):
        stored_pwd = ""        

        with open("users.text", 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    store_pwd = line.split(" ")[1]
                    
        file.close()
        
        hashed_pwd = hashlib.md5(password.encode()).hexdigest()
        if hashed_pwd == stored_pwd:
            print("password found")
        
                    



class Rider(User):
    def __init__(self, name, email, password, location, balance):
        super().__init__(name, email, password)
        self.location = location
        self.balance = balance
        
    def set_location(self, location):
        self.location = location
        
    def get_location(self):
        return self.location
    
    
    def request_a_trip(self, rider, vehicle_type, destination):
        if vehicle_type == "car":
            pass
    
    
    def start_a_trip(self, fare):
        self.balance -= fare
        
        
        
        
class Driver(User):
    def __init__(self, name, email, password, location, license, balance):
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(self.email, self.license)
        self.balance  = 0
        
        
        
    def take_driving_test(self):
        result = license_authority.driving_test(self.email)
        if result == False:
            print('Sorry you failed')
            self.valid_driver = False
        else:
            print("Congratulation! You achived driving license")
            self.valid_driver = True
            
            
    def register_a_vehicle(self, vehicle_type, license_plate , rate):
        if self.valid_driver is True:
            new_vehicle = None
            if vehicle_type == "car":
                new_vehicle = Car(vehicle_type, self.license, self, 50)
                goRide.add_a_vehicle(vehicle_type, new_vehicle)
            if vehicle_type == "bike":
                new_vehicle = Bike(vehicle_type, self.license, self, 50)
                goRide.add_a_vehicle(vehicle_type, new_vehicle)
            if vehicle_type == "cng":
                new_vehicle = Cng(vehicle_type, self.license, self, 50)
                goRide.add_a_vehicle(vehicle_type, new_vehicle)
                
                
            
        
        else:
            print("Please apply with a valid license")
        
        
    def start_a_trip(self, destination, fare):
        self.balance += fare
        self.location = destination
    
    
    
    
    
    
    
    
    
# riders

rider1 = Rider("rider1", "r1@gmail.com", "r1abcd", randint(0,1000), 100)
rider2 = Rider("rider2", "r2@gmail.com", "r2abcd", randint(0,1000), 100)
rider3 = Rider("rider3", "r3@gmail.com", "r3abcd", randint(0,1000), 100)
    
    
    
    
    
    
    
# drivers

driver1 = Driver("driver1", "d1@gmail.com", "d1abcd", randint(0,1000), randint(5000,9999), 100)
driver1.take_driving_test()
driver1.register_a_vehicle("car", driver1.license, 50)


driver2 = Driver("driver2", "d2@gmail.com", "d2abcd", randint(0,1000), randint(5000,9999), 100)
driver2.take_driving_test()
driver2.register_a_vehicle("car", driver2.license, 60)

driver3 = Driver("driver3", "d3@gmail.com", "d3abcd", randint(0,1000), randint(5000,9999), 100)
driver3.take_driving_test()
driver3.register_a_vehicle("car", driver3.license, 90)



print(goRide.get_available_cars())

goRide.find_a_vahicle(rider1, "car", 2232)