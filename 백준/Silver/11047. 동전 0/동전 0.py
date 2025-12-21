import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 동전 0 (11047)
1. 동전 개수를 최소로 사용해서 K 만들기

[풀이]
1. 동전 역순으로 사용
"""


def calculator(K, coins):
    cnt = 0
    # 몫만큼 개수 더하기, 나머지만큼 금액 차감
    for coin in coins:
        cnt += K // coin
        K %= coin

    return cnt


N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))

# 역순 정렬
coins = sorted(coins, reverse=True)
print(calculator(K, coins))