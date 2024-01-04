class Car:
    def turn_on(self):
        print('You start the engine')
        return self
    def drive(self):
        print('You drive the car')
        return self
    def brake(self):
        print('you step on the brakes')
        return self

car = Car()

(car.turn_on()
 .drive())