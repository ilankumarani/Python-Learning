# Method Resolution Order (MRO) in Python — README (with Example)

## What is MRO?
**MRO (Method Resolution Order)** is the rule Python uses to decide **which class method to call first**
when multiple inheritance is involved.

When you call:
```python
d.hello()
```
Python searches for `hello` following the class order defined by the MRO list:
```python
D -> B -> C -> A -> object
```

You can view it using:
```python
print(D.mro())
# or
print(D.__mro__)
```

---

## Why MRO matters
In multiple inheritance, two or more parent classes can define the same method name.
MRO ensures:
- a **consistent** method lookup order
- a safe way for classes to cooperate using `super()`
- the “diamond problem” is handled correctly (no duplicated base calls)

Python uses an algorithm called **C3 linearization** to compute the MRO.

---

## The diamond inheritance example (classic)

```python
class A:
    def hello(self) -> None:
        print("A.hello")

class B(A):
    def hello(self) -> None:
        print("B.hello")
        super().hello()

class C(A):
    def hello(self) -> None:
        print("C.hello")
        super().hello()

class D(B, C):
    def hello(self) -> None:
        print("D.hello")
        super().hello()
```

### What happens when you run `D().hello()`?
It prints in this order:
```
D.hello
B.hello
C.hello
A.hello
```

That order comes from:
```
D.mro() == [D, B, C, A, object]
```

---

## Key rule (the most important one)
### ✅ Use `super()` everywhere in cooperative multiple inheritance
Each class should call `super()` so Python can follow the MRO chain exactly once per class.

### ❌ Don’t call a parent directly (breaks MRO)
Bad pattern:
```python
A.hello(self)  # can skip classes or call A multiple times
```

---

## Quick checklist (Do / Don’t)
✅ DO:
- Prefer single inheritance unless multiple inheritance is clearly needed.
- In multiple inheritance, use **cooperative super()** in every class that participates.
- Inspect MRO using `Class.mro()` when debugging.

❌ DON’T:
- Don’t call parent class methods directly in diamond inheritance.
- Don’t mix direct base calls and `super()` in the same cooperative chain.

---

## Summary (one line)
MRO is Python’s predictable method-lookup path in multiple inheritance, and `super()` is how you safely follow it.
