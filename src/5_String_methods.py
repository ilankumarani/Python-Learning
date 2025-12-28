"""
String Methods Demo
Generated from String_Functions.md

Run:
    python 5_String_methods.py
"""

def show(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

def demo(expr: str, value) -> None:
    """Pretty-print an expression and its evaluated result."""
    print(f"{expr:<55} -> {value!r}")

def formatting() -> None:
    show("Formatting")
    demo('\"Hi {}, age {}\".format(\"Sam\", 30)', "Hi {}, age {}".format("Sam", 30))
    demo('\"Hi {name}\".format_map({\"name\":\"Sam\"})', "Hi {name}".format_map({"name": "Sam"}))

def search_replace() -> None:
    show("Search / Replace")
    demo('\"hello\".find(\"ll\")', "hello".find("ll"))
    demo('\"ababa\".rfind(\"ba\")', "ababa".rfind("ba"))
    demo('\"hello\".index(\"ll\")', "hello".index("ll"))
    demo('\"ababa\".rindex(\"ba\")', "ababa".rindex("ba"))
    demo('\"banana\".count(\"an\")', "banana".count("an"))
    demo('\"a-b\".replace(\"-\", \"_\")', "a-b".replace("-", "_"))
    demo('\"hello\".startswith(\"he\")', "hello".startswith("he"))
    demo('\"hello\".endswith(\"lo\")', "hello".endswith("lo"))

def split_join() -> None:
    show("Split / Join")
    demo('\"a,b,c\".split(\",\")', "a,b,c".split(","))
    demo('\"a,b,c\".rsplit(\",\", 1)', "a,b,c".rsplit(",", 1))
    demo('\"a\\nb\".splitlines()', "a\nb".splitlines())
    demo('\"-\".join([\"a\",\"b\"])', "-".join(["a", "b"]))
    demo('\"a=b=c\".partition(\"=\")', "a=b=c".partition("="))
    demo('\"a=b=c\".rpartition(\"=\")', "a=b=c".rpartition("="))

def case_conversions() -> None:
    show("Case conversions")
    demo('\"HeLLo\".lower()', "HeLLo".lower())
    demo('\"HeLLo\".upper()', "HeLLo".upper())
    demo('\"hello\".capitalize()', "hello".capitalize())
    demo('\"hello world\".title()', "hello world".title())
    demo('\"HeLLo\".swapcase()', "HeLLo".swapcase())
    demo('\"ß\".casefold()', "ß".casefold())

def trim_padding() -> None:
    show("Trim / Padding (Alignment)")
    demo('\"  hi  \".strip()', "  hi  ".strip())
    demo('\"  hi\".lstrip()', "  hi".lstrip())
    demo('\"hi  \".rstrip()', "hi  ".rstrip())
    demo('\"hi\".center(6)', "hi".center(6))
    demo('\"hi\".ljust(5)', "hi".ljust(5))
    demo('\"hi\".rjust(5)', "hi".rjust(5))
    demo('\"42\".zfill(5)', "42".zfill(5))

def checks_true_false() -> None:
    show("Checks (True/False methods)")
    demo('\"abc\".isalpha()', "abc".isalpha())
    demo('\"123\".isdigit()', "123".isdigit())
    demo('\"123\".isdecimal()', "123".isdecimal())
    demo('\"Ⅻ\".isnumeric()', "Ⅻ".isnumeric())
    demo('\"a1\".isalnum()', "a1".isalnum())
    demo('\"   \".isspace()', "   ".isspace())
    demo('\"abc\".islower()', "abc".islower())
    demo('\"ABC\".isupper()', "ABC".isupper())
    demo('\"Hello World\".istitle()', "Hello World".istitle())
    demo('\"abc\".isascii()', "abc".isascii())
    demo('\"name_1\".isidentifier()', "name_1".isidentifier())
    demo('\"hi\\n\".isprintable()', "hi\n".isprintable())

def other_advanced() -> None:
    show("Other advanced / useful methods")
    demo('\"hi\".encode(\"utf-8\")', "hi".encode("utf-8"))
    demo('\"a\\tb\".expandtabs(4)', "a\tb".expandtabs(4))

    tbl = str.maketrans({"-": "_"})
    demo('tbl = str.maketrans({\"-\":\"_\"})', tbl)
    demo('\"a-b\".translate(tbl)', "a-b".translate(tbl))

    demo('\"unhappy\".removeprefix(\"un\")', "unhappy".removeprefix("un"))
    demo('\"file.txt\".removesuffix(\".txt\")', "file.txt".removesuffix(".txt"))

def main() -> None:
    formatting()
    search_replace()
    split_join()
    case_conversions()
    trim_padding()
    checks_true_false()
    other_advanced()
    print("\nDone ✅")

if __name__ == "__main__":
    main()
