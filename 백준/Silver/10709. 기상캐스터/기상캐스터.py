import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs(city):
    answer = [[-1] * W for _ in range(H)]
    q = deque()

    for x in range(H):
        for y in range(W):
            if city[x][y] == 'c':
                q.append((x, y))
                answer[x][y] = 0

    while q:
        sx, sy = q.popleft()

        for dy in range(1, W - sy):
            ny = sy + dy
            if 0 <= ny < W and answer[sx][ny]:
                answer[sx][ny] = dy
            elif answer[sx][ny] == 0:
                break

    for i in range(H):
        print(*answer[i])



H, W = map(int, input().split())
city = [list(input().rstrip()) for _ in range(H)]

bfs(city)