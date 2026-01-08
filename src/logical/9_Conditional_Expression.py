# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                 Print or assign one of two values based on a condition
#                 X if condition else Y



# Python ternary operator— officially it’s called a conditional expression.

# Syntax:
# value_if_true if condition else value_if_false

def main()->None:
    x = input("Please enter your age: ")
    if x.isdecimal():
        x = int(x)
        message = "Right to vote" if x >= 18 else "Can not vote"

    else:
        message = "Please enter the number"

    print(f"{message}")


if __name__ == "__main__":
    main()
