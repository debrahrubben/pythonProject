from Car import Car
car_1 = Car('chevy','blue','Corvette','2021')
car_2 = Car('Ford','red','Mustang','2022')

print(car_1.year,car_1.model,car_1.color,car_1.make)
car_1.stop()
car_2.drive()
car_1.wheels = 2

print(car_1.wheels)