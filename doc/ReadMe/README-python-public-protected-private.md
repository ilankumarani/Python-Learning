# Public, Protected, and Private Variables in Python — README (for Java Developers)

## Quick answer
Python does **not** enforce `public / protected / private` like Java.
Instead, it uses **naming conventions** (and one mechanism called **name mangling**).

| Java idea | Python style | Meaning |
|---|---|---|
| public | `name` | normal attribute, freely accessible |
| protected | `_name` | “internal” / for subclasses (convention only) |
| private | `__name` | name-mangled to reduce accidental access / avoid clashes |

---

## 1) Public attribute (default)
```python
class User:
    def __init__(self, name: str) -> None:
        self.name = name   # public
```

Usage:
```python
u = User("Bala")
print(u.name)
u.name = "Kumar"
```

**Java mapping:** similar to a public field or a property-like access pattern.

---

## 2) “Protected” attribute (`_name`) — convention only
```python
class User:
    def __init__(self, age: int) -> None:
        self._age = age  # "protected" by convention
```

Meaning: “this is internal; external code shouldn’t touch it unless necessary”.

✅ Common use:
- internal helper data
- subclass extension points
- module/library internals

❗Important: Python does **not** block access:
```python
u._age  # allowed, but discouraged
```

---

## 3) “Private” attribute (`__name`) — name mangling
```python
class User:
    def __init__(self, salary: int) -> None:
        self.__salary = salary  # name-mangled
```

From outside, this fails:
```python
u.__salary  # AttributeError
```

But it can still be accessed with the mangled name (not true security):
```python
u._User__salary  # works
```

### Why this exists
`__name` is mainly to:
- prevent **accidental** access
- avoid **name clashes in subclasses**

Example:
```python
class A:
    def __init__(self) -> None:
        self.__x = 1

class B(A):
    def __init__(self) -> None:
        super().__init__()
        self.__x = 2  # different attribute than A.__x due to name mangling
```

---

## Best practice (Java-style encapsulation): `@property`
Instead of exposing and mutating internal fields directly, use properties.

```python
class User:
    def __init__(self, salary: int) -> None:
        self.__salary = salary

    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, value: int) -> None:
        if value < 0:
            raise ValueError("salary cannot be negative")
        self.__salary = value
```

Usage:
```python
u = User(100)
print(u.salary)   # looks like a field, runs getter
u.salary = 200    # runs setter
```

**Java mapping:** `getSalary()` / `setSalary()` but accessed like a field.

---

## Class variables vs instance variables (common confusion)
- `self.x` → instance variable (per object)
- `ClassName.x` → class variable (shared)

```python
class Counter:
    total = 0  # class variable

    def __init__(self) -> None:
        Counter.total += 1
        self.id = Counter.total  # instance variable
```

---

## DO / DON’T (pin-point rules)

### ✅ DO
- Use **public attributes** for simple data objects (especially `@dataclass`).
- Use `_name` to signal “internal / protected-ish”.
- Use `__name` when you want to avoid subclass name collisions or accidental access.
- Use `@property` when you need validation, computed values, or controlled mutation.

### ❌ DON’T
- Don’t assume `__name` is true “private security” — it’s only name mangling.
- Don’t create huge getter/setter boilerplate like Java unless you need it (properties are cleaner).
- Don’t expose mutable shared state as a class variable unless you really want it shared.

---

## Summary
Python uses **conventions** for access control:
- public: `name`
- protected-ish: `_name`
- private-ish: `__name` (name-mangled)

For real encapsulation behavior, use **`@property`**.
