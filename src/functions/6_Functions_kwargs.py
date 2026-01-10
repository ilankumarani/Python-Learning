def full_name(**kwargs):
    if "first_name" in kwargs and "last_name" in kwargs:
        print(f"firstName :: {kwargs.get('first_name')} , lastName :: {kwargs['last_name']}")
    return kwargs;


if __name__ == "__main__":
    x = full_name(first_name="Ilankumaran", last_name="Ilangovan");
    print(f"{type(x)}")
