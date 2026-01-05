# Python Function Parameters — `a, b, *args, c, d=10, **kwargs` (README)

This README explains how to **define and call** a function like this:

```python
def f(a, b, *args, c, d=10, **kwargs):
    pass
```

It covers:
- What each parameter type means
- How to call it correctly
- Common mistakes

---

## 1) What each part means (simple)

```python
def f(a, b, *args, c, d=10, **kwargs):
```

- `a`, `b` → **normal parameters**  
  Can be passed as positional or keyword.

- `*args` → **extra positional arguments**  
  Any extra positional values go into a **tuple** named `args`.

- `c` → **keyword-only parameter (required)**  
  Because it comes after `*args`, you **must** pass it by name: `c=...`

- `d=10` → **keyword-only parameter with default value**  
  Optional. If not provided, it uses `10`.

- `**kwargs` → **extra keyword arguments**  
  Any additional named values go into a **dict** named `kwargs`.

---

## 2) The biggest rule to remember ✅

### **Positional first, then keyword-only**
You must pass:
1) `a`, `b` (positional or keyword)
2) any extra positional values (go into `*args`)
3) then keyword-only values: `c` (required), `d` (optional)
4) and any extra keywords (`**kwargs`)

---

## 3) Correct calling examples ✅

### Minimum valid call (must include `c`)
```python
f(1, 2, c=3)
```

### With extra positional values (`*args`)
```python
f(1, 2, 100, 200, c=3)
# args = (100, 200)
```

### Override the default `d`
```python
f(1, 2, c=3, d=99)
```

### With extra keyword args (`**kwargs`)
```python
f(1, 2, c=3, x="hello", y=True)
# kwargs = {"x": "hello", "y": True}
```

### With everything together
```python
f(1, 2, 100, 200, c=3, d=99, x="hello", y=True)
```

---

## 4) Common mistakes ❌ (and why)

### Missing `c` (required keyword-only)
```python
f(1, 2)     # ❌ TypeError: missing required keyword-only argument 'c'
```

### Giving `c` positionally (not allowed)
```python
f(1, 2, 3)  # ❌ 3 becomes part of *args, but c is still missing
```

### Positional after keyword (not allowed)
```python
f(1, 2, c=3, 4)  # ❌ SyntaxError: positional argument follows keyword argument
```

### Passing the same argument twice
```python
f(1, 2, 100, c=3, a=9)  # ❌ TypeError: multiple values for argument 'a'
```

---

## 5) Mini demo function (prints what it receives)

Use this to see the mapping clearly:

```python
def f(a, b, *args, c, d=10, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)       # tuple of extra positionals
    print("c =", c)             # required keyword-only
    print("d =", d)             # keyword-only with default
    print("kwargs =", kwargs)   # dict of extra keywords
```

Example call:
```python
f(1, 2, 100, 200, c=3, d=99, x="hello")
```

Output (example):
```text
a = 1
b = 2
args = (100, 200)
c = 3
d = 99
kwargs = {'x': 'hello'}
```

---

## 6) Quick summary (memorize)

- `a, b` → normal
- `*args` → extra positional
- `c` → required keyword-only
- `d=10` → optional keyword-only
- `**kwargs` → extra keywords
- You must call with `c=...`

---

## 7) Bonus: General parameter order rule

Python function parameter order is:

1. Positional-only (`/`)  
2. Positional-or-keyword  
3. `*args`  
4. Keyword-only (after `*` / `*args`)  
5. `**kwargs`  

Your example follows this rule perfectly.
