

class Car:
    pass


if __name__ == "__main__":
    c = Car()
    print("\nMRO for D:")
    for cls in Car.mro():
        print(" -", cls.__name__)