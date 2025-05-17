import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 미로 탐색 (2178)
1. bfs
"""
from collections import deque


def bfs(maze):
    visited = [[0] * M for _ in range(N)]
    # 누적 거리와 출발점
    q = deque([(1, 0, 0)])
    visited[0][0] = 1

    while q:
        distance, x, y = q.popleft()

        # 이동 가능한 곳 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and not visited[nx][ny]:
                # 도착점 도달 시 종료
                if nx == N - 1 and ny == M - 1:
                    return distance + 1
                # 방문 처리
                visited[nx][ny] = 1
                q.append((distance + 1, nx, ny))


# 미로 정보
N, M = map(int, input().split())
maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]

print(bfs(maze))