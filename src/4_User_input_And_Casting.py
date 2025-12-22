# input("Enter: ") is used to take input from the user through the console/terminal.

# "Enter: " is just a prompt message shown to the user.

# It waits until the user types something and presses Enter.

# It returns what the user typed as a string (str).

x = input("Enter: ")
print(type(x))   # <class 'str'>

age = int(input("Enter age: "))
salary = float(input("Enter salary: "))


print(f"Age ::{age} and type {type(age)}")
print(f"Salary ::{salary} and type {type(salary)}")