# https://atcoder.jp/contests/abc121/tasks/abc121_c
N, M = map(int, input().split(" "))
stores = []
for i in range(N):
    Ai, Bi = map(int, input().split(" "))
    tg_idx = -1
    for idx, s in enumerate(stores):
        if s[0] > Ai:
            tg_idx = idx
            break
    if tg_idx != -1:
        stores.insert(tg_idx, (Ai, Bi))
    else:
        stores.append((Ai, Bi))

    stock = 0
    unuse_idx = -1
    for idx, s in enumerate(stores):
        if stock <= M:
            stock += s[1]
        else:
            unuse_idx = idx
    if unuse_idx != -1:
        stores = stores[:unuse_idx]
print(stores)

price = 0
for store in stores:
    if M <= store[1]:
        price += store[0] * M
        break
    else:
        price += store[0] * store[1]
        M -= store[1]
print(price)
