# Nested Loops in Python

A **nested loop** is a loop inside another loop.

- The **inner loop** runs *all of its iterations* for **each** single iteration of the **outer loop**.
- This is very useful for working with **rows & columns** (grids), **tables**, **patterns**, etc.

---

## What you had in the screenshot (typed out)

```python
# nested loops = The "inner loop" will finish all of it's iterations before
#                finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
```

---

## Example 1: Print a grid (rows × columns)

### Code

```python
rows = 3
columns = 5
symbol = "#"

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
```

### Output

```text
#####
#####
#####
```

**How it works (simple):**
- Outer loop runs 3 times → creates **3 lines**
- Inner loop runs 5 times each line → prints **5 symbols per line**

---

## Example 2: Multiplication table (1 to 5)

### Code

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:2}", end=" ")
    print()
```

### Output

```text
 1  2  3  4  5 
 2  4  6  8 10 
 3  6  9 12 15 
 4  8 12 16 20 
 5 10 15 20 25 
```

---

## Run the included Python file

This folder includes **`nested_loops_examples.py`**.

```bash
python nested_loops_examples.py
```

It will:
1. Run the **grid printer** using user input
2. Print a **5×5 multiplication table**
