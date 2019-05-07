N = int(input())
As = []
minus = 0
for c in input().split(" "):
  tmp = int(c)
  if tmp<0:
    minus += 1
    As.append(-tmp)
  else:
    As.append(tmp)

if minus%2==0:
  print(sum(As))
else:
  print(sum(As) - 2 * min(As))
