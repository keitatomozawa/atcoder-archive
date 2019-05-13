n, k = map(int, input().split(" "))
b_k = list(map(int, format(k + 1, "b").zfill(40)[::-1]))
target = [0 for _ in range(40)]
numbers = list(map(int, input().split(" ")))
for i in numbers:
    for idx, v in enumerate(format(i, "b")[::-1]):
        if v == "1":
            target[idx] += 1
best = [1 if n > 2 * target[i] else 0 for i in range(40)]

maxr = sum(numbers)
for i in range(len(b_k)):
    if b_k[i] == 1:
        maxr = max(maxr, sum((2 ** idx) * (t if r == 0 else n - t) for idx, (t, r) in
                             enumerate(zip(target, best[:i] + [0] + b_k[i + 1:]))))
print(maxr)
