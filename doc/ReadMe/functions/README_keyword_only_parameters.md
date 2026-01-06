# Keyword-Only Parameters in Python (`*`) — README

Keyword-only parameters let you **force certain arguments to be passed using `name=value`**.

This improves readability and prevents “wrong-order” bugs.

---

## 1) What does `*` mean?

Everything **after** `*` is **keyword-only**.

```python
def f(a, b, *, c, d=10):
    ...
```

- `a`, `b` → normal (positional or keyword)
- `c`, `d` → keyword-only (`c` required, `d` optional default)

✅ Valid calls:
```python
f(1, 2, c=3)
f(1, 2, c=3, d=99)
f(a=1, b=2, c=3)
```

❌ Invalid calls:
```python
# f(1, 2, 3)   # TypeError: c must be a keyword
# f(1, 2, 3, 4)
```

---

## 2) Two ways to create keyword-only parameters

### A) Bare `*`
```python
def send_email(to, *, subject, body):
    ...
```

✅
```python
send_email("a@b.com", subject="Hi", body="Hello")
```

❌
```python
# send_email("a@b.com", "Hi", "Hello")  # TypeError
```

### B) After `*args` (anything after `*args` is keyword-only)
```python
def f(a, *args, c, d=10):
    ...
```

✅
```python
f(1, 100, 200, c=3)
```

---

## 3) Why use keyword-only? (When it’s useful)

### ✅ Advantage 1: Call sites become self-documenting
```python
connect(host="db.local", timeout=30, ssl=True)
```

### ✅ Advantage 2: Prevent “wrong-order” mistakes
If two params are both ints, `f(10, 30)` could be ambiguous — keyword-only forces clarity.

### ✅ Advantage 3: Great for optional settings (“options” style)
Timeouts, flags, config parameters, feature switches, formatting options.

> [!NOTE]
> Keyword-only is very common in modern Python APIs for safety.

---

## 4) Disadvantages (be careful)

- More typing at the call site (need `name=value`)
- Can feel verbose for very frequently-called small helper functions

---

## 5) Rules to remember (keyword-only)

> [!TIP]
> **Rule:** “Everything RIGHT of `*` must be named.”

### Rule A — Keyword-only must be passed using `name=value`
```python
def f(*, c): ...
f(c=1)      # ✅
# f(1)      # ❌
```

### Rule B — Positional arguments must come first in the call
```python
f(1, 2, c=3)    # ✅
# f(1, c=3, 2)  # ❌ SyntaxError
```

### Rule C — Don’t pass the same argument twice
```python
def f(a, *, c): ...
# f(1, a=2, c=3)  # ❌ TypeError: multiple values for 'a'
```

---

## 6) Common keyword-only patterns

### Keyword-only options API
```python
def download(url, *, timeout=10, retries=3, verify_ssl=True):
    ...
```

### Enforcing clarity for two similar parameters
```python
def move(x, y, *, dx=0, dy=0):
    ...
```

### Keyword-only with defaults
```python
def format_name(first, last, *, title=None, uppercase=False):
    ...
```

---

## 7) Memory trick (easy)

> [!TIP]
> Think: `*` means **“keywords start here”**.

- Before `*` → positional can be used
- After `*` → **must** use `name=value`

---

## 8) Quick checklist

- [ ] Do these parameters represent “options/settings”? → keyword-only fits well
- [ ] Could callers easily mix up argument order? → keyword-only prevents bugs
- [ ] Is the function a public API? → keyword-only improves readability
