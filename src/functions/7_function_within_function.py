def get_full_name(first_name, last_name):
    def get_first_name(x):
        return x.strip()

    def get_last_name(y):
        return y.strip()

    return get_first_name(first_name) + " " + get_last_name(last_name)


if __name__ == "__main__":
    full_name = get_full_name("Ilankumaran", "Ilangovan");
    print(f"Full name :: {full_name}")
