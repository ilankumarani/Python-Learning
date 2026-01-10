import string


class Car:
    wheels: int = 0  # class variable (Static variable in java) (Shared across the Objects)

    def __init__(self, make: string = "Toyota", model: string = "Rav4", year: int = 1989,
                 color: string = "Red") -> None:
        self.make = make  # instance variable
        self.model = model  # instance variable
        self.year = year  # instance variable
        self.color = color  # instance variable




def main() -> None:
    Car.wheels = 4
    car_1 = Car(color="White")

    car_2 = Car(color="Blue")
    car_2.wheels = 8

    print(f"car_1 Wheels :: {car_1.wheels}", f"car_2 Wheels :: {car_2.wheels}", sep=", ", end=" !!!")


if __name__ == "__main__":
    main()
