# Python Lambda Functions — README (Do’s & Don’ts + Passing Lambdas)

A **lambda** in Python is an **anonymous (nameless) function** written in one line.

---

## 1) Syntax

```python
lambda arguments: expression
```

- A lambda can contain **only one expression**
- The expression’s value is automatically returned

Example:
```python
add = lambda a, b: a + b
print(add(2, 3))  # 5
```

---

## 2) Lambda vs normal function (`def`)

### Using `def`
```python
def add(a, b):
    return a + b
```

### Using `lambda`
```python
add = lambda a, b: a + b
```

> **Best practice:** use `def` for anything non-trivial or reused often.

---

## 3) Most common real use: `key=` in sorting

```python
people = [{"name": "Ilan", "age": 30}, {"name": "Bala", "age": 25}]
people.sort(key=lambda p: p["age"])
print(people)
```

---

## 4) Passing a lambda as a parameter (custom function)

In Python, functions are **first-class** objects, so you can pass a lambda just like a variable.

### Example: `apply()`
```python
def apply(op, x, y):
    return op(x, y)

result = apply(lambda a, b: a * b, 3, 4)
print(result)  # 12
```

### Example: transform items
```python
def transform_list(items, func):
    return [func(x) for x in items]

print(transform_list([1, 2, 3], lambda x: x * x))  # [1, 4, 9]
```

---

## 5) Built-in higher-order functions: `map` and `filter`

```python
nums = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))

print(squares)  # [1, 4, 9, 16, 25]
print(evens)    # [2, 4]
```

> Many Python developers prefer list comprehensions for readability:
```python
squares = [x * x for x in nums]
evens = [x for x in nums if x % 2 == 0]
```

---

## 6) Do’s ✅

### ✅ Do: keep it short and obvious
```python
key_fn = lambda p: p["age"]
```

### ✅ Do: use for one-off small logic
```python
nums.sort(key=lambda x: x)
```

### ✅ Do: use conditional expression (still one expression)
```python
label = lambda n: "adult" if n >= 18 else "minor"
print(label(20))
```

### ✅ Do: pass lambdas into your own helper functions
```python
def run_twice(fn, x):
    return fn(fn(x))

print(run_twice(lambda n: n + 1, 5))  # 7
```

---

## 7) Don’ts ❌

### ❌ Don’t write complex logic in lambda
Bad (hard to read):
```python
# lambda x: (x*2 if x>10 else x/2) + (x%3)
```
Better:
```python
def compute(x):
    if x > 10:
        return (x * 2) + (x % 3)
    return (x / 2) + (x % 3)
```

### ❌ Don’t try multi-line statements in lambda
Python lambdas cannot contain statements like `for`, `while`, assignment, `try`, etc.

Bad (not allowed):
```python
# lambda x:
#     y = x + 1
#     return y
```
Use `def` instead.

### ❌ Don’t overuse `map/filter` if list comprehension is clearer
Readable Python often prefers:
```python
[x * x for x in nums]
[x for x in nums if x % 2 == 0]
```

---

## 8) Type hints (optional but useful)

If you want type hints for a function that accepts a lambda/function:

```python
from typing import Callable

def apply(op: Callable[[int, int], int], x: int, y: int) -> int:
    return op(x, y)
```

---

## 9) Quick summary

- `lambda` = **one-line anonymous function**
- Great for: `key=`, small one-off transformations
- Not great for: complex logic → use `def`
- You can pass lambdas into custom functions because functions are values in Python
