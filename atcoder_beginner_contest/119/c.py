def grouping(data, n):
    return _grouping(data, n, 0)


def _grouping(data, n, c):
    if c == len(data):
        return [tuple([] for _ in range(n))]
    else:
        tg = data[c]
        b = _grouping(data, n, c + 1)
        a = []
        for i in range(n):
            for t in b:
                a.append(tuple(e + [tg] if idx == i else e for idx, e in enumerate(t)))
        return a


n, a, b, c = map(int, input().split(" "))
reqs = (a, b, c)
ls = [int(input()) for _ in range(n)]
gr = filter(lambda x: len(x[0]) != 0 and len(x[1]) != 0 and len(x[2]) != 0, grouping(ls, 4))
print(min(sum(10 * (len(es) - 1) + abs(sum(es) - r) for es, r in zip(t, reqs)) for t in gr))
