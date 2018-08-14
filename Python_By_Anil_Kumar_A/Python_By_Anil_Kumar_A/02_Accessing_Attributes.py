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
