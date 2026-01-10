import logging
import string
from typing import Self, Type

from src.oops.Car_Constructor import Car as Car


class Car:
    wheels: int = 0  # class variable (Static variable in java) (Shared across the Objects)

    def __init__(self, make: string = "Toyota", model: string = "Rav4", year: int = 1989,
                 color: string = "Red") -> None:
        self.make = make  # instance variable
        self.model = model  # instance variable
        self.year = year  # instance variable
        self.color = color  # instance variable


Car.wheels = 4

car_1 = Car(color="White")
print(f"{car_1.get_colour()}")
logging.log("tesst")
print(f"---->{car_1 is car_1.get_instance(), type(car_1.get_instance())}")
print(f"++++>{car_1 is car_1.get_current_instance(), type(car_1.get_current_instance())}")
print(f"{car_1.get_current_instance().color}")

car_2 = Car(color="Blue")
car_2.wheels = 8
print(f"{car_2.get_colour()}")
print(f"{car_2.get_current_instance().color}")

print(f"{car_1.wheels, car_2.wheels}")
