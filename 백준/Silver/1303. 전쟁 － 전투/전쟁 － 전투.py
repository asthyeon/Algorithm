import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(battleground):
    cnt = 1
    q = [(sx, sy)]
    visited[sx][sy] = 1
    while q:
        x, y = q.pop()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                if battleground[x][y] == battleground[nx][ny]:
                    cnt += 1
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    return cnt ** 2


N, M = map(int, input().split())
battleground = [list(input().rstrip()) for _ in range(M)]

W_power = B_power = 0
visited = [[0] * N for _ in range(M)]
for sx in range(M):
    for sy in range(N):
        if not visited[sx][sy]:
            if battleground[sx][sy] == 'W':
                W_power += bfs(battleground)
            else:
                B_power += bfs(battleground)

print(W_power, B_power)