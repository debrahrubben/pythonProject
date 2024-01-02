class Car:
   wheels=4
   def __init__(self,make,color,model,year):
       self.make = make
       self.model = model
       self.color = color
       self.year = year

   def drive(self):
        print('This '+self.model+' is driving')
   def stop(self):
        print('This '+self.model+' has stopped')