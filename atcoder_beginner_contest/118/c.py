import fractions

n = int(input())
ms = list(map(int, input().split(" ")))
ans = ms[0]

for i in ms[1:]:
    ans = fractions.gcd(ans, i)

print(ans)
