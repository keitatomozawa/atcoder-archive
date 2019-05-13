n, m = map(int, input().split(" "))
sets = [set(list(map(int, input().split(" ")))[1:]) for _ in range(n)]

ans = set(i for i in range(1, m + 1))

for favset in sets:
    ans = ans & favset

print(len(ans))
