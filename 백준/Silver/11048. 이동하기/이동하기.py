import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 이동하기 (11048)
 1. (1, 1) -> (N, M)으로 이동할 때 사탕을 가져올 수 있음
 2. 준규는 오른쪽, 아래, 오른쪽 아래로만 이동 가능
[입력]
 1. N, M: 미로의 크기
 2. N개의 줄: 미로 정보, 숫자는 사탕의 개수
[출력]
 1. 준규가 (N, M)으로 이동할 때 가져올 수 있는 사탕 개수를 출력
"""

"""
<풀이>
 1. bfs -> 메모리 초과
 2. q가 아닌 dp로 해결
"""


# dp
def dynamic_programming(maze):
    dp = [[0] * M for _ in range(N)]

    # 각 자리 순회
    for x in range(N):
        for y in range(M):
            if x == 0 and y == 0:
                dp[x][y] = maze[x][y]
            elif x == 0:
                dp[x][y] = dp[x][y - 1] + maze[x][y]
            elif y == 0:
                dp[x][y] = dp[x - 1][y] + maze[x][y]
            else:
                dp[x][y] = max(dp[x][y - 1], dp[x - 1][y], dp[x - 1][y - 1]) + maze[x][y]

    return dp[N - 1][M - 1]


N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

print(dynamic_programming(maze))