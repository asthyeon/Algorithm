import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 제곱수의 합
 1. 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있음
[입력]
 1. 자연수 N
[출력]
 1. 주어진 자연수를 제곱수 합으로 나타낼 때에 그 제곱수 항의 최소 개수 출력
"""

"""
<풀이>
 1. dp 이용
  1: 1
  2: 1 + 1
  3: 1 + 1 + 1
  4: 2
  5: 2 + 1
  6: 2 + 1 + 1
  7: 2 + 1 + 1 + 1
  8: 2 + 2
  9: 3
  10: 3 + 1
"""
from math import sqrt
# 제곱수 리스트
squares = []

# dp
def dynamic_programming(N):
    # 기본 값은 1의 제곱수로만 구성했을 때의 수
    dp = [i for i in range(N + 1)]

    # 원래의 수 순회
    for origin in range(1, N + 1):
        # 제곱수라면 1
        if sqrt(origin) == int(sqrt(origin)):
            dp[origin] = 1
            # 제곱수 리스트에 넣기
            squares.append(origin)
        # 제곱수가 아니라면
        else:
            # 제곱수 순회
            for square in squares:
                # 제곱수를 순회하며 최소값이 쓰일 때
                dp[origin] = min(dp[origin], dp[origin - square] + dp[square])

    return dp[N]


# 자연수 N
N = int(input())

print(dynamic_programming(N))