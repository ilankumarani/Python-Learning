
from dataclasses import dataclass

@dataclass
class Car:
    make: str
    model: str




def main() -> None:
    print([n for n in dir(Car) if not n.startswith("_")])
    c1 = Car("Toyota", "Rav4")
    c2 = Car("Toyota", "Rav4")
    print(c1)  # Car(make='Toyota', model='Rav4')  (nice __repr__)
    print(c1 == c2)  # True (value-based __eq__)


if __name__ == "__main__":
    main()