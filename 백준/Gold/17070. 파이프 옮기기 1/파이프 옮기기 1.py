import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 파이프 옮기기 1 (17070)
 1. 파이프를 밀 수 있는 방향:  →, ↘, ↓
 2. 빈 칸은 0, 벽은 1
 3. 가장 처음 파이프는 가로 파이프
[입력]
 1. N: 집의 크기
 2. N개의 줄: 집의 상태
[출력]
 1. 파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수 출력
   (이동시킬 수 없는 경우에는 0을 출력)
"""

"""
<풀이>
 1. bfs -> 시간초과
 2. dp
"""


def dynamic_programming(house):
    # 3차원으로 가로, 세로, 대각선이 놓여 있는 dp 배열 생성
    dp = [[[0] * N for _ in range(N)] for _ in range(3)]

    # 시작 파이프
    dp[0][0][1] = 1
    # 첫 행은 가로 파이프만 가능
    for first in range(2, N):
        # 이번 칸이 벽이 아닐 때
        if house[0][first] == 0:
            # 이전 가로 파이프 잇기
            dp[0][0][first] = dp[0][0][first - 1]

    # 첫 행은 이미 연결, 첫 열은 파이프 잇기 불가
    for x in range(1, N):
        for y in range(1, N):
            # 대각선 파이프 잇기(해당 칸, 위 칸, 왼쪽 칸이 벽이 아니어야 함)
            if house[x][y] == 0 and house[x - 1][y] == 0 and house[x][y - 1] == 0:
                dp[2][x][y] = dp[0][x - 1][y - 1] + dp[1][x - 1][y - 1] + dp[2][x - 1][y - 1]

            # 가로, 세로 파이프 잇기
            if house[x][y] == 0:
                # 가로 파이프
                dp[0][x][y] = dp[0][x][y - 1] + dp[2][x][y - 1]
                # 세로 파이프
                dp[1][x][y] = dp[1][x - 1][y] + dp[2][x - 1][y]

    # 목적지에 연결된 총 파이프 출력
    answer = 0
    for i in range(3):
        answer += dp[i][N - 1][N - 1]
    return answer


N = int(input())
house = list(list(map(int, input().split())) for _ in range(N))

print(dynamic_programming(house))