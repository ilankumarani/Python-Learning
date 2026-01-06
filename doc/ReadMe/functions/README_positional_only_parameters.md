# Positional-Only Parameters in Python (`/`) — README

Positional-only parameters let you **force some arguments to be passed only by position** (not by `name=value`).

> [!IMPORTANT]
> Positional-only syntax (`/`) requires **Python 3.8+**.

---

## 1) What does `/` mean?

Everything **before** `/` is **positional-only**:

```python
def f(a, b, /, c, d):
    ...
```

- `a`, `b` → positional-only
- `c`, `d` → normal (positional **or** keyword)

✅ Valid calls:
```python
f(1, 2, 3, 4)
f(1, 2, c=3, d=4)
```

❌ Invalid calls:
```python
# f(a=1, b=2, c=3, d=4)   # TypeError: a and b are positional-only
# f(1, b=2, c=3, d=4)     # TypeError: b cannot be a keyword
```

---

## 2) Why use positional-only? (When it’s useful)

### ✅ Advantage 1: You can rename parameters later (API stability)
If callers are forced to pass `a` and `b` positionally, you can rename them in the future without breaking code that calls you.

### ✅ Advantage 2: Matches many built-in / C-style APIs
Some APIs are designed to be positional for speed/history/compatibility.

### ✅ Advantage 3: Makes some calls shorter/cleaner
Example: `pow(2, 3)` is cleaner than `pow(x=2, y=3)`.

> [!NOTE]
> Use positional-only mainly for **library/public API design**. For application code, it’s less common.

---

## 3) Disadvantages (be careful)

- Harder to read at the call site (no argument names shown)
- Easy to mix up values when parameters have the same type (e.g., two ints)
- Less self-documenting than keyword arguments

---

## 4) Rules to remember (positional-only)

> [!TIP]
> **Rule:** “Everything LEFT of `/` is position-only.”

### Rule A — Positional-only cannot be passed as keyword
```python
def f(a, /, b): ...
f(1, b=2)        # ✅
# f(a=1, b=2)    # ❌ a is positional-only
```

### Rule B — You can still use keyword arguments for parameters AFTER `/`
```python
def f(a, b, /, c): ...
f(1, 2, c=3)     # ✅
```

### Rule C — Positional must still come before keyword in the call
```python
f(1, 2, c=3)      # ✅
# f(a=1, 2, c=3)  # ❌ SyntaxError
```

---

## 5) Common signature patterns (positional-only)

### Only positional-only
```python
def f(a, b, /):
    ...
```

### Positional-only + normal
```python
def f(a, b, /, c, d=10):
    ...
```

### Positional-only + keyword-only (combined with `*`)
```python
def f(a, b, /, *, c, d=10):
    ...
```
Call:
```python
f(1, 2, c=3)
```

---

## 6) Memory trick (easy)

> [!TIP]
> Think: **`/` is a “wall”** — names cannot cross it from the right side to label the left-side arguments.

- Left of `/` → only position
- Right of `/` → normal rules apply

---

## 7) Quick checklist

- [ ] Do I really need positional-only? (mostly for public APIs)
- [ ] Will positional-only make calls confusing?
- [ ] Do I want to allow renaming parameters later? (good reason)
