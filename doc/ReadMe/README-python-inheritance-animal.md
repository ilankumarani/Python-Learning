# Inheritance in Python (Animal Example) — README for Java Developers

## What inheritance means
Inheritance lets a **child class reuse and extend** a **parent class**.

- **Java:** `class Dog extends Animal`
- **Python:** `class Dog(Animal)`

Python supports:
- Inheriting methods/attributes from a parent
- **Overriding** parent methods in a child
- Calling parent behavior using `super()`
- (Optionally) **multiple inheritance** (with rules via MRO)

---

## Simple words (Java mapping)
- `self` ≈ `this`
- `class Dog(Animal)` ≈ `class Dog extends Animal`
- Overriding = same method name in child
- `super().method()` ≈ `super.method()` in Java
- Polymorphism works the same idea: calling `speak()` runs the child's implementation

---

## Core example: `Animal` inheritance

```python
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return "..."  # default behavior

    def eat(self, food: str) -> None:
        print(f"{self.name} eats {food}")


class Dog(Animal):
    def speak(self) -> str:  # override
        return "Woof!"


class Cat(Animal):
    def speak(self) -> str:  # override
        return "Meow!"


def main() -> None:
    animals: list[Animal] = [Dog("Rocky"), Cat("Mimi")]

    for a in animals:
        print(f"{a.name} says {a.speak()}")  # polymorphism
        a.eat("food")


if __name__ == "__main__":
    main()
```

### What happens here
- `Dog` and `Cat` inherit `eat()` and `name` from `Animal`
- `Dog.speak()` and `Cat.speak()` override `Animal.speak()`
- The loop calls `a.speak()` and Python picks the correct method at runtime

---

## Overriding constructors + using `super()`

```python
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name)   # call parent constructor
        self.breed = breed
```

**Java-style note:** In Python you typically call `super().__init__(...)` explicitly when you override `__init__`.

---

## Java vs Python: the important differences

### 1) Access modifiers (public/private/protected)
- Java has `public/protected/private`.
- Python relies on **conventions**:
  - `name` = public
  - `_name` = “internal/protected-ish” (by convention)
  - `__name` = name-mangled (harder to access, not true privacy)

### 2) Method overloading
- Java supports method overloading by signature.
- Python **does not** overload by signature.
  - Use default params, `*args/**kwargs`, or `singledispatch`.

### 3) Multiple inheritance
- Java: single class inheritance, multiple interfaces.
- Python: **multiple class inheritance is allowed**:
  ```python
  class C(A, B): ...
  ```
  Method resolution follows the **MRO (Method Resolution Order)**.

**Rule:** If you use multiple inheritance, prefer “cooperative” `super()` (especially in diamond shapes).

### 4) Interfaces
- Java has interfaces.
- Python equivalents:
  - **Duck typing** (most common): “if it quacks, it’s a duck”
  - `typing.Protocol` (static type checking)
  - `abc.ABC` + `@abstractmethod` (runtime enforcement)

### 5) Equality and hashing
- Java: `equals()` / `hashCode()`
- Python: `__eq__()` / `__hash__()`
- If you override `__eq__` and don’t define `__hash__`, Python may make instances unhashable (to avoid broken sets/dicts).

### 6) Fields(Class(Static) variable vs attributes(Instance variable)
- Java fields are declared in the class.
- Python instance attributes often appear in `__init__`:
  ```python
  self.name = name
  ```
- Typos can create new attributes silently (`self.colour` vs `self.color`) unless you use tools like type checkers or `__slots__`.

### 7) “final” and strict types
- Java has `final`, and types are enforced at compile time.
- Python is dynamic. Type hints help tooling but don’t enforce at runtime (unless you add runtime checks).

---

## Polymorphism rule (same as Java concept, Python mechanism differs)
When you do:
```python
a: Animal = Dog("Rocky")
a.speak()
```
Python uses **dynamic dispatch** to call `Dog.speak`.

---

## MRO (Method Resolution Order) — quick note (Python-only concept)
In multiple inheritance:
```python
class A: ...
class B: ...
class C(A, B): ...
```
If both `A` and `B` have `eat()`, `C().eat()` checks:
1. `C`
2. then `A`
3. then `B`
4. then `object`

You can inspect this:
```python
print(C.mro())
```

---

## DO / DON’T (practical checklist)

### ✅ DO
- Use inheritance when there is a true **is-a** relationship (Dog is-an Animal).
- Use `super()` when extending behavior:
  ```python
  def speak(self):
      base = super().speak()
      return base + "!"
  ```
- Prefer composition over deep inheritance (same advice as good Java design).

### ❌ DON’T
- Don’t copy Java patterns 1:1 (like giant base classes or util classes everywhere).
- Don’t expect method overloading to work.
- Don’t use multiple inheritance unless you understand the MRO and cooperative `super()`.

---

## Summary (one line)
Inheritance in Python works like Java conceptually, but Python is more dynamic: it uses conventions over access modifiers, has no signature overloading, and supports multiple inheritance via MRO.
