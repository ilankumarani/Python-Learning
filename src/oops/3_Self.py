
import string

class Car:

    def __init__(self, make: string = "Toyota", model: string = "Rav4", year: int = 1989,
                 color: string = "Red") -> None:
        self.make = make  # instance variable
        self.model = model  # instance variable
        self.year = year  # instance variable
        self.color = color  # instance variable

    def get_colour(self) -> string:
        return self.color


def main() -> None:
    car_1 = Car("BMW", "Lola", 2002, "White")
    print(f"car_1 is instance of Car? :: {isinstance(car_1, Car)}")
    print(f"type(car_1) is Car?        :: {type(car_1) is Car}")

    car_2 = Car("Benz", "Lola", 2026, "Green")
    print(f"car_2 is instance of Car? :: {isinstance(car_2, Car)}")
    print(f"type(car_2) is Car?        :: {type(car_2) is Car}")


if __name__ == "__main__":
    main()
