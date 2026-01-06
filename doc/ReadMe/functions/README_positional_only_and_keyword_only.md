# Python Parameters: Positional-Only (`/`) and Keyword-Only (`*`) — README

This README explains **positional-only parameters** and **keyword-only parameters**, how to define them, how to call them, and all common signature patterns.

---

## Image → Text (transcribed)

**Positional-only arguments**
- Advanced and rare feature  
- Force argument to be positional only (cannot use keyword)  
- Must have Python 3.8 or above  
- Place a `/` in the parameter list. Parameters that come before `/` are positional only  

```python
def foo(a, b, /, c, d):
    ...
```

**A mix of positional-only, both, and keyword-only**
```python
def foo(a, b, /, c, d, *, e, f):
    ...
```

**A mix of positional-only and keyword-only**
```python
def foo(a, b, /, *, e, f):
    ...
```

**All positional-only or all keyword-only**
```python
def foo(a, b, /):      # only positional-only
    ...

def foo(*, e, f):      # only keyword-only
    ...
```

---

## 1) The 5 kinds of parameters in Python

In Python, function parameters can be:

1. **Positional-only**: must be passed by position (before `/`)
2. **Positional-or-keyword**: can be passed either way (normal params)
3. **Var-positional**: `*args` (extra positional values)
4. **Keyword-only**: must be passed with `name=value` (after `*` or `*args`)
5. **Var-keyword**: `**kwargs` (extra keyword values)

---

## 2) Positional-only parameters (`/`)

### What it means
Anything **before** `/` is **positional-only**.

```python
def f(a, b, /, c):
    ...
```

✅ Valid calls:
```python
f(1, 2, 3)
f(1, 2, c=3)
```

❌ Invalid calls (because `a` and `b` are positional-only):
```python
# f(a=1, b=2, c=3)   # TypeError
# f(1, b=2, c=3)     # TypeError (b cannot be a keyword)
```

### Why it exists (real reasons)
- Keep a stable public API (you can rename parameters later without breaking callers)
- Match C-implemented/built-in functions that historically only accepted positional args
- Make calls simpler/cleaner for some APIs (like `pow(x, y, /, mod=None)` style)

> Requirement: positional-only syntax `/` is supported in **Python 3.8+**.

---

## 3) Keyword-only parameters (`*`)

### What it means
Anything **after** `*` must be passed as a keyword.

You can force keyword-only in two ways:

### A) Using a bare `*`
```python
def f(a, *, b, c=10):
    ...
```

✅ Valid:
```python
f(1, b=2, c=3)
f(1, b=2)          # c uses default
```

❌ Invalid:
```python
# f(1, 2, 3)       # TypeError (b and c must be keywords)
```

### B) Using `*args` (keyword-only comes after it)
```python
def f(a, *args, b):
    ...
```

✅ Valid:
```python
f(1, 100, 200, b=5)
```

❌ Invalid:
```python
# f(1, 100, 200, 5)   # TypeError (b must be a keyword)
```

### Why keyword-only is useful
- Makes calls self-documenting: `send_email(to, subject=..., body=...)`
- Prevents mistakes when arguments are same type/order-confusing
- Safer APIs for optional settings (timeouts, flags, configs)

---

## 4) “All possible” common signature patterns (with examples)

Below are the patterns you’ll see in real code.

### 4.1 Only positional-only
```python
def f(a, b, /):
    ...
```
Call:
```python
f(1, 2)
# f(a=1, b=2)  # ❌
```

### 4.2 Only keyword-only
```python
def f(*, a, b=10):
    ...
```
Call:
```python
f(a=1, b=2)
f(a=1)      # b default
# f(1, 2)   # ❌
```

### 4.3 Positional-only + normal (pos-or-kw)
```python
def f(a, b, /, c, d=10):
    ...
```
Call:
```python
f(1, 2, 3, 4)
f(1, 2, c=3, d=4)
```

### 4.4 Normal + keyword-only (classic)
```python
def f(a, b, *, c, d=10):
    ...
```
Call:
```python
f(1, 2, c=3)
f(1, 2, c=3, d=99)
```

### 4.5 Positional-only + keyword-only (no “normal” params)
```python
def f(a, b, /, *, c, d=10):
    ...
```
Call:
```python
f(1, 2, c=3)
# f(1, 2, 3)   # ❌ c must be keyword
```

### 4.6 Positional-only + normal + keyword-only (full mix)
```python
def f(a, b, /, c, d, *, e, f_=10):
    ...
```
Call:
```python
f(1, 2, 3, 4, e=5)
f(1, 2, c=3, d=4, e=5, f_=99)
```

### 4.7 With `*args` and keyword-only
```python
def f(a, b, *args, c, d=10):
    ...
```
Call:
```python
f(1, 2, c=3)                 # args = ()
f(1, 2, 100, 200, c=3)        # args = (100, 200)
f(1, 2, 100, c=3, d=99)
```

### 4.8 With everything: posonly + normal + *args + kwonly + **kwargs
This is the “master” signature:
```python
def f(a, b, /, x, y=0, *args, c, d=10, **kwargs):
    ...
```
Call:
```python
f(1, 2, 3, c=4)                         # x=3, y=0, args=()
f(1, 2, 3, 9, 100, 200, c=4, z="hi")    # y=9, args=(100,200), kwargs={"z":"hi"}
```

---

## 5) Calling rules / limitations (highly important)

### ✅ Rule A — Positional arguments must come before keyword arguments
```python
f(1, 2, c=3)      # ✅
# f(a=1, 2, c=3)  # ❌ positional after keyword (SyntaxError)
```

### ✅ Rule B — Positional-only params cannot be passed as keywords
```python
def f(a, /, b): ...
f(1, b=2)     # ✅
# f(a=1, b=2) # ❌ a is positional-only
```

### ✅ Rule C — Keyword-only params must be passed by name
```python
def f(*, c): ...
f(c=1)        # ✅
# f(1)        # ❌
```

### ✅ Rule D — You can’t pass the same argument twice
```python
def f(a, b): ...
# f(1, a=2)   # ❌ TypeError (multiple values for a)
```

### ✅ Rule E — Defaults must be at the end (within their section)
```python
def ok(a, b=0): ...
# def bad(a=0, b): ...  # ❌ SyntaxError
```

---

## 6) Quick cheat sheet

- Put `/` to the **left** to force **positional-only**
- Put `*` (or `*args`) to force **keyword-only**
- Typical order (definition):
  1) pos-only (`/`)
  2) normal (pos-or-kw)
  3) `*args`
  4) kw-only
  5) `**kwargs`

---

## 7) Your example: how to call it

```python
def f(a, b, *args, c, d=10, **kwargs):
    pass
```

✅ Valid calls:
```python
f(1, 2, c=3)
f(1, 2, 100, 200, c=3)
f(1, 2, 100, 200, c=3, d=99, x="hello", y=True)
```

❌ Common mistakes:
```python
# f(1, 2)          # ❌ missing required keyword-only c
# f(1, 2, 3)       # ❌ c still missing (3 goes into args)
# f(1, 2, c=3, 4)  # ❌ positional after keyword
```
