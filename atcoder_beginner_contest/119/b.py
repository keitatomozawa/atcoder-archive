n = int(input())
s = 0
for i in range(n):
  am, un = input().split(" ")
  s += float(am) if un=="JPY" else float(am)*380000.0
print(s)
