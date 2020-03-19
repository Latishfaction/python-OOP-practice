import clearterm


def top(start, end):
    cur = start
    while cur <= end:
        yield cur
        cur += 1


tt = top(1, 10)
for i in tt:
    print(i)
