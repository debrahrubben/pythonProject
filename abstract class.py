from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
class Car(vehicle):
    def __ge__(self, other):
        print('You drive the car')