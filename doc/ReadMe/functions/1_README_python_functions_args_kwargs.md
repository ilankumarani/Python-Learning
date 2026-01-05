# Python Functions — README (with `return`, `*args`, `**kwargs`, and parameter rules)

This README explains:
- What a function is
- `return`
- `*args` (variable positional arguments)
- `**kwargs` (variable keyword arguments)
- **Important limitations / rules** when calling and defining functions

---

## 1) What is a function?

A **function** is a reusable block of code that you can call many times.

### Syntax
```python
def function_name(parameters):
    # code
    return value
```

### Example
```python
def greet(name):
    print(f"Hello {name} 👋")

greet("Ilan")
```

---

## 2) `return` in functions

### What `return` does
- Sends a value back to the caller
- Stops the function immediately

### Example
```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)  # 30
```

### Returning multiple values (tuple)
```python
def min_max(nums):
    return min(nums), max(nums)

mn, mx = min_max([3, 1, 9])
print(mn, mx)  # 1 9
```

### `return` vs `print`
- `print()` shows output on screen
- `return` gives a value to use in code

```python
def bad_add(a, b):
    print(a + b)   # prints but returns None

def good_add(a, b):
    return a + b   # returns value
```

---

## 3) `*args` (variable positional arguments)

### What `*args` means
- Collects **extra positional arguments** into a tuple.
- Use it when you don’t know how many values will be passed.

### Example
```python
def total(*args):
    return sum(args)

print(total(1, 2, 3))       # 6
print(total(10, 20, 30, 5)) # 65
```

### Normal parameters + `*args`
```python
def log(prefix, *messages):
    for msg in messages:
        print(prefix, msg)

log("[INFO]", "Started", "Loading", "Done")
```

---

## 4) `**kwargs` (variable keyword arguments)

### What `**kwargs` means
- Collects **extra keyword arguments** into a dictionary.
- Use it when you want flexible named inputs.

### Example
```python
def show_profile(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

show_profile(name="Ilan", role="Developer", city="Glasgow")
```

### Normal parameters + `**kwargs`
```python
def connect(host, port=5432, **options):
    print("host:", host)
    print("port:", port)
    print("options:", options)

connect("db.local", timeout=30, ssl=True)
```

---

## 5) Using `*args` and `**kwargs` together

```python
def demo(*args, **kwargs):
    print("args:", args)     # tuple
    print("kwargs:", kwargs) # dict

demo(1, 2, 3, name="Ilan", active=True)
```

---

## 6) Forwarding args/kwargs (very common)

Useful when you wrap another function.

```python
def run_with_logging(func, *args, **kwargs):
    print("Running...")
    result = func(*args, **kwargs)
    print("Done")
    return result

def multiply(a, b):
    return a * b

print(run_with_logging(multiply, 3, 4))  # 12
```

---

# 7) IMPORTANT: Function parameter rules / limitations (highlight)

These rules are the ones that most commonly cause errors in interviews and real projects.

---

## ✅ Rule 1 — Default parameters must be at the end

**All non-default parameters must come first.**  
✅ Valid:
```python
def discount_price(price, discount=0):
    return price - (price * discount / 100)
```

❌ Invalid (SyntaxError):
```python
# def discount_price(price=0, discount):  # ❌ default before non-default
#     ...
```

---

## ✅ Rule 2 — Positional arguments must come before keyword arguments (when calling)

When calling a function:
- First pass positional arguments
- Then pass keyword arguments

✅ Valid (your example):
```python
def full_name(title, first_name, last_name):
    print(f"hello {title} , First name :: {first_name} , Last name :: {last_name}")

full_name("Mr", last_name="Ilangovan", first_name="Ilankumaran")
```

❌ Invalid (positional after keyword):
```python
# full_name(title="Mr", "Ilankumaran", last_name="Ilangovan")  # ❌ SyntaxError
```

---

## ✅ Rule 3 — You cannot pass the same argument twice
❌ Invalid:
```python
def full_name(title, first_name, last_name):
    print(f"hello {title} , First name :: {first_name} , Last name :: {last_name}")


# full_name("Mr", "Ilankumaran", first_name="Other")  # ❌ TypeError (multiple values)
```

---

## ✅ Rule 4 — Parameter order in function definitions (the full rule)

Python parameter order is:

1. **Positional-only** (rare; uses `/`)
2. Normal parameters (positional-or-keyword)
3. `*args`
4. **Keyword-only** parameters (after `*` or `*args`)
5. `**kwargs`

Example showing the order:
```python
def f(a, b, *args, c, d=10, **kwargs):
    pass
# a, b -> normal
# *args -> extra positional
# c, d -> keyword-only (must be named)
# **kwargs -> extra keywords
```
> [!NOTE]
> [Click here to read in Full detail](1_README_function_params_args_kwargs_kwonly.md)

---

## ✅ Rule 5 — Keyword-only parameters (must be named)

If a parameter is after `*` (or after `*args`), it must be passed using a keyword.

```python
def send_email(to, *, subject, body):
    print(to, subject, body)

send_email("a@b.com", subject="Hi", body="Hello")  # ✅
# send_email("a@b.com", "Hi", "Hello")            # ❌ TypeError
```

---

## ✅ Rule 6 — `*args` must come before `**kwargs`

✅ Valid:
```python
def demo(*args, **kwargs):
    pass
```

❌ Invalid:
```python
# def demo(**kwargs, *args):  # ❌ SyntaxError
#     pass
```

---

## ⚠️ Rule 7 — Avoid mutable default arguments (VERY important)

Default arguments are created **once** (not every call).  
So using `[]` or `{}` as defaults can cause bugs.

❌ Bad:
```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

✅ Good:
```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## ⚠️ Rule 8 — Keyword names must match the parameter names

❌ Wrong name:
```python
def greet(name):
    print(name)

# greet(nam="Ilan")  # ❌ TypeError: unexpected keyword argument
```

---

## 8) Quick summary (most useful)

- Defaults go last: `def f(a, b=0): ...`
- Calling order: positional first, then keyword
- Don’t pass the same argument twice
- `*args` before `**kwargs`
- Use `None` instead of `[]` / `{}` for defaults

---

## 9) Quick examples summary

```python
def add(a, b):
    return a + b

def total(*args):
    return sum(args)

def config(**kwargs):
    return kwargs

def all_in_one(a, b, *args, **kwargs):
    return a, b, args, kwargs
```
