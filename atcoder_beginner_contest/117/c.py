n, m = map(int, input().split(" "))
if n >= m:
    print(0)
else:
    ls = list(sorted(map(int, input().split(" "))))
    total = ls[-1] - ls[0]
    sections = sorted([ls[i + 1] - ls[i] for i in range(m - 1)], reverse=True)
    print(total - sum(sections[:n - 1]))
