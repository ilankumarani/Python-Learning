# Python Naming Best Practices — Class Names (README)

This README covers **class naming best practices** in Python (PEP 8 style), plus a few practical conventions you’ll see in real projects.

---

## 1) Class naming (recommended)

### ✅ Use `PascalCase` (CapWords)
- Start with a capital letter
- Each new word starts with a capital
- No underscores (usually)

Examples:
```python
class CustomerOrder: ...
class UserService: ...
class HttpClient: ...
class PaymentGateway: ...
```

### ❌ Avoid `snake_case` for class names
```python
class customer_order: ...   # ❌ not standard for classes
```

### ❌ Avoid Java-style prefixes/suffixes that don’t add value
```python
class CustomerOrderImpl: ...   # ❌ usually unnecessary in Python
class ICustomerOrder: ...      # ❌ “I” interface naming is not Python style
```

---

## 2) Exceptions naming

### ✅ End exceptions with `Error` (or `Exception`)
Examples:
```python
class ValidationError(Exception): ...
class ConfigError(Exception): ...
```

---

## 3) Abstract base classes / interfaces (Python style)

If you use ABCs (abstract base classes), keep the same `PascalCase` naming.

Examples:
```python
from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, data): ...
```

No need for `IStorage` like Java; just name it by responsibility (`Storage`, `Repository`, `Client`).

---

## 4) Mixins (common convention)

### ✅ End with `Mixin`
A mixin is a helper class meant to be inherited for extra behavior.

Examples:
```python
class JsonSerializableMixin: ...
class LoggingMixin: ...
```

---

## 5) Dataclasses / records (common)

If the class mainly holds data, still use `PascalCase`.

Examples:
```python
from dataclasses import dataclass

@dataclass
class Address:
    city: str
    zip_code: str
```

---

## 6) Private/internal classes

### ✅ Prefix with a single underscore `_`
This indicates “internal use”.

Examples:
```python
class _InternalCache: ...
class _TokenParser: ...
```

---

## 7) Acronyms in names

PEP 8 commonly prefers acronyms as normal words (readability).

Examples:
```python
class HttpClient: ...    # preferred
class UrlParser: ...
```

Many codebases still use:
```python
class HTTPClient: ...
class URLParser: ...
```

Pick one style and be consistent in your project.

---

## 8) File/module naming vs class naming

- **Files (modules):** `snake_case.py`
  - `user_service.py`
  - `http_client.py`

- **Classes:** `PascalCase`
  - `UserService`
  - `HttpClient`

---

## 9) Quick examples (clean style)

```python
# file: payment_gateway.py

class PaymentGateway:
    def charge(self, amount: float) -> bool:
        return True

class StripeGateway(PaymentGateway):
    pass

class PaymentError(Exception):
    pass
```

---

## Recommended standard (short)
- **Class names:** `PascalCase`
- **Exceptions:** end with `Error`
- **Mixins:** end with `Mixin`
- **Internal classes:** prefix `_`
- **Modules/files:** `snake_case.py`
