def full_name(**kwargs):
    print(f"firstName :: {kwargs.get('first_name')} , lastName :: {kwargs['last_name']}")
    return kwargs;

x = full_name(first_name="Ilankumaran", last_name="Ilangovan");

print(f"{type(x)}")
