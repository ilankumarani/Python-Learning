"""29_Positional_only_arguments.py

Demo: Positional-only parameters (Python 3.8+)

Key idea:
- Parameters BEFORE '/' are positional-only.
- You cannot pass them as keyword arguments.

Run:
    python 29_Positional_only_arguments.py
"""

def f(a, b, /, c, d=10):
    """a and b are positional-only; c and d are normal (positional or keyword)."""
    return a, b, c, d


def only_positional(a, b, /):
    """Both a and b are positional-only."""
    return a + b


def mixed_posonly_kwonly(a, b, /, *, c, d=10):
    """a,b are positional-only; c,d are keyword-only."""
    return a, b, c, d


def main():
    print("=== Positional-only demo ===")

    # ✅ RIGHT: pass positional-only args by position
    print("f(1, 2, 3, 4) ->", f(1, 2, 3, 4))
    print("f(1, 2, c=3)  ->", f(1, 2, c=3))  # c can be keyword

    # ✅ RIGHT: only_positional must be called with position
    print("only_positional(5, 7) ->", only_positional(5, 7))

    # ✅ RIGHT: mix pos-only + kw-only
    print("mixed_posonly_kwonly(1, 2, c=3) ->", mixed_posonly_kwonly(1, 2, c=3))

    print("\n--- Wrong calls (commented out) ---")

    # ❌ WRONG: a and b are positional-only, so keywords are not allowed.
    # f(a=1, b=2, c=3)

    # ❌ WRONG: b is positional-only (because it's before '/'), so you can't use b=...
    # f(1, b=2, c=3)

    # ❌ WRONG: only_positional parameters are positional-only; keywords are not allowed.
    # only_positional(a=5, b=7)

    # ❌ WRONG: mixed_posonly_kwonly: a,b are positional-only; cannot use a= or b=
    # mixed_posonly_kwonly(a=1, b=2, c=3)

    print("\nTip: Uncomment wrong calls one-by-one to see the exact TypeError.")


if __name__ == "__main__":
    main()
