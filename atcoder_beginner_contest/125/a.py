a, b, t = map(int, input().split(" "))
g = 1
c = 0

while a * g <= t:
  c += b
  g += 1

print(c)
