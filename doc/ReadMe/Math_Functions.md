# Python `math` (and numeric) Functions — README Cheat Sheet

# Run this (it prints every name in your installed Python’s math):
```python
import math
print([n for n in dir(math) if not n.startswith("_")])
```
```shell
python -c "print([n for n in dir(str) if not n.startswith('_')])"

python -c "import math; print([n for n in dir(math) if not n.startswith(\"_\")])"
```

> Same style/format as your `String_Methods.md` cheat sheet. fileciteturn1file0
## Built-in numeric helpers (no import)
| Function | What it does | Example code | Result |
|---|---|---|---|
| `abs(x)` | Absolute value | `abs(-5)` | `5` |
| `round(x, n)` | Round to n digits (banker’s rounding for .5 cases) | `round(3.14159, 2)` | `3.14` |
| `pow(x, y[, mod])` | Power (optionally modular) | `pow(2, 3)` | `8` |
| `divmod(a, b)` | Quotient + remainder | `divmod(10, 3)` | `(3, 1)` |
| `sum(iterable)` | Sum of values | `sum([1, 2, 3])` | `6` |
| `min(...)` | Smallest value | `min(3, 7, 2)` | `2` |
| `max(...)` | Largest value | `max(3, 7, 2)` | `7` |

---

## `math` constants
| Name | What it is | Example code | Result |
|---|---|---|---|
| `pi` | π (pi) | `math.pi` | `3.141592653589793` |
| `e` | Euler’s number | `math.e` | `2.718281828459045` |
| `tau` | 2π | `math.tau` | `6.283185307179586` |
| `inf` | Infinity | `math.inf` | `inf` |
| `nan` | Not-a-Number | `math.nan` | `nan` |

---

## Rounding / integer-like operations
| Function | What it does | Example code | Result |
|---|---|---|---|
| `ceil(x)` | Round up to nearest int | `math.ceil(3.1)` | `4` |
| `floor(x)` | Round down to nearest int | `math.floor(3.9)` | `3` |
| `trunc(x)` | Drop fractional part (toward 0) | `math.trunc(-3.9)` | `-3` |
| `fabs(x)` | Absolute value (returns float) | `math.fabs(-5)` | `5.0` |
| `fmod(x, y)` | Remainder with sign of x (float) | `math.fmod(7, 3)` | `1.0` |
| `remainder(x, y)` | IEEE 754-style remainder | `math.remainder(8, 3)` | `-1.0` |
| `modf(x)` | Split into (fractional, integer) parts | `math.modf(3.14)` | `(0.14000000000000012, 3.0)` |
| `frexp(x)` | Return (mantissa, exponent) such that x = m*2**e | `math.frexp(8)` | `(0.5, 4)` |
| `ldexp(m, e)` | Return m * (2**e) (inverse of frexp) | `math.ldexp(0.5, 4)` | `8.0` |
| `copysign(x, y)` | Copy sign of y onto magnitude of x | `math.copysign(3, -1)` | `-3.0` |

---

## Powers / roots / logarithms
| Function | What it does | Example code | Result |
|---|---|---|---|
| `sqrt(x)` | Square root | `math.sqrt(16)` | `4.0` |
| `isqrt(n)` | Integer square root (floor of sqrt) | `math.isqrt(17)` | `4` |
| `pow(x, y)` | Power (float result) | `math.pow(2, 3)` | `8.0` |
| `exp(x)` | e**x | `math.exp(1)` | `2.718281828459045` |
| `exp2(x)` | 2**x | `math.exp2(10)` | `1024.0` |
| `expm1(x)` | e**x - 1 (better precision for small x) | `math.expm1(1)` | `1.718281828459045` |
| `log(x, base)` | Log with optional base | `math.log(8, 2)` | `3.0` |
| `log1p(x)` | log(1+x) (better precision for small x) | `math.log1p(0.5)` | `0.4054651081081644` |
| `log2(x)` | Log base 2 | `math.log2(8)` | `3.0` |
| `log10(x)` | Log base 10 | `math.log10(1000)` | `3.0` |
| *(optional)* | *(available in newer Python)* |  |  |
| `cbrt(x)` | Cube root | `math.cbrt(27)` | `3.0000000000000004` |

---

## Trigonometry (angles are in **radians**)
| Function | What it does | Example code | Result |
|---|---|---|---|
| `sin(x)` | Sine | `math.sin(math.pi/2)` | `1.0` |
| `cos(x)` | Cosine | `math.cos(0)` | `1.0` |
| `tan(x)` | Tangent | `math.tan(0)` | `0.0` |
| `asin(x)` | Inverse sine | `math.asin(1)` | `1.5707963267948966` |
| `acos(x)` | Inverse cosine | `math.acos(1)` | `0.0` |
| `atan(x)` | Inverse tangent | `math.atan(1)` | `0.7853981633974483` |
| `atan2(y, x)` | Angle of vector (x,y) | `math.atan2(1, 1)` | `0.7853981633974483` |
| `degrees(x)` | Radians → degrees | `math.degrees(math.pi)` | `180.0` |
| `radians(x)` | Degrees → radians | `math.radians(180)` | `3.141592653589793` |

---

## Hyperbolic functions
| Function | What it does | Example code | Result |
|---|---|---|---|
| `sinh(x)` | Hyperbolic sine | `math.sinh(0)` | `0.0` |
| `cosh(x)` | Hyperbolic cosine | `math.cosh(0)` | `1.0` |
| `tanh(x)` | Hyperbolic tangent | `math.tanh(0)` | `0.0` |
| `asinh(x)` | Inverse hyperbolic sine | `math.asinh(1)` | `0.881373587019543` |
| `acosh(x)` | Inverse hyperbolic cosine | `math.acosh(1)` | `0.0` |
| `atanh(x)` | Inverse hyperbolic tangent | `math.atanh(0.5)` | `0.5493061443340548` |

---

## Combinatorics / number theory
| Function | What it does | Example code | Result |
|---|---|---|---|
| `factorial(n)` | n! factorial | `math.factorial(5)` | `120` |
| `comb(n, k)` | n choose k combinations | `math.comb(5, 2)` | `10` |
| `perm(n, k)` | nP k permutations | `math.perm(5, 2)` | `20` |
| `gcd(*ints)` | Greatest common divisor | `math.gcd(12, 18)` | `6` |
| `lcm(*ints)` | Least common multiple | `math.lcm(12, 18)` | `36` |

---

## Geometry / distances / precision helpers
| Function | What it does | Example code | Result |
|---|---|---|---|
| `hypot(*coords)` | Euclidean norm (length) | `math.hypot(3, 4)` | `5.0` |
| `dist(p, q)` | Distance between 2 points | `math.dist([0, 0], [3, 4])` | `5.0` |
| `fsum(iterable)` | High-precision floating sum | `math.fsum([0.1] * 10)` | `1.0` |
| `prod(iterable)` | Product of values | `math.prod([1, 2, 3, 4])` | `24` |
| `isclose(a, b)` | Check floats are “close enough” | `math.isclose(0.1 + 0.2, 0.3)` | `True` |

---

## Special functions
| Function | What it does | Example code | Result |
|---|---|---|---|
| `gamma(x)` | Gamma function (Γ); Γ(n) = (n-1)! for ints | `math.gamma(6)` | `120.0` |
| `lgamma(x)` | Natural log of |Γ(x)| | `math.lgamma(6)` | `4.787491742782047` |
| `erf(x)` | Error function | `math.erf(1)` | `0.8427007929497149` |
| `erfc(x)` | Complementary error function (1 - erf(x)) | `math.erfc(1)` | `0.15729920705028513` |

---

## Float checks / stepping
| Function | What it does | Example code | Result |
|---|---|---|---|
| `isfinite(x)` | True if not inf/nan | `math.isfinite(1.0)` | `True` |
| `isinf(x)` | True if +/- infinity | `math.isinf(math.inf)` | `True` |
| `isnan(x)` | True if NaN | `math.isnan(math.nan)` | `True` |
| `nextafter(x, y)` | Next representable float from x toward y | `math.nextafter(1.0, 2.0)` | `1.0000000000000002` |
| `ulp(x)` | Unit in the last place for x | `math.ulp(1.0)` | `2.220446049250313e-16` |

---

### Notes
- `math` functions generally work with **real numbers** (floats). For complex numbers, use the `cmath` module.
- Angles for trig functions are in **radians**. Use `math.radians()` and `math.degrees()` for conversion.
- `math.fsum()` is better than `sum()` when you need high precision for floats.