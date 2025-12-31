# Python ternary operator— officially it’s called a conditional expression.

# Syntax:
# value_if_true if condition else value_if_false

x = int(input("Please enter your age: "))
message = "Right to vote" if x >= 18 else "Can not vote"

print(f"{message}")
