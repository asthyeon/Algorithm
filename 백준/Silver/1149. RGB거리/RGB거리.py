import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
"""
# RGB거리 (1149)
 1. 집을 빨강, 초록, 파랑 중 하나의 색으로 칠해야 함
 2. 색을 칠하는 규칙
  - 1번 집의 색은 2번 집의 색과 같지 않아야 한다
  - N번 집의 색은 N-1번 집의 색과 같지 않아야 한다
  - i번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다
[입력]
 1. N: 집의 수
 2. N개의 줄: 각 집을 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어짐
[출력]
 1. 모든 집을 칠하는 비용의 최솟값 출력
"""

"""
<풀이>
 1. dp
"""


def dynamic_programming(houses):
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0] = houses[0]

    for i in range(1, N):
        for j in range(3):
            # 색상 별로 겹치지 않게 색칠하기
            if j == 0:
                dp[i][j] = min(dp[i - 1][j + 1], dp[i - 1][j + 2]) + houses[i][j]
            elif j == 1:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j + 1]) + houses[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j - 2], dp[i - 1][j - 1]) + houses[i][j]
    
    # 최소 비용 출력
    return min(dp[N - 1])


N = int(input())
houses = []
for _ in range(N):
    R, G, B = map(int, input().split())
    houses.append([R, G, B])

print(dynamic_programming(houses))