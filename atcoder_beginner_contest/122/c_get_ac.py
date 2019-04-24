# A, C, G, Tからなる長さNの文字列Sが与えられます。以下のQこの問いに答えてください。
# 問i(1<i<Q): 整数l_i, r_i(1<=l_i<=r_i<=N)が与えられる。Sの先頭からl_i文字目からr_i文字目までの部分文字列を考える。
# この時文字列に'AC'は部分文字列として何回現れるか
N, Q = map(int, input().split(" "))
S = input()
bi_gram = [1 if S[k:k + 2] == "AC" else 0 for k in range(N - 1)]
qs = [list(map(int, input().split(" "))) for i in range(Q)]

for q in qs:
    print(sum(bi_gram[q[0] - 1: q[1] - 1]))
