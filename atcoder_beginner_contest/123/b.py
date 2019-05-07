menus = list(map(lambda x: (x - x % 10, x % 10), [int(input()) for _ in range(5)]))
tens = [ i[0] for i in menus ]
mods = sorted(list(filter(lambda x: x != 0, [ i[1] for i in menus])))
print(sum(tens) + ((mods[0] + 10*(len(mods) - 1))if len(mods) > 0 else 0))
