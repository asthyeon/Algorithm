import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# Coins (3067)
 1. 동전의 종류가 주어질 때 주어진 금액을 만드는 모든 방법 세기
[입력]
 1. T: 테스트 케이스의 개수
 2. N: 동전의 가지 수 (1 <= N <= 20)
 3. 두번째 줄: N가지 동전의 각 금액이 오름차순으로 정렬되어 주어짐
 4. M: N가지 동전으로 만들어야 할 금액(1 <= M <= 10,000)
[출력]
 1. N가지 동전으로 금액 M을 만드는 모든 방법의 수 출력
"""

"""
<풀이>
 1. dp
 2. 동전 문제 -> 만들어야 할 금액을 인덱스로
"""


def dynamic_programing(M, coins):
    # M 원을 만들어야 함
    dp = [0] * (M + 1)

    # 동전 순회
    for coin in coins:
        # 이번 동전이 목표 금액 보다 작거나 같을 때
        if coin <= M:
            # 이 금액을 만드는 방법의 수 + 1
            dp[coin] += 1
            # 이 금액부터 목표 금액까지 이전에 사용한 동전으로 만드는 방법들의 수 더하기
            for i in range(coin + 1, M + 1):
                dp[i] += dp[i - coin]
        # 이번 동전이 목표 금액을 넘어가면 종료
        else:
            break

    return dp[M]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    # 동전 정렬
    coins.sort()

    print(dynamic_programing(M, coins))