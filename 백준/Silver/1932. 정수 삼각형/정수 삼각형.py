import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 정수 삼각형 (1932)
1. 맨 위층부터 아래에 있는 수 중 하나를 선택하여 내려올 때, 선택된 수의 합이 최대가 되는 경로

[풀이]
1. dp
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
"""


def dynamic_programming(triangle):
    dp = [[0] * n for _ in range(n)]
    # 초기값 설정
    dp[0][0] = triangle[0][0]

    # 두 번째 행 부터
    for x in range(1, n):
        # 행과 같은 값까지
        for y in range(x + 1):
            # 맨 좌측 값
            if y == 0:
                # 바로 대각선 우측 위 값
                dp[x][y] = dp[x - 1][y] + triangle[x][y]
            # 맨 우측 값
            elif y == x:
                # 바로 대각선 좌측 위 값
                dp[x][y] = dp[x - 1][y - 1] + triangle[x][y]
            # 사이 값
            else:
                # 좌측 위 값 vs 우측 위 값
                dp[x][y] = max(dp[x - 1][y - 1], dp[x - 1][y]) + triangle[x][y]

    # 마지막 줄 중 가장 큰 값
    return max(dp[n - 1])


n = int(input())
triangle = []
for _ in range(n):
    line = list(map(int, input().split()))
    triangle.append(line)

print(dynamic_programming(triangle))