import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 농장 관리 (1245)
 1. 산봉우리는 같은 높이를 가지는 하나의 격자 혹은 인접한 격자들의 집합
  - 인접한: X좌표 차이와 Y좌표 차이 모두 1 이하일 경우
 2. 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작아야 함
[입력]
 1. N, M: 산 크기
 2. N개의 줄: M: 격자의 높이
[출력]
 1. 산봉우리의 개수 출력
"""

"""
<풀이>
 1. bfs 및 델타 탐색
"""
from collections import deque

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]


# bfs
def bfs(q):
    # 산봉우리 확인
    peak = 1
    while q:
        sx, sy = q.popleft()
        visited[sx][sy] = 1

        # 델타 탐색(8방향)
        for d in range(8):
            nx, ny = sx + dx[d], sy + dy[d]
            # 벽 형성
            if 0 <= nx < N and 0 <= ny < M:
                # 현재 위치가 산봉우리가 아니라면 peak = 0
                if mountain[sx][sy] < mountain[nx][ny]:
                    peak = 0
                # 현재 위치와 같은 높이고, 미방문한 곳이라면 방문
                elif mountain[sx][sy] == mountain[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))

    # 산봉우리인 경우 + 1
    return peak


N, M = map(int, input().split())
mountain = [list(map(int, input().split())) for _ in range(N)]
# 방문 리스트
visited = [[0] * M for _ in range(N)]
# 산봉우리 수
answer = 0

for x in range(N):
    for y in range(M):
        # 방문하지 않은 곳이라면 bfs
        if not visited[x][y]:
            q = deque([(x, y)])
            answer += bfs(q)
            
print(answer)


