a, b = map(int, input().split(" "))
print(2*max(a, b) - (0 if a==b else 1))
