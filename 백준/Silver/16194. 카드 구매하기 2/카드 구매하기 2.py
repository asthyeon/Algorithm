import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 카드 구매하기 2 (16194)
 1. 돈을 최소로 지불해서 카드 N개 구매하기
[입력]
 1. N: 구매하려고 하는 카드 수
 2. P1 ~ PN: 각 카드의 가격 
[출력]
 1. 카드 N개를 갖기 위해 지불해야 하는 금액의 최솟값
"""

"""
<풀이>
 1. dp
"""


# dp
def dynamic_programming(N, P):
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            # 이번에 처음 계산되는 카드 수라면
            if dp[i] == 0:
                # 이전 개수를 살 때 필요한 금액 + 새로 필요한 금액
                dp[i] = dp[i - j] + P[j]
            # 이전에 계산되었던 카드 수라면
            else:
                # 이전에 계산된 금액 vs (이전 개수를 살 때 필요한 금액 + 새로 필요한 금액)
                dp[i] = min(dp[i], dp[i - j] + P[j])

    return dp[N]


N = int(input())
# 0장부터 N장까지 맞추기
P = [0] + list(map(int, input().split()))

print(dynamic_programming(N, P))