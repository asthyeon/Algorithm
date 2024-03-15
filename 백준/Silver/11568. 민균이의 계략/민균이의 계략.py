import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 민균이의 계략(11568)
 1. 카드 N장을 준민이에게 정해진 순서대로 보여줌
 2. 준민이 앞의 카드부터 임의의 개수만큼 골라 민균이에게 제시함
 3. 제시한 카드의 수열이 순증가하고 원소의 개수가 제일 많지 않으면 바보라고 놀림받음
[입력]
 1. N: 민균이가 제시한 카드의 수
 2. 두 번째 줄 -> 민균이가 제시한 카드 N개가 들어있는 정수가 주어짐
[출력]
 1. 준민이가 제시할 수 있는 수열의 원소의 최대 개수 출력
"""

"""
<풀이>
 1. 백트래킹 -> 시간초과
 2. dp 이용
"""


# dp
def dynamic_programming(cards):
    # 모든 원소는 최소 1개의 수열
    dp = [1] * N

    # start ~ end 순회(역방향)
    for end in range(1, N):
        for start in range(end):
            # 이번 start 수가 end 수보다 작다면
            if cards[start] < cards[end]:
                # 이전에 카운트한 수 + 1과 현재 수 중 더 큰값으로 교체
                dp[end] = max(dp[start] + 1, dp[end])

    return max(dp)


# 카드 수
N = int(input())
# 카드 정보
cards = list(map(int, input().split()))

print(dynamic_programming(cards))




