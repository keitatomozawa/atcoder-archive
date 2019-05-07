antennas = sorted([int(input()) for _ in range(5)])
k = int(input())

ds = []
for idx, antenna in enumerate(antennas):
    for j in range(idx+1, 5):
        ds.append(antennas[j] - antenna)

print("Yay!" if max(ds) <= k else ":(")

