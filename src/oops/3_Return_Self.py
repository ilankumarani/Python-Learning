import string
from typing import Self, Type


class House:

    def __init__(self, make: string = "Toyota", model: string = "Rav4", year: int = 1989,
                 color: string = "Red") -> None:
        self.make = make  # instance variable
        self.model = model  # instance variable
        self.year = year  # instance variable
        self.color = color  # instance variable

    def get_instance(self) -> Self:
        return self

    def get_house_instance(self) -> Type["House"]:
        #return type(self)
        return self # (This is not correct)

    def get_car_instance(self) -> Type["Car"]:
        return type(self)


def main() -> None:
    house = House("BMW", "Lola", 2002, "White")
    print(f"house is instance of Car? :: {isinstance(house.get_instance(), House)}")
    print(f"type(house) is Car?        :: {type(house.get_house_instance()) is House}")
    print(f"type(car) is Car?        :: {type(house.get_car_instance()) is House}")


if __name__ == "__main__":
    main()
