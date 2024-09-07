import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 걷다보니 신천역 삼 (Large) (14651)
 1. 3개의 숫자(0, 1, 2)만 가지고 N자리 3의 배수 만들기
 2. 0으로 시작하는 수는 만들 수 없음
[입력]
 1. N: 목표 자리 수
[출력]
 1. 0, 1, 2만 가지고 만들 수 있는 N자리 3의 배수의 개수 출력
 2. 답을 1,000,000,009로 나눈 나머지 출력
"""

"""
<풀이>
 1. dp
N = 1 [0]
N = 2 12, 21 [2]
N = 3 [6] + 4
N = 4 [18] + 12
N = 5 [54] + 36
N = 6 [162] + 108
"""


# dp
def dynamic_programming(N):
    dp = [0] * (N + 1)

    for i in range(2, N + 1):
        if i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 6
        else:
            dp[i] = dp[i - 1] + (dp[i - 1] - dp[i - 2]) * 3

    return dp[N] % 1000000009


N = int(input())

print(dynamic_programming(N))