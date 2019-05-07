s = list(map(int, input()))
o = s[::2]
e = s[1::2]
l_o = len(o)
l_e = len(e)
o_o = sum(o)
o_e = sum(e)

print(min(l_o - o_o + o_e, o_o + l_e - o_e))
