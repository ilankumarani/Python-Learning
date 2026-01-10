# Public, Protected, and Private Methods in Python — README (for Java Developers)

## Quick answer
Python does **not** enforce access modifiers (`public/protected/private`) like Java.
For **methods**, Python uses the same approach as variables:
- **public**: `method()`
- **protected-ish (convention)**: `_method()`
- **private-ish (name mangling)**: `__method()`

---

## 1) Public methods (default)
```python
class Service:
    def run(self) -> None:
        print("run (public)")
```

Usage:
```python
s = Service()
s.run()
```

**Java mapping:** like a public method.

---

## 2) “Protected” methods: `_method` (convention only)
```python
class Service:
    def _helper(self) -> None:
        print("_helper (internal/protected-ish)")
```

Meaning: “This is internal; intended for subclasses or internal use.”

✅ Common use:
- helper methods inside the class
- extension points for subclasses
- internal API for your module/package

❗Important: It’s still accessible:
```python
s._helper()  # allowed, but discouraged
```

**Java mapping:** similar intention as `protected`, but **not enforced**.

---

## 3) “Private” methods: `__method` (name mangling)
```python
class Service:
    def __secret(self) -> None:
        print("__secret (name-mangled)")
```

This fails:
```python
s.__secret()  # AttributeError
```

But it can be accessed via the mangled name:
```python
s._Service__secret()  # works
```

### Why name mangling exists (real reason)
It’s mainly to **avoid accidental overrides/clashes in subclasses**, not to provide security.

Example:
```python
class A:
    def __work(self) -> None:
        print("A.__work")

    def run(self) -> None:
        self.__work()


class B(A):
    def __work(self) -> None:
        print("B.__work")  # this does NOT override A.__work due to mangling
```

Calling:
```python
B().run()
```
prints:
```
A.__work
```

Because:
- `A.__work` becomes `_A__work`
- `B.__work` becomes `_B__work`
So they are different method names internally.

---

## Best practice (what to do in real projects)
### ✅ Use:
- `public_method()` for your class API
- `_internal_method()` for helpers
- `__name_mangled_method()` only when you **really** need to avoid clashes with subclasses

### ❌ Avoid:
- using `__method` everywhere (harder debugging/testing and rarely necessary)
- expecting Python to enforce access control like Java

---

## DO / DON’T (pin-point rules)

### ✅ DO
- Keep your “public API” clean and small.
- Prefix internal helpers with `_`.
- Use `__` when you must prevent subclass name collisions.
- Document expectations clearly (docstrings).

### ❌ DON’T
- Don’t treat `__method` as security (it’s not).
- Don’t rely on access modifiers to enforce design; rely on conventions + tests + reviews.

---

## Summary
Python methods follow the same convention rules as attributes:
- public: `method`
- protected-ish: `_method`
- private-ish: `__method` (name mangling)

Name mangling is mainly for **collision avoidance**, not strict privacy.
