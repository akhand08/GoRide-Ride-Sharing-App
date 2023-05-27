


class RideManager:
    def __init__(self, ) -> None:
        print("Ride Manager Activated")
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cng = []
        
        
    def add_a_vehicle(self, vehicle_type, vehicle):
        if vehicle_type == "car":
            self.__available_cars.append(vehicle)
        if vehicle_type == "bike":
            self.__available_bikes.append(vehicle)
        if vehicle_type == "cng":
            self.__available_cng.append(vehicle)
            
            
            
    def get_available_cars(self):
        return self.__available_cars
        
        
    def find_a_vahicle(self, rider, vehicle_type, destination):
        if vehicle_type == "car":
            if len(self.__available_cars) == 0:
                print("Sorry no car available right now")
                return False
            for car in self.__available_cars:
                print(rider.location , car.driver.location , "  potential "  )
                if abs(rider.location - car.driver.location) < 200:
                    dis = abs(rider.location - car.driver.location)
                    fare = dis * car.rate
                    if car.status == 'available':
                        car.status = 'occupied'
                        self.__available_cars.remove(car)
                        print("Find a match")
            print("Looping done")
    
    
    
    
goRide = RideManager()