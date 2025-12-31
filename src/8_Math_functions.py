"""
Math Functions Demo (Python)

Run:
    python 8_Math_functions.py

Note:
- Uses the `math` module + a few built-in numeric helpers.
"""

import math


def show(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def demo(expr: str, value) -> None:
    print(f"{expr:<60} -> {value!r}")


def builtins_demo() -> None:
    show("Built-in numeric helpers (no import)")
    demo("abs(-5)", abs(-5))
    demo("round(3.14159, 2)", round(3.14159, 2))
    demo("pow(2, 3)", pow(2, 3))
    demo("divmod(10, 3)", divmod(10, 3))
    demo("sum([1, 2, 3])", sum([1, 2, 3]))
    demo("min(3, 7, 2)", min(3, 7, 2))
    demo("max(3, 7, 2)", max(3, 7, 2))


def constants_demo() -> None:
    show("math constants")
    for name in ["pi", "e", "tau", "inf", "nan"]:
        if hasattr(math, name):
            demo(f"math.{name}", getattr(math, name))


def rounding_demo() -> None:
    show("Rounding / integer-like operations")
    demo("math.ceil(3.1)", math.ceil(3.1))
    demo("math.floor(3.9)", math.floor(3.9))
    demo("math.trunc(-3.9)", math.trunc(-3.9))
    demo("math.fabs(-5)", math.fabs(-5))
    demo("math.fmod(7, 3)", math.fmod(7, 3))
    if hasattr(math, "remainder"):
        demo("math.remainder(8, 3)", math.remainder(8, 3))
    demo("math.modf(3.14)", math.modf(3.14))
    demo("math.frexp(8)", math.frexp(8))
    demo("math.ldexp(0.5, 4)", math.ldexp(0.5, 4))
    demo("math.copysign(3, -1)", math.copysign(3, -1))
    demo("math.isclose(0.1 + 0.2, 0.3)", math.isclose(0.1 + 0.2, 0.3))


def power_log_demo() -> None:
    show("Powers / roots / logarithms")
    demo("math.sqrt(16)", math.sqrt(16))
    demo("math.isqrt(17)", math.isqrt(17))
    demo("math.pow(2, 3)", math.pow(2, 3))
    demo("math.exp(1)", math.exp(1))
    demo("math.exp2(10)", math.exp2(10))
    demo("math.expm1(1)", math.expm1(1))
    demo("math.log(8, 2)", math.log(8, 2))
    demo("math.log1p(0.5)", math.log1p(0.5))
    demo("math.log2(8)", math.log2(8))
    demo("math.log10(1000)", math.log10(1000))
    if hasattr(math, "cbrt"):
        demo("math.cbrt(27)", math.cbrt(27))


def trig_demo() -> None:
    show("Trigonometry (radians)")
    demo("math.sin(math.pi/2)", math.sin(math.pi / 2))
    demo("math.cos(0)", math.cos(0))
    demo("math.tan(0)", math.tan(0))
    demo("math.asin(1)", math.asin(1))
    demo("math.acos(1)", math.acos(1))
    demo("math.atan(1)", math.atan(1))
    demo("math.atan2(1, 1)", math.atan2(1, 1))
    demo("math.degrees(math.pi)", math.degrees(math.pi))
    demo("math.radians(180)", math.radians(180))


def hyperbolic_demo() -> None:
    show("Hyperbolic functions")
    demo("math.sinh(0)", math.sinh(0))
    demo("math.cosh(0)", math.cosh(0))
    demo("math.tanh(0)", math.tanh(0))
    demo("math.asinh(1)", math.asinh(1))
    demo("math.acosh(1)", math.acosh(1))
    demo("math.atanh(0.5)", math.atanh(0.5))


def combinatorics_demo() -> None:
    show("Combinatorics / number theory")
    demo("math.factorial(5)", math.factorial(5))
    demo("math.comb(5, 2)", math.comb(5, 2))
    demo("math.perm(5, 2)", math.perm(5, 2))
    demo("math.gcd(12, 18)", math.gcd(12, 18))
    demo("math.lcm(12, 18)", math.lcm(12, 18))


def geometry_demo() -> None:
    show("Geometry / distances / precision helpers")
    demo("math.hypot(3, 4)", math.hypot(3, 4))
    demo("math.dist([0,0], [3,4])", math.dist([0, 0], [3, 4]))
    demo("math.fsum([0.1] * 10)", math.fsum([0.1] * 10))
    demo("math.prod([1,2,3,4])", math.prod([1, 2, 3, 4]))


def special_demo() -> None:
    show("Special functions")
    demo("math.gamma(6)", math.gamma(6))
    demo("math.lgamma(6)", math.lgamma(6))
    demo("math.erf(1)", math.erf(1))
    demo("math.erfc(1)", math.erfc(1))


def float_helpers_demo() -> None:
    show("Float checks / stepping")
    demo("math.isfinite(1.0)", math.isfinite(1.0))
    demo("math.isinf(math.inf)", math.isinf(math.inf))
    demo("math.isnan(math.nan)", math.isnan(math.nan))
    if hasattr(math, "nextafter"):
        demo("math.nextafter(1.0, 2.0)", math.nextafter(1.0, 2.0))
    if hasattr(math, "ulp"):
        demo("math.ulp(1.0)", math.ulp(1.0))


def main() -> None:
    builtins_demo()
    constants_demo()
    rounding_demo()
    power_log_demo()
    trig_demo()
    hyperbolic_demo()
    combinatorics_demo()
    geometry_demo()
    special_demo()
    float_helpers_demo()
    print("\nDone ✅")


if __name__ == "__main__":
    main()
