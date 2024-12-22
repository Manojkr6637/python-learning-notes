class Car:
    total_car = 0
    def __init__(self, brand, model):
         self.__brand = brand
         self.model = model
        #  self.total_car +=1 
         Car.total_car +=1 
    def full_detail(self):
        return f"{self.__brand}-{self.model}"
    def get_brand(self):
        return f"{self.__brand}"
    # def get_decription(self):
        #  return 'All descriptions'
    @staticmethod    
    def get_decription():
        return 'All descriptions'      
    
    # def brand(self):
    #      return self.__brand #private
    @property
    def brand(self):
         return self.__brand 
        

class ElectricCar(Car):
    def __init__(self, brand, model, battery): 
         super().__init__(brand, model)   
         self.battery=battery
          

# my_car =  Car('Manoj','33', '80KWH')

# print(my_car.name)

# # print(my_car.full_detail())
# teslaCar = ElectricCar('Telsa', 'RX500', '80KWH')

# # print(teslaCar.full_detail())
# print(teslaCar.get_decription())
# print(isinstance(teslaCar, ElectricCar))


class Engine:
    def battery_info(self):
      return 'This is Battery info'
class Electric:
     def engine_info(self):
      return 'This is engine info'

class TwoWheel(Engine, Electric, Car):
       pass
   
two = TwoWheel('Tata', 'Tiango')
print(two.battery_info())