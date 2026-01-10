import string


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return "..."  # default / generic

    def eat(self, food: str) -> None:
        print(f"{self.name} eats {food}")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self) -> str:  # override
        return "Woof!"

class Cat(Animal):  # Cat inherits from Animal
    def speak(self) -> str:  # override
        return "Meow!"

def main() -> None:
    animals: list[Animal] = [Dog("Rocky"), Cat("Mimi")]

    for a in animals:
        print(f"{a.name} says {a.speak()}")  # polymorphism (dynamic dispatch)
        a.eat("food")

if __name__ == "__main__":
    main()

