import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 안녕 (1535)
 1. 세준이를 생각해준 사람 1번 ~ N번
 2. i번 사람에게 인사를 하면 L[i]만큼 체력 잃고, J[i]만큼 기쁨 얻음
 3. 각각의 사람에게 최대 1번만 말할 수 있음
 4. 세준이의 체력은 100, 0 이하가 될시 기쁨을 못 느낌
 5. 주어진 체력 내에서 최대한의 기쁨 느끼기
[입력]
 1. N: 사람 수
 2. 둘째 줄: 인사할 때 잃는 체력
 3. 셋째 줄: 인사할 때 얻는 기쁨
[출력]
 1. 얻을 수 있는 최대 기쁨
"""

"""
<풀이>
 1. 일단 풀어보기 -> 백트래킹 -> 시간초과
 2. dp
"""


# dp
def dynamic_programming(N, healths, joys):
    # 모든 체력의 경우 구하기
    dp = [[0] * 101 for _ in range(N + 1)]

    # 사람 수만큼 순회
    for i in range(1, N + 1):
        # 체력 순회
        for j in range(1, 101):
            # 이전 값으로 교체
            dp[i][j] = dp[i - 1][j]

            # 만약 이번에 기쁨을 얻을 수 있다면
            if healths[i] <= j:
                # 현재 값과 기쁨을 얻었을 때 중 큰 값으로 교체
                dp[i][j] = max(dp[i][j], dp[i - 1][j - healths[i]] + joys[i])

    return dp[N][99]


# 사람 수
N = int(input())
# 잃는 체력 리스트
healths = [0] + list(map(int, input().split()))
# 얻는 기쁨 리스트
joys = [0] + list(map(int, input().split()))

print(dynamic_programming(N, healths, joys))