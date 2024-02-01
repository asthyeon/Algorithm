import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 오르막 수
 1. 오르막 수: 수의 자리가 오름차순을 이루는 수
 2. 인접한 수가 같아도 오름차순으로 분류
 3. 수의 길이 N이 주어졌을 때 오르막 수의 개수를 구하기
[입력]
 1. 수의 길이 N
[출력]
 1. 길이가 N인 오르막 수의 개수를 10,007로 나눈 나머지 출력
"""

"""
<풀이>
 1. dp 이용
  - 1: 10  (1 + 1 + 1 +  1 +  1 +  1 +  1 +  1 +  1 +  1)
  - 2: 55  (1 + 2 + 3 +  4 +  5 +  6 +  7 +  8 +  9 + 10)
  - 3: 220 (1 + 3 + 6 + 10 + 15 + 21 + 28 + 36 + 45 + 55)
 2. dp[0] = 1 고정, dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
"""


# dp
def dynamic_programming(N):
    # 기본값 1 부여
    dp = [[1] * 10 for _ in range(N)]

    # N의 길이만큼 반복
    for i in range(1, N):
        # 숫자 0 ~ 9 반복
        for j in range(1, 10):
            # 해당 값은 왼쪽과 위쪽의 합
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    # 해당 줄의 합
    return sum(dp[N - 1]) % 10007


# 수의 길이 N
N = int(input())

print(dynamic_programming(N))