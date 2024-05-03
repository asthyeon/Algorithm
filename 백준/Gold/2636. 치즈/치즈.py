import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 치즈 (2636)
 1. 공기와 접촉된 칸은 한 시간이 지나면 없어짐
 2. 치즈로 감싸져 있는 구멍은 공기가 없음
[입력]
 1. 세로와 가로의 길이
 2. 치즈 판 정보(치즈가 없는 칸 0, 치즈가 있는 칸 1)
[출력]
 1. 치즈가 모두 녹아서 없어지는 데 걸리는 시간
 2. 남아있는 치즈조각 칸의 개수
"""

"""
<풀이>
 1. bfs
 2. 치즈가 한 번에 다 녹는 경우의 수도 고려 -> 남은 치즈 수 먼저 세기
"""
from collections import deque


def bfs(arr):
    # 복사본, 방문기록
    arr_copy = [a[:] for a in arr]
    visited = [[0] * C for _ in range(R)]
    # 큐 생성 및 시작점 방문기록
    q = deque([(0, 0)])
    visited[0][0] = 1
    # 변화 플래그
    flag = False

    while q:
        x, y = q.popleft()

        # 델타 탐색
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            # 벽 형성 및 방문하지 않았을 때
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                # 방문 기록
                visited[nx][ny] = 1
                # 치즈라면 녹이고 변화 감지
                if arr[nx][ny]:
                    arr_copy[nx][ny] = 0
                    flag = True
                # 공기라면 인큐
                else:
                    q.append((nx, ny))

    # 치즈판 변화본 반환
    return flag, arr_copy


# 세로 R, 가로 C
R, C = map(int, input().split())
# 치즈판
arr = [list(map(int, input().split())) for _ in range(R)]

# 걸리는 시간, 남아있는 치즈 조각
hour = 0
cheese = 0

while True:
    # 치즈 수 세기
    now_cheese = 0
    for x in range(R):
        for y in range(C):
            if arr[x][y]:
                now_cheese += 1

    # 처음에 치즈가 없는 경우
    if hour == 0:
        if now_cheese == 0:
            print(hour)
            print(cheese)
            break

    # 치즈가 다 녹은 경우
    if now_cheese == 0:
        print(hour)
        print(cheese)
        break

    # 시간 증가 및 치즈 교체
    hour += 1
    cheese = now_cheese

    # 치즈 녹이기
    flag, arr = bfs(arr)