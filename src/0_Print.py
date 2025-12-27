


print("a", "b", "c")
# a b c   (separated by a space)

print("a", "b", "c", sep="-")
# a-b-c

print("year", 2025, sep=":")
# year:2025


print(1, 2, 3, sep=", ")
# behaves like: ", ".join(["1", "2", "3"])
# Output: 1, 2, 3


print("2025", "12", "23", sep="-")
# 2025-12-23

print("path", "to", "file", sep="/")
# path/to/file

print("a", "b", "c", sep="")
# abc   (no spaces at all)


x = print("path", "to", "file", sep="/")
print(f"hello {x}")
