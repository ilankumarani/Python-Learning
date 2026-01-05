"""nested_loops_examples.py

Run:
    python nested_loops_examples.py

This file demonstrates nested loops with:
1) A grid printer (rows x columns)
2) A multiplication table
"""

def grid_printer():
    print("\n=== Grid Printer (nested loops) ===")

    rows = int(input("How many rows?: "))
    columns = int(input("How many columns?: "))
    symbol = input("Enter a symbol to use: ")

    for i in range(rows):
        for j in range(columns):
            print(symbol, end="")
        print()  # new line after each row


def multiplication_table():
    print("\n=== 5x5 Multiplication Table (nested loops) ===")

    for i in range(1, 6):
        for j in range(1, 6):
            # :2 pads the number to width 2 for alignment
            print(f"{i*j:2}", end=" ")
        print()


if __name__ == "__main__":
    grid_printer()
    multiplication_table()
