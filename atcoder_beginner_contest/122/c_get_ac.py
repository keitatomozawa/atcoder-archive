# A, C, G, Tからなる長さNの文字列Sが与えられます。以下のQこの問いに答えてください。
# 問i(1<i<Q): 整数l_i, r_i(1<=l_i<=r_i<=N)が与えられる。Sの先頭からl_i文字目からr_i文字目までの部分文字列を考える。
# この時文字列に'AC'は部分文字列として何回現れるか
N, Q = map(int, input().split(" "))
S = input()
ac_cnts = []
ac_cnt = 0
for i in range(N-1):
    if S[i:i+2] == "AC":
        ac_cnt += 1
    ac_cnts.append(ac_cnt)


for j in range(Q):
    l, r = map(int, input().split(" "))
    print(ac_cnts[r] - ac_cnts[l-2])
