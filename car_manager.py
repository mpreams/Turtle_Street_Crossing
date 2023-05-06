from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.increment = STARTING_MOVE_DISTANCE

    def create_car(self):
        make_if = random.randint(1, 5)
        if make_if == 1:
            new_car = Turtle("square")
            car_color = random.choice(COLORS)
            new_car.color(car_color)
            new_car.penup()
            new_car.setheading(180)
            new_car.setx(300)
            new_car.sety(random.randint(-240, 280))
            new_car.shapesize(stretch_len=2)
            self.cars.append(new_car)


    def move(self):
        for car in self.cars:
            car.forward(self.increment)

    def faster(self):
        self.increment += MOVE_INCREMENT










