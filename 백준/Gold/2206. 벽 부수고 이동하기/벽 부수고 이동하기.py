import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 벽 부수고 이동하기 (2206)
1. 0: 이동 가능, 1: 벽
2. (1, 1) -> (N, M) 최단 경로로 이동하기 (1개까지 벽 부수기 가능)

[풀이]
1. bfs
2. 벽을 부순 세계선이 존재한다 -> 배열을 2개로 돌리기
3. 벽을 부섰는지에 대한 변수 필요
4. 벽을 부섰을 때랑 안부섰을 때의 거리를 지정해줘야 함
"""
from collections import deque


def bfs(arr):
    # 원래 세계와 벽을 부순 세계선
    original = [[0] * M for _ in range(N)]
    another = [[0] * M for _ in range(N)]
    # x, y, 벽 부수기 여부
    q = deque([(0, 0, False)])
    original[0][0] = 1
    another[0][0] = 1

    while q:
        x, y, destroyed = q.popleft()

        # 벽을 안부섰을 때와 부섰을 때의 거리
        if not destroyed:
            now = original[x][y]
        else:
            now = another[x][y]

        # 도착했다면 최단 거리 반환
        if x == N - 1 and y == M - 1:
            return now

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                # 이동 가능하다면
                if arr[nx][ny] == 0:
                    # 벽을 부수지 않았다면 원본 방문
                    if not destroyed and original[nx][ny] == 0:
                        original[nx][ny] = now + 1
                        q.append((nx, ny, destroyed))
                    # 벽을 부순 상태라면 다른 세계선 방문
                    elif destroyed and another[nx][ny] == 0:
                        another[nx][ny] = now + 1
                        q.append((nx, ny, destroyed))

                # 벽이라면 벽 부수기
                else:
                    if not destroyed and another[nx][ny] == 0:
                        another[nx][ny] = now + 1
                        q.append((nx, ny, True))

    # 도달하지 못한 경우
    return -1


N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs(arr))