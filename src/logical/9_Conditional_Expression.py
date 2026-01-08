# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                 Print or assign one of two values based on a condition
#                 X if condition else Y
import logging


# Python ternary operator— officially it’s called a conditional expression.

# Syntax:
# value_if_true if condition else value_if_false

def main()->None:
    x = input("Please enter your age: ")
    message = "*** Right to vote ***!!!" if x.isdecimal() and x >= 18 else """May be you have Entered is not a number 
    (or) 
    Can not vote"""
    print(f"{message}")


if __name__ == "__main__":
    main()
