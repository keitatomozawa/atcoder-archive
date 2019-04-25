# https://gyazo.com/7686815f630fab87047428e24934bffa
# https://atcoder.jp/contests/abc121/tasks/abc121_b
N, M, C = map(int, input().split(" "))
Bs = list(map(int, input().split(" ")))
c = 0

for i in range(N):
    Ais = map(int, input().split(" "))
    if sum([a*b for a, b in zip(Ais, Bs)]) + C > 0:
        c += 1

print(c)
