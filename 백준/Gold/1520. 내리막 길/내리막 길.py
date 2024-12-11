import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 내리막 길 (1520)
 1. 제일 왼쪽 위 -> 제일 오른쪽 아래 이동
 2. 항상 높이가 더 낮은 지점으로만 이동 가능
[입력]
 1. M: 세로, N: 가로
 2. M개의 줄: 지도 정보
[출력]
 1. H: 이동 가능한 경로의 수
"""

"""
<풀이>
 1. dp + bfs
 2. 우선순위 큐 사용 -> 가장 높은 위치에서 내려오기
"""
import heapq


def dynamic_programming(navigation):
    dp = [[0] * N for _ in range(M)]
    # 가장 높은 값을 음수로 바꿔 먼저 계산하도록
    hq = [(-navigation[0][0], 0, 0)]
    dp[0][0] = -1

    # bfs
    while hq:
        now, x, y = heapq.heappop(hq)

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                # 다음 지역이 더 낮다면
                if navigation[x][y] > navigation[nx][ny]:
                    # 방문하지 않은 곳일 경우 인큐
                    if not dp[nx][ny]:
                        heapq.heappush(hq, (-navigation[nx][ny], nx, ny))
                    # 지나온 경로 값 더하기
                    dp[nx][ny] += dp[x][y]

    return -dp[M - 1][N - 1]


M, N = map(int, input().split())
navigation = [list(map(int, input().split())) for _ in range(M)]

print(dynamic_programming(navigation))