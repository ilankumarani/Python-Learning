# `self` in Python — README (for Java Developers)

## What is `self`?
`self` is **the current object (instance)** passed into an *instance method*.

In Java you write:
```java
car.paint("Red");   // uses `this`
```

In Python, this:
```python
car.paint("Red")
```
is equivalent to:
```python
Car.paint(car, "Red")
```
So inside `paint`, the first parameter receives the object — by convention we call it `self`.

---

## Simple words (Java mapping)
- `self` ≈ **`this`**
- `self.x` ≈ **`this.x`**
- `self.method()` ≈ **`this.method()`**
- Python makes the receiver **explicit** in the method signature.

---

## Technical explanation (how binding works)
When you access an instance method like `car.paint`, Python produces a **bound method**:
- It remembers the function (`Car.paint`)
- It also remembers the instance (`car`)
- When called, it automatically supplies the instance as the first argument

So the method definition must include the first parameter (conventionally `self`):
```python
class Car:
    def paint(self, color: str) -> None:
        self.color = color
```

---

## The biggest “Java → Python” differences to know

### 1) `self` is **not a keyword**
You *could* write `def paint(me, color): ...` but **don’t**.
Use `self` for readability and consistency.

### 2) You MUST use `self.` to access instance fields/methods
In Java you can often omit `this.`.
In Python, you usually cannot.

✅ Correct:
```python
class Car:
    def __init__(self, make: str):
        self.make = make

    def show(self) -> None:
        print(self.make)
```

❌ Wrong (creates/uses a local variable, not a field):
```python
class Car:
    def __init__(self, make: str):
        make = make   # does nothing useful
```

### 3) Attributes can be created dynamically (power + danger)
This is valid Python:
```python
car.sunroof = True
```
If you make a typo, Python won’t stop you by default:
```python
self.colour = "Red"   # typo; creates a NEW attribute
```

**Tip:** Use type checking (mypy/pyright) and/or `__slots__` if you want stricter models.

### 4) “Overloading” isn’t like Java
Python doesn’t overload by signature. A method name is a single attribute.
Use default values, `*args/**kwargs`, or `functools.singledispatch` for variants.

### 5) References behave like Java object references
Variables hold references to objects (like Java). Mutating via `self` mutates that instance.

---

## Rules / Pin-point facts (the “must know” list)
1. In an **instance method**, the first parameter receives the instance (call it `self`).
2. `self` is passed automatically when you call `obj.method(...)`.
3. To read/write instance state, use `self.attribute`.
4. If you forget `self.` you’ll likely create a local variable (bug).
5. `self` is not special syntax; the **position** of the first parameter is what matters.
6. `@staticmethod` has **no `self`**. `@classmethod` uses **`cls`** instead of `self`.

---

## DO and DON’T (practical checklist)

### ✅ DO
- **Use `self` as the name** of the first parameter in instance methods.
- **Initialize instance attributes in `__init__`**:
  ```python
  class Car:
      def __init__(self) -> None:
          self.color = "Red"
  ```
- **Call other instance methods using `self`**:
  ```python
  def start(self) -> None:
      self._check_fuel()
      self._ignite()
  ```
- **Return `self` for fluent/builder style (common in Python too)**:
  ```python
  def set_color(self, color: str) -> "Car":
      self.color = color
      return self
  ```
- **Use `super()` for parent methods** (no `super.method(self, ...)` needed):
  ```python
  class ElectricCar(Car):
      def start(self) -> None:
          super().start()
  ```

### ❌ DON’T
- ❌ Don’t use `is` to check instance-ness:
  ```python
  car is Car  # wrong
  ```
  Use:
  ```python
  isinstance(car, Car)
  ```
- ❌ Don’t forget `self.` when assigning:
  ```python
  color = "Red"  # local variable, NOT field
  ```
- ❌ Don’t add attributes “accidentally” with typos (`self.colour` vs `self.color`).
- ❌ Don’t store mutable defaults at the class level thinking it’s per-instance:
  ```python
  class Bad:
      items = []  # shared by ALL instances
  ```
  Prefer per-instance in `__init__`.

---

## `self` vs `cls` vs nothing

### Instance method → `self`
```python
class A:
    def m(self) -> None:
        ...
```

### Class method → `cls`
```python
class A:
    @classmethod
    def make_default(cls) -> "A":
        return cls()
```

### Static method → no `self`, no `cls`
```python
class A:
    @staticmethod
    def util(x: int) -> int:
        return x + 1
```

---

## Extra “advanced” things worth knowing (small but useful)

### 1) Type hinting `self` return: `typing.Self`
Python 3.11+:
```python
from typing import Self

class Car:
    def set_color(self, color: str) -> Self:
        self.color = color
        return self
```
This is cleaner than `"Car"` and works great for fluent APIs.

### 2) Properties feel like fields but are methods
```python
class Car:
    @property
    def age(self) -> int:
        return 2026 - self.year
```
Call as `car.age` (no parentheses), but it runs code.

### 3) Restrict accidental attributes with `__slots__`
```python
class Car:
    __slots__ = ("make", "model", "year", "color")
```
Now `self.colour = ...` will raise an error (good for preventing typos).

---

## Quick sanity examples

### Correct instance check
```python
car = Car()
print(isinstance(car, Car))   # True
print(type(car) is Car)       # True (exact type)
```

### Why `obj is Class` is wrong
`is` checks identity (same object), not type:
```python
car is Car  # always False
```

---

## Summary (one line)
`self` is **the instance**, explicit like Java’s `this`, and you must use `self.` to access per-object state.
