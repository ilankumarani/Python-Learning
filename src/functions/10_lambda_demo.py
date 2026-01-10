"""10_lambda_demo.py

Run:
    python 10_lambda_demo.py

This file demonstrates:
- Basic lambda usage
- Sorting with key=lambda
- Passing lambda to custom functions
- Right vs wrong examples (wrong ones are commented out with explanations)
"""

from typing import Callable, List, Dict


def apply(op: Callable[[int, int], int], x: int, y: int) -> int:
    """Applies a function (or lambda) to two integers."""
    return op(x, y)


def transform_list(items: List[int], func: Callable[[int], int]) -> List[int]:
    """Applies func to each item and returns a new list."""
    return [func(x) for x in items]


def run_twice(fn: Callable[[int], int], x: int) -> int:
    """Runs fn(fn(x))."""
    return fn(fn(x))


def main() -> None:
    print("=== 1) Basic lambda ===")
    add = lambda a, b: a + b
    print("add(2,3) ->", add(2, 3))

    print("\n=== 2) Sorting with key=lambda ===")
    people: List[Dict[str, int]] = [{"name": "Ilan", "age": 30}, {"name": "Bala", "age": 25}]
    people.sort(key=lambda p: p["age"])
    print("sorted by age ->", people)

    print("\n=== 3) Passing lambda to custom function ===")
    print("apply(mul, 3, 4) ->", apply(lambda a, b: a * b, 3, 4))

    print("\n=== 4) Transform list using lambda ===")
    print("squares ->", transform_list([1, 2, 3], lambda x: x * x))

    print("\n=== 5) One-expression conditional lambda ===")
    label = lambda n: "adult" if n >= 18 else "minor"
    print("label(20) ->", label(20))
    print("label(10) ->", label(10))

    print("\n=== 6) Run a lambda twice ===")
    print("run_twice(+1, 5) ->", run_twice(lambda n: n + 1, 5))  # (5+1)+1 = 7

    print("\n--- Wrong examples (commented out) ---")

    # ❌ WRONG: Python lambda must be a single expression (multi-line statements are not allowed)
    # bad = lambda x:
    #     y = x + 1
    #     return y

    # ❌ WRONG: Putting complex logic inside lambda hurts readability
    # complex_lambda = lambda x: (x * 2 if x > 10 else x / 2) + (x % 3)
    # Better: use a named function with clear steps.

    print("\nTip: Keep lambda short; use def for complex logic.")


if __name__ == "__main__":
    main()
