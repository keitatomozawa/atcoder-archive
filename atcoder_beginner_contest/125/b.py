n = int(input())
vs = map(int, input().split(" "))
cs = map(int, input().split(" "))

print(sum(filter(lambda i: i > 0, map(lambda i: i[0] - i[1],zip(vs, cs)))))

