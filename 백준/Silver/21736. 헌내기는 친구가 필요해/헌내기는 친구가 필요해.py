import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 헌내기는 친구가 필요해 (21736)
 1. 캠퍼스 이동 법은 상하좌우
 2. 캠퍼스에서 만날 수 있는 사람의 수
[입력]
 1. N, M: 캠퍼스 크기
 2. N개의 줄: 'O': 빈 공간, 'X': 벽, 'I': 도연이, 'P': 사람
[출력]
 1. 도연이가 만날 수 있는 사람 수 출력
 2. 아무도 만나지 못한 경우 'TT' 출력
"""

"""
<풀이>
 1. bfs
"""
from collections import deque


# bfs
def bfs(campus, sx, sy):
    # 방문 리스트 및 큐
    visited = [[0] * M for _ in range(N)]
    q = deque([(sx, sy)])
    visited[sx][sy] = 1
    # 만난 사람 수
    cnt = 0

    while q:
        x, y = q.popleft()

        # 델타 탐색
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            # 벽형성 및 방문하지 않았을 때
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 빈 공간
                if campus[nx][ny] == 'O':
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                # 사람 만났을 때
                elif campus[nx][ny] == 'P':
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1

    # 사람을 못만날 때
    if cnt == 0:
        return 'TT'
    # 사람을 만날 때
    else:
        return cnt


N, M = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(N)]

for x in range(N):
    for y in range(M):
        if campus[x][y] == 'I':
            print(bfs(campus, x, y))
            exit()
