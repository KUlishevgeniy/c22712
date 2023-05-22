from time import time, sleep
from random import random

class Car:
    def __init__(self, model = "BMW 5 Седан", color = "Gray", volume = 50, consumption = 1):
        self.model = model
        self.color = color
        self.overall_volume = volume
        self.volume = volume
        self.consumption = consumption
    def start(self):
        self.start_time = int(time())
        return self.volume // self.consumption
    def stop(self):
        self.volume -= self.consumption * (int(time())- self.start_time)
        return self.volume
    def show_info(self):
        print(f"Model: {self.model}. Color: {self.color}. Overall volume: {self.overall_volume}. Volume left: {self.volume}")
car = Car(volume=20)
time_sleep = int(car.start()*random())
print(f"time of working: {time_sleep}")
sleep(time_sleep)
car.stop()
car.show_info()

