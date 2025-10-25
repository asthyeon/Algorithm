import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
<문제>
# 유기농 배추 (1012)
1. 배추에 지렁이가 있으면 해충 보호
2. 한 배추에 지렁이가 한 마리 있으면 인접한 다른 배추로 이동 가능
 - 상하좌우 네 방향
3. 모든 배추가 보호될 수 있는 최소 지렁이 수?
<풀이>
1. bfs
"""
from collections import deque


def bfs(field, location):
    answer = 0
    visited = [[0] * M for _ in range(N)]

    # 모든 좌표 순회
    while location:
        sx, sy = location.popleft()

        # 방문하지 않은 밭이라면, 지렁이 + 1 및 bfs 탐색
        if not visited[sy][sx]:
            visited[sy][sx] = 1
            q = deque([(sy, sx)])
            answer += 1

            while q:
                x, y = q.popleft()
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    # 배추밭 영역 안에서
                    if 0 <= nx < N and 0 <= ny < M:
                        # 방문하지 않은 배추라면 방문 처리 및 인큐
                        if field[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            q.append((nx, ny))

    return answer


T = int(input())
for tc in range(1, T + 1):
    # 배추밭 가로 M, 세로 N, 배추 수 K
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in range(N)]
    # 배추 좌표 입력
    location = deque(tuple(map(int, input().split())) for _ in range(K))
    for X, Y in location:
        field[Y][X] = 1

    # 정답 출력
    print(bfs(field, location))

