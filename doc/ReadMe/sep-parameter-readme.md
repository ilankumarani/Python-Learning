# `sep` Parameter in `print()` (Python)

In Python, the `print()` function can print multiple values at once:

```python
print("a", "b", "c")
# Output: a b c
```

By default, it puts a **space `" "`** between each value.  
The **`sep` (separator)** parameter lets you change what is printed **between** those values.

## Syntax

```python
print(value1, value2, ..., sep="separator_string")
```

## Description

- `sep` stands for **separator**.
- It must be a **string**.
- It is inserted **between** each value passed to `print()`.

## Examples

### 1. Default behavior (space)

```python
print("a", "b", "c")
# Output: a b c
```

### 2. Using a hyphen as separator

```python
print("a", "b", "c", sep="-")
# Output: a-b-c
```

### 3. Combining text and numbers

```python
print("year", 2025, sep=":")
# Output: year:2025
```

### 4. No separator (values stuck together)

```python
print("a", "b", "c", sep="")
# Output: abc
```

### 5. Building a date-like string

```python
print("2025", "12", "23", sep="-")
# Output: 2025-12-23
```

## `sep` vs `end`

The `print()` function also has an `end` parameter.

- `sep` → string printed **between** multiple values in one `print()` call.  
- `end` → string printed **after** all values (default is newline `"
"`).

Example:

```python
print("Hello", "World", sep=", ", end="!!!\n")
# Output: Hello, World!!!
```

## Summary

- Use `sep` when you want to control what appears **between** printed values.  
- Common uses:
  - `sep=","` → comma-separated values  
  - `sep="-"` → hyphen-separated values  
  - `sep=""` → no space between values
