# Loop Control Statements in Python (`break`, `continue`, `pass`)

Loop control statements change the normal flow of a loop.

## Quick summary

| Keyword | Used for | What it does |
|---|---|---|
| `break` | Exit a loop early | Stops the loop immediately |
| `continue` | Skip current iteration | Jumps to the next iteration |
| `pass` | Placeholder / do nothing | Executes nothing (useful for stubs) |

---

## 1) `break` — terminate the loop

### Example: stop searching when you find the first match

```python
numbers = [3, 8, 2, 9, 5]
target = 9

for n in numbers:
    print("checking:", n)
    if n == target:
        print("found target, stopping")
        break
```

**Output**
```text
checking: 3
checking: 8
checking: 2
checking: 9
found target, stopping
```

---

## 2) `continue` — skip to the next iteration

### Example: skip invalid inputs

```python
items = ["10", "x", "25", "", "7"]

total = 0
for s in items:
    if not s.isdigit():          # skip non-numeric strings
        print("skipping:", repr(s))
        continue

    total += int(s)
    print("added:", s)

print("total =", total)
```

**Output**
```text
added: 10
skipping: 'x'
added: 25
skipping: ''
added: 7
total = 42
```

---

## 3) `pass` — do nothing (placeholder)

`pass` is useful when Python requires a statement, but you don’t want to do anything yet.

### Example A: stub out logic you’ll implement later

```python
age = 17

if age >= 18:
    print("Adult")
else:
    pass  # TODO: add minor-handling logic later
```

**Output**
```text
# (no output, because else block does nothing)
```

### Example B: define an empty function/class for now

```python
def future_feature():
    pass

class ComingSoon:
    pass
```

---

## Full runnable file

A runnable example file is included: **`loop_control_examples.py`**  
Run it like:

```bash
python loop_control_examples.py
```
