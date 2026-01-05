# Python Naming Best Practices — Method Names (README)

This README focuses on **method/function naming** best practices in Python (PEP 8 style), with a short note about class names for context.

---

## 1) Method / Function naming (recommended)

### ✅ Use `snake_case`
- Use lowercase words separated by underscores.

Examples:
```python
def calculate_total(): ...
def get_user_name(): ...
def parse_json_file(): ...
```

### ✅ Use verbs for actions
Method names should describe what they **do**.

Examples:
```python
def load_data(): ...
def save_report(): ...
def send_email(): ...
```

---

## 2) Boolean method naming (returns True/False)

### ✅ Use `is_`, `has_`, `can_`, `should_`
Examples:
```python
def is_valid(): ...
def has_permission(): ...
def can_retry(): ...
def should_log(): ...
```

Avoid vague names:
```python
def valid(): ...     # ❌ unclear (is it boolean? what does it return?)
def check(): ...     # ❌ too generic
```

---

## 3) “Private” / internal methods

### ✅ Prefix with a single underscore `_`
This signals: “internal use, not part of public API”.

Examples:
```python
def _parse_config(): ...
def _build_headers(): ...
```

Note: It’s a convention, not real access control.

---

## 4) Special methods (“dunder” methods)

### ✅ Double underscore methods are reserved for Python protocol behavior
Examples:
```python
def __init__(self): ...
def __str__(self): ...
def __len__(self): ...
```

Don’t invent your own `__my_method__()` unless you truly implement a Python protocol.

---

## 5) Avoid these common mistakes

### ❌ Don’t use Java-style camelCase
```python
def getUserName(): ...   # ❌ not Python style
```

### ❌ Don’t use ClassName style for methods
```python
def CalculateTotal(): ... # ❌ looks like a class
```

### ❌ Don’t shadow built-ins
Avoid names like:
- `list`, `dict`, `str`, `id`, `type`, `sum`

Bad:
```python
def sum(values): ...  # ❌ shadows built-in sum()
```

---

## 6) Naming patterns (practical cheatsheet)

| Purpose | Good examples |
|---|---|
| Create | `create_user()`, `build_request()` |
| Read/Fetch | `get_user()`, `fetch_orders()` |
| Update | `update_status()`, `set_price()` |
| Delete | `delete_item()`, `remove_user()` |
| Convert | `to_dict()`, `from_json()` |
| Validate | `is_valid()`, `validate_input()` *(validate may raise errors instead of returning bool)* |

---

## 7) Quick note: Class naming (for context)

### ✅ Class names use `PascalCase`
Examples:
```python
class CustomerOrder: ...
class HttpClient: ...
class UserService: ...
```

---

## 8) Mini example (clean naming)

```python
class OrderCalculator:
    def calculate_total(self, items):
        return sum(item["price"] for item in items)

    def is_discount_eligible(self, customer):
        return customer.get("is_premium", False)

    def _round_currency(self, amount):
        return round(amount, 2)
```

---

## Recommended standard
- **Class names:** `PascalCase`
- **Methods/functions:** `snake_case`
- **Boolean methods:** `is_ / has_ / can_ / should_`
- **Internal methods:** `_leading_underscore`
