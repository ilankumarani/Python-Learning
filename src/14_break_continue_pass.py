"""loop_control_examples.py

Run:
    python loop_control_examples.py
"""

def break_example():
    print("\n=== break example ===")
    numbers = [3, 8, 2, 9, 5]
    target = 9

    for n in numbers:
        print("checking:", n)
        if n == target:
            print("found target, stopping")
            break


def continue_example():
    print("\n=== continue example ===")
    items = ["10", "x", "25", "", "7"]

    total = 0
    for s in items:
        if not s.isdigit():
            print("skipping:", repr(s))
            continue

        total += int(s)
        print("added:", s)

    print("total =", total)


def pass_example():
    print("\n=== pass example ===")
    age = 17

    if age >= 18:
        print("Adult")
    else:
        pass  # placeholder: do nothing

    print("done (notice there was no output from the else branch)")


if __name__ == "__main__":
    break_example()
    continue_example()
    pass_example()
