# Python Imports: `import X` vs `from X import Y` (Simple README)

This README explains **two common ways to import** in Python:

- `import X`  → import the **module**
- `from X import Y` → import **a name** (function/class/variable) **from** that module

---

## 1) `import X` (import the module)

### What it means
You import the module as a whole, and you access things using **dot notation**.

### Example
```python
import datetime

now = datetime.datetime.now()
print(now.year)
```

### Pros ✅
- **Very clear** where names come from (`datetime.datetime`)
- **Avoids name clashes** (your variable named `datetime` is less likely to conflict)
- Easier to read in large codebases
- Lets you access many things from the same module without multiple imports

### Cons ⚠️
- More typing (`datetime.datetime.now()` can be long)

---

## 2) `from X import Y` (import specific names)

### What it means
You pull specific items into the current namespace, so you can use them directly.

### Example
```python
from datetime import datetime

now = datetime.now()
print(now.year)
```

### Pros ✅
- **Shorter and cleaner** when you use `Y` many times
- Useful when you only need **one or two things** from a module

### Cons ⚠️
- Can become confusing if you import lots of names:
  ```python
  from module import a, b, c, d, e
  ```
- Higher chance of **name clashes** (you might already have `datetime` or `sum` etc.)
- Harder sometimes to know **where a name came from** while reading

---

## 3) Recommended standard (practical rules)

### Recommended ✅
1. Use **`import X`** for most modules (clear + safe):
   ```python
   import math
   import os
   import datetime
   ```
2. Use **`from X import Y`** when:
   - You use `Y` a lot, and it’s very common/clear
   - `Y` name is unlikely to clash
   Example:
   ```python
   from datetime import datetime, timedelta
   from pathlib import Path
   ```

### Very common in real projects ✅ (aliasing)
Aliasing keeps code short while staying clear:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

You can also alias a specific import:
```python
from datetime import datetime as dt
now = dt.now()
```

---

## 4) What NOT recommended (avoid this)

### Avoid: `from X import *`
```python
from math import *  # ❌ not recommended
```

Why:
- Pollutes your namespace (too many unknown names)
- Causes name conflicts
- Makes debugging and reading harder

---

## 5) Quick comparison table

| Style | Example | Best when | Main downside |
|---|---|---|---|
| `import X` | `import math` → `math.sqrt(9)` | Clarity + larger code | More typing |
| `from X import Y` | `from math import sqrt` → `sqrt(9)` | Using Y many times | Can hide where Y came from |
| Alias module | `import numpy as np` | Popular libraries / frequent use | Need to remember alias |
| Alias name | `from datetime import datetime as dt` | Short but still clear | Might confuse if overused |

---

## 6) A simple “which should I use?” guide

- You’re writing **production / team code** → **prefer `import X`** (clarity)
- You keep calling one thing many times (like `Path`, `datetime`, `timedelta`) → **use `from X import Y`**
- You use big libraries (NumPy/Pandas/Matplotlib) → **use aliases** (`np`, `pd`, `plt`)
- You’re learning → start with **`import X`**, then use `from X import Y` when comfortable

---

## 7) Tiny examples side-by-side

### Example with `math`
```python
import math
print(math.sqrt(16))
```

```python
from math import sqrt
print(sqrt(16))
```

### Example with `datetime`
```python
import datetime
print(datetime.datetime.now())
```

```python
from datetime import datetime
print(datetime.now())
```
