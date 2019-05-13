n = int(input())
ls = list(map(int, input().split(" ")))
print("Yes" if 2 * max(ls) < sum(ls) else "No")
