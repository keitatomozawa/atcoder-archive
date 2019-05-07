import fractions

n = int(input())
As = list(map(int, input().split(" ")))

largest = 1

for i in range(n):
  gcd = 0
  for idx, j in enumerate(As):
    if idx == i:
      continue
    gcd = j if gcd==0 else fractions.gcd(gcd, j)
    if gcd <= largest:
      break
  if gcd > largest:
    largest = gcd

print(largest)

