import math
n = int(input())
state = [n, 0, 0, 0, 0, 0]
capacities = [int(input()) for _ in range(5)]
for i in range(1, 5):
    if capacities[i - 1] < capacities[i]:
        capacities[i] = capacities[i - 1]
print(4+math.ceil(n/capacities[4]))
