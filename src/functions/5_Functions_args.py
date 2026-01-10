def full_name(*args):
    print(f"firstName :: {args[0]} , lastName :: {args[1]}")
    return args;



if __name__ == "__main__":
    x = full_name("Ilankumaran", "Ilangovan");
    print(f"{type(x)}")

    # ❌ Will throw an error
    # x = full_name(first_name="Ilankumaran", last_name="Ilangovan");