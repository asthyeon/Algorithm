import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 현수막 (14716)
 1. 글자인 부분은 1, 글자가 아닌 부분은 0
 2. 글자인 부분 1이 상, 하, 좌, 우, 대각선으로 인접하여 서로 연결 = 한 개의 글자
[입력]
 1. M, N: 현수막의 크기
 2. M개의 줄: 현수막의 정보
[출력]
 1. 현수막에서 글자의 개수가 몇 개인지 출력
"""

"""
<풀이>
 1. bfs
"""
from collections import deque

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, -1, 1]


# bfs
def bfs(banner):
    visited = [[0] * N for _ in range(M)]
    q = deque([])

    # 문자 수
    cnt = 0

    for x in range(M):
        for y in range(N):
            # 글자의 부분이고, 방문하지 않았다면
            if banner[x][y] == 1 and not visited[x][y]:
                visited[x][y] = 1
                q.append((x, y))
                cnt += 1
                while q:
                    sx, sy = q.popleft()

                    # 델타 탐색 (대각선 포함)
                    for i in range(8):
                        nx, ny = sx + dx[i], sy + dy[i]

                        # 벽 형성
                        if 0 <= nx < M and 0 <= ny < N:
                            # 글자이고 방문하지 않았다면 방문
                            if banner[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = 1
                                q.append((nx, ny))

    return cnt


M, N = map(int, input().split())

banner = [list(map(int, input().split())) for _ in range(M)]

print(bfs(banner))