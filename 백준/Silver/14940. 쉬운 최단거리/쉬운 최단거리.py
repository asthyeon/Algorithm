import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def bfs(arr, sx, sy):
    visited = [[-2] * m for _ in range(n)]
    q = deque([(sx, sy)])
    visited[sx][sy] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -2:
                if arr[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    for x in range(n):
        for y in range(m):
            if visited[x][y] == -2:
                if arr[x][y] == 0:
                    visited[x][y] = 0
                else:
                    visited[x][y] = -1

    for k in range(n):
        print(*visited[k])


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            bfs(arr, i, j)