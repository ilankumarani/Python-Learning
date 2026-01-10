"""mro_example.py

Run:
    python mro_example.py

This file demonstrates Python's Method Resolution Order (MRO)
using a classic diamond inheritance pattern and cooperative super().
"""

from __future__ import annotations


class A:
    def hello(self) -> None:
        print("A.hello")


class B(A):
    def hello(self) -> None:
        print("B.hello")
        super().hello()


class C(A):
    def hello(self) -> None:
        print("C.hello")
        super().hello()


class D(B, C):
    def hello(self) -> None:
        print("D.hello")
        super().hello()


def main() -> None:
    d = D()
    d.hello()

    print("\nMRO for D:")
    for cls in D.mro():
        print(" -", cls.__name__)


if __name__ == "__main__":
    main()
