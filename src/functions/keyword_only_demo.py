"""keyword_only_demo.py

Demo: Keyword-only parameters

Key idea:
- Parameters AFTER '*' (or after '*args') are keyword-only.
- You must pass them using name=value.

Run:
    python keyword_only_demo.py
"""

def send_email(to, *, subject, body):
    """subject and body are keyword-only."""
    return f"To={to}, subject={subject}, body={body}"


def connect(host, port=5432, *, timeout=10, ssl=True):
    """timeout and ssl are keyword-only options (safe API design)."""
    return f"host={host}, port={port}, timeout={timeout}, ssl={ssl}"


def f(a, b, *args, c, d=10):
    """c and d are keyword-only because they come after *args."""
    return a, b, args, c, d


def main():
    print("=== Keyword-only demo ===")

    # ✅ RIGHT: subject and body must be keywords
    print(send_email("a@b.com", subject="Hi", body="Hello"))

    # ✅ RIGHT: keyword-only options for connect
    print(connect("db.local", timeout=30, ssl=False))
    print(connect("db.local"))  # uses defaults for timeout/ssl

    # ✅ RIGHT: after *args, c must be keyword
    print("f(1,2,c=3) ->", f(1, 2, c=3))
    print("f(1,2,100,200,c=3,d=99) ->", f(1, 2, 100, 200, c=3, d=99))

    print("\n--- Wrong calls (commented out) ---")

    # ❌ WRONG: subject and body are keyword-only; passing positionally is not allowed.
    # send_email("a@b.com", "Hi", "Hello")

    # ❌ WRONG: timeout is keyword-only; you cannot pass it positionally.
    # connect("db.local", 5432, 30)

    # ❌ WRONG: c is keyword-only (after *args), so you must pass c=...
    # f(1, 2, 100, 200, 3)

    # ❌ WRONG: positional argument after keyword is not allowed (syntax error)
    # f(1, 2, c=3, 100)

    print("\nTip: Uncomment wrong calls one-by-one to see the exact error.")


if __name__ == "__main__":
    main()
