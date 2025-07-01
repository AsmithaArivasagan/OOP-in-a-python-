from abc import ABC ,abstractmethod
class Car(ABC):
    def __init__(self,model,year,speed,carnumber):
        self.model=model
        self.year=year
        self.speed=speed
        self.__carnumber=carnumber
    def get_carnumber(self):
        return self.__carnumber
    def set_carnumber(self,new_number):
        self.__carnumber=new_number
    @abstractmethod
    def drive(self):
         pass
class ElectricCar(Car):
    def drive(self):
        print("Model:",self.model)
        print("Year:",self.year)
        print("speed:",self.speed)
        print("carnumber:",self.get_carnumber())
        print(f"{self.model}  an electric car moves silently and smoothly with no engine sound.")
class PetrolCar(Car):
    def drive(self):
        print("Model:",self.model)
        print("Year:",self.year)
        print("speed:",self.speed)
        print("carnumber:",self.get_carnumber())
        print(f"{self.model} a petrol car moves quickly with a light engine sound and smooth pickup.")
class DieselCar(Car):
    def drive(self):
        print("Model:",self.model)
        print("Year:",self.year)
        print("speed:",self.speed)
        print("carnumber",self.get_carnumber())
        print(f"{self.model} a diesel car moves powerfully with a loud, deep engine sound.")
car1=ElectricCar("Tata Nexon ",2020,"120 km/h","TN01AB1234")
car2=PetrolCar("Maruti Suzuki swift",2005,"160 km/h","TN10CD5678")
car3=DieselCar("Mahendra Bolero",2000,"125 km/h","TN22EF9012")
car1.drive()
print()
car2.drive()
print()
car3.drive()

