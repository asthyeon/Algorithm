import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

L = int(input())
N = int(input())
cake = [0] * (L + 1)
expect = en = 0
true = tn = 0

for i in range(1, N + 1):
    P, K = map(int, input().split())

    # 예상 방청객
    ex = K - P
    if expect < ex:
        expect = ex
        en = i

    # 실제 방청객
    cnt = 0
    for j in range(P, K + 1):
        if not cake[j]:
            cake[j] = i
            cnt += 1
    if true < cnt:
        true = cnt
        tn = i

print(en)
print(tn)