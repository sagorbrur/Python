class Cars:
   'Common base class for all cars'
   car_count = 0
   def __init__(self, company_name, model_name, car_color):
      self.company_name = company_name
      self.model_name = model_name
      self.car_color = car_color
      Cars.car_count += 1

   def displayCount(self):
     print ("Total Cars %d" % Cars.car_count) 

   def displayCars(self):
      print("Company Name : ", self.company_name,  ", Model Name: ", self.model_name, ", Car Color: ", self.car_color)
      

# Creating Instance Object-01
car_01 = Cars("Maruthi_Suzuki", "Alto", "Black")

# Creating Instance Object-02
car_02 = Cars("Hundai", "i20", "White")

# Accessing Attributes
car_01.displayCars()
car_02.displayCars()
print("Total Cars %d" % Cars.car_count)

# Adding New Attributes
car_01.wheel_brand = 'MRF'
car_02.wheel_brand = 'JK Tyres'

#Deleting Attributes
del car_01.car_color
print('Now car_01.car_color attribute is removed from the class Cars...')
print('Following statement is commented because attribute "car_01.car_color" is removed so following statement as it throws an error. I have added another statement for car_02')
#car_01.displayCars()
car_02.displayCars()
