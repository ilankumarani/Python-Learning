# String ↔ int/float

x = "10"
a = int(x)        # 10 (int)
b = float(x)      # 10.0 (float)

y = 12
s = str(y)        # "12"


# Float ↔ int

f = 10.9
i = int(f)        # 10  (truncates, does NOT round)

i2 = round(f)     # 11  (rounding)


# Bool casting

bool(0)       # False
bool(1)       # True
bool("")      # False
bool("hi")    # True
bool([])      # False
bool([1])     # True


# List / tuple / set conversions

list("abc")           # ['a','b','c']
tuple([1, 2, 2])      # (1, 2, 2)
set([1, 2, 2])        # {1, 2}


# Safe casting (avoid crash)


s = "10a"
try:
    n = int(s)
except ValueError:
    n = None

print(f"Value n ::{n}")

