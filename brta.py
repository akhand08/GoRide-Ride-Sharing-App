import random


class Brta:
    def __init__(self):
        self.__license = { }
        
    
    def driving_test(self, email):
        score = random.randint(0,100)
        if score > 33:
            print("congrats, you have passed")
            license_no = random.randint(5000,9999)
            self.__license[email] = license_no
            return license_no
        else:
            print("Sorry you failed")
            return False
        
        
    def validate_license(self, email, license_no):
        for key, value in self.__license.items():
            if key == email and  license_no ==  value:
                print("Yes it is a valid license")
                return True
        
        return False