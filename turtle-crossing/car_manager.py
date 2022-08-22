from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:

    def __init__(self) -> None:
        self.cars = []
        self.used_cars = []
        self.create_cars()
        self.move_distance = STARTING_MOVE_DISTANCE

    def add_car(self, x_pos, car=None):
        if car == None:
            car = Turtle("square")
        car.color(random.choice(COLORS))
        car.penup()
        car.showturtle()
        car.shapesize(stretch_wid=1, stretch_len=3)
        car.goto(x_pos, random.randint(-250, 250))
        self.cars.append(car)

    def create_cars(self):
        num_cars = random.randint(5, 10)
        # print(f"creating {num_cars} cars")
        for i in range(num_cars, 0, -1):
            # print(f"on {i} car")
            # reuse used cars
            if i < len(self.used_cars):
                self.add_car(random.randint(-240, 300), self.used_cars.pop(i))
                # print("At the used car lot, baby!")
            else:
                self.add_car(random.randint(-240, 300))

    def move(self):
        for car in self.cars:
            car.setx(car.xcor() - self.move_distance)
            if car.xcor() < -260:
                car.hideturtle()
                self.cars.remove(car)
                self.used_cars.append(car)
                new_cars = random.randint(0, 2)
                for _ in range(new_cars):
                    self.add_car(random.randint(240, 300))

    def next_level(self):
        for car in self.cars:
            car.hideturtle()
            car.setx(300)
            self.cars.remove(car)
            self.used_cars.append(car)
        # self.cars.clear()
        self.move_distance += MOVE_INCREMENT
        self.create_cars()
