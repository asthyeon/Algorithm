import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 목장 건설하기 (14925)
 1. 목장을 하나의 정사각형으로 최대한 크게 지으려고 하는데 그 안에 나무나 바위 없어야 함
 2. 0: 들판, 1: 나무, 2: 바위
[입력]
 1. M: 세로 길이, N: 가로 길이
 2. 행렬 정보
[출력]
 1. L: 정사각형 목장의 한 변의 크기 출력
"""

"""
<풀이>
 1. dp
 2. 정사각형이 될 수 있는 조건을 생각해보기
"""


# dp
def dynamic_programming(arr):
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    # 가장 큰 정사각형 한 변의 길이
    length = 0

    for x in range(1, M + 1):
        for y in range(1, N + 1):
            # 대각선 왼쪽 위가 들판이라면
            if arr[x - 1][y - 1] == 0:
                # 현재 값은 정사각형 변 중 가장 낮은 값
                dp[x][y] = min(dp[x - 1][y - 1], dp[x - 1][y], dp[x][y - 1]) + 1
                # 가장 큰 한 변의 길이 갱신
                length = max(length, dp[x][y])

    return length


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

print(dynamic_programming(arr))