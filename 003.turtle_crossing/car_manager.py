from random import choice, randint
from car import Car
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        random_making_car = randint(1,5)
        if random_making_car != 1:
            return
        self.all_cars.append(Car())

    def move_cars(self):
        for car in self.all_cars:
            car.backward(car.move_distance)

