import time as tm
import datetime

## for Range between 50(Inclusive) and 100(Exclusive) and Count
for i in range(0, 10, 2):
    print(f"{i}")

print(f"\n========= for Range Count down timer =========")
## for Range between 50(Inclusive) and 100(Exclusive) and Count
for i in range(5, 0, -1):
    print(f"{i}")
    tm.sleep(1)
print(f"Happy new year", datetime.now().year, sep=" :: [", end="]")
