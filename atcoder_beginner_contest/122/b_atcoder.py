# 英大文字からなる文字列Sが与えられます。
# Sの部分文字列 (注記を参照) であるような最も長い ACGT 文字列 の長さを求めてください。
# ここで、ACGT 文字列とは A, C, G, T 以外の文字を含まない文字列です。
src = input()
length = len(src)
acgt = set("ACGT")
ans = 0
for i in range(length):
    n = length - i
    for ngram in [src[k:k+n] for k in range(length - n + 1)]:
        print(ngram)
        subtract = len(set(ngram) - acgt)
        if subtract == 0:
            ans = n
            break
    if ans != 0:
        break
print(ans)

