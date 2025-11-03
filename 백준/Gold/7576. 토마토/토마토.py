import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
<문제>
# 토마토 (7576)
1. 창고에 보관된 토마토들이 최소 며칠이 지나면 다 익게 되는 지?
 - 익은 토마토는 하루 후에 상하좌우 토마토를 익게 함 
 - 1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토가 없는 칸
 - 저장될 때부터 모든 토마토가 익어 있는 상태: 0 출력, 모두 익지 못하는 상황: -1 출력
<풀이>
1. bfs -> 익은 토마토 위치를 먼저 찾기
2. 토마토가 없는 칸이 있는 경우, 이 칸을 제외한 나머지 토마토는 모두 익을 수 있음
"""
from collections import deque


def bfs(box):
    q = deque()

    # 익은 토마토 위치 찾기
    for sx in range(N):
        for sy in range(M):
            if box[sx][sy] == 1:
                q.append((sx, sy))

    while q:
        x, y = q.popleft()

        # 델타탐색
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if box[nx][ny] == 0 and box[nx][ny] != -1:
                    box[nx][ny] = box[x][y] + 1
                    q.append((nx, ny))

    # 토마토 검사
    answer = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1
            answer = max(answer, box[i][j])

    return answer - 1


# M: 가로 크기, N: 세로 크기
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

print(bfs(box))