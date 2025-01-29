import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 동전 (9084)
 1. 동전들로 정수의 금액을 다양한 방법으로 만들 수 있음
[입력]
 1. T: 테스트 케이스의 개수
 2. N: 동전의 가지 수
 3. 두번째 줄: N가지 동전의 각 금액이 오름차순으로 정렬되어 주어짐
 4. M: 만들어야 할 금액
[출력]
 1. N가지 동전으로 금액 M을 만드는 모든 방법의 수 출력
"""

"""
<풀이>
 1. dp
"""


def dynamic_programming(coins):
    dp = [0] * (M + 1)
    # 모든 동전은 0원을 만들 수 있음
    dp[0] = 1

    # 각 동전 순회
    for coin in coins:
        # 모든 값 순회(각 인덱스는 동전의 합이 됨)
        for total in range(1, M + 1):
            # 이번 값이 동전 값보다 크거나 같을 때
            if total >= coin:
                # 이번 값에 이번 값에서 동전만큼 뺀 값을 만드는 가지 수를 더하기
                dp[total] += dp[total - coin]

    return dp[M]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    print(dynamic_programming(coins))