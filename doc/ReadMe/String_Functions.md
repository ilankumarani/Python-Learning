# Python `str` (String) Methods — README Cheat Sheet


# Run this (it prints every name in your installed Python’s String):
```python
import string
print([n for n in dir(string) if not n.startswith("_")])
```
```shell
python -c "import string; print([n for n in dir(string) if not n.startswith('_')])"
```

## Formatting
| Method | What it does | Example code | Result |
|---|---|---|---|
| `format()` | Format using `{}` placeholders | `"Hi {}, age {}".format("Sam", 30)` | `"Hi Sam, age 30"` |
| `format_map()` | Format using a dict | `"Hi {name}".format_map({"name":"Sam"})` | `"Hi Sam"` |

---

## Search / Replace
| Method | What it does | Example code | Result |
|---|---|---|---|
| `find(sub)` | First index, `-1` if not found | `"hello".find("ll")` | `2` |
| `rfind(sub)` | Last index, `-1` if not found | `"ababa".rfind("ba")` | `3` |
| `index(sub)` | First index, error if not found | `"hello".index("ll")` | `2` |
| `rindex(sub)` | Last index, error if not found | `"ababa".rindex("ba")` | `3` |
| `count(sub)` | Count occurrences | `"banana".count("an")` | `2` |
| `replace(old, new)` | Replace text | `"a-b".replace("-", "_")` | `"a_b"` |
| `startswith(x)` | Check prefix | `"hello".startswith("he")` | `True` |
| `endswith(x)` | Check suffix | `"hello".endswith("lo")` | `True` |

---

## Split / Join
| Method | What it does | Example code | Result |
|---|---|---|---|
| `split(sep)` | Split into list | `"a,b,c".split(",")` | `["a","b","c"]` |
| `rsplit(sep, n)` | Split from right (max n splits) | `"a,b,c".rsplit(",", 1)` | `["a,b","c"]` |
| `splitlines()` | Split by line breaks | `"a\nb".splitlines()` | `["a","b"]` |
| `join(items)` | Join items into string | `"-".join(["a","b"])` | `"a-b"` |
| `partition(sep)` | Split into 3 parts (first match) | `"a=b=c".partition("=")` | `("a","=","b=c")` |
| `rpartition(sep)` | Split into 3 parts (last match) | `"a=b=c".rpartition("=")` | `("a=b","=","c")` |

---

## Case conversions
| Method | What it does | Example code | Result |
|---|---|---|---|
| `lower()` | Lowercase | `"HeLLo".lower()` | `"hello"` |
| `upper()` | Uppercase | `"HeLLo".upper()` | `"HELLO"` |
| `capitalize()` | Capitalize first char | `"hello".capitalize()` | `"Hello"` |
| `title()` | Title case words | `"hello world".title()` | `"Hello World"` |
| `swapcase()` | Swap case | `"HeLLo".swapcase()` | `"hEllO"` |
| `casefold()` | Strong lowercase (best for comparison) | `"ß".casefold()` | `"ss"` |

---

## Trim / Padding (Alignment)
| Method | What it does | Example code | Result |
|---|---|---|---|
| `strip()` | Remove both-side whitespace | `"  hi  ".strip()` | `"hi"` |
| `lstrip()` | Remove left whitespace | `"  hi".lstrip()` | `"hi"` |
| `rstrip()` | Remove right whitespace | `"hi  ".rstrip()` | `"hi"` |
| `center(w)` | Center with spaces | `"hi".center(6)` | `"  hi  "` |
| `ljust(w)` | Pad right spaces | `"hi".ljust(5)` | `"hi   "` |
| `rjust(w)` | Pad left spaces | `"hi".rjust(5)` | `"   hi"` |
| `zfill(w)` | Pad left with zeros | `"42".zfill(5)` | `"00042"` |

---

## Checks (True/False methods)
| Method | What it checks | Example code | Result |
|---|---|---|---|
| `isalpha()` | Letters only | `"abc".isalpha()` | `True` |
| `isdigit()` | Digits only | `"123".isdigit()` | `True` |
| `isdecimal()` | Decimal digits only | `"123".isdecimal()` | `True` |
| `isnumeric()` | Numeric chars (incl. unicode) | `"Ⅻ".isnumeric()` | `True` |
| `isalnum()` | Letters or digits only | `"a1".isalnum()` | `True` |
| `isspace()` | Whitespace only | `"   ".isspace()` | `True` |
| `islower()` | All lowercase | `"abc".islower()` | `True` |
| `isupper()` | All uppercase | `"ABC".isupper()` | `True` |
| `istitle()` | Title case | `"Hello World".istitle()` | `True` |
| `isascii()` | ASCII only | `"abc".isascii()` | `True` |
| `isidentifier()` | Valid Python identifier | `"name_1".isidentifier()` | `True` |
| `isprintable()` | Printable chars only | `"hi\n".isprintable()` | `False` |

---

## Other advanced / useful methods
| Method | What it does | Example code | Result |
|---|---|---|---|
| `encode(enc)` | Convert to bytes | `"hi".encode("utf-8")` | `b"hi"` |
| `expandtabs(n)` | Replace `\t` with spaces | `"a\tb".expandtabs(4)` | `"a   b"` |
| `translate(table)` | Replace multiple chars using mapping | `"a-b".translate(str.maketrans({"-":"_"}))` | `"a_b"` |
| `str.maketrans(...)` | Build mapping for `translate()` | `tbl = str.maketrans({"-":"_"})` | `tbl` (mapping) |
| `removeprefix(x)` | Remove prefix if present | `"unhappy".removeprefix("un")` | `"happy"` |
| `removesuffix(x)` | Remove suffix if present | `"file.txt".removesuffix(".txt")` | `"file"` |

---

### Notes
- `find()` returns `-1` if not found, but `index()` raises an error.
- `translate()` is great for many replacements at once (faster/cleaner than chaining `replace()` many times).
