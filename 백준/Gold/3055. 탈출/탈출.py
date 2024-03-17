import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 탈출(3055)
 1. 티떱숲의 지도는 R행 C열
  - '.': 비어 있는 곳
  - '*': 물이 차 있는 지역
  - 'X': 돌
  - 'D': 비버 굴
  - 'S': 고슴도치 위치
 2. 매 분마다 고슴도치는 동서남북 이동, 물도 비어있는 칸으로 확장
 3. 물과 고슴도치는 돌 통과 X
 4. 고슴도치는 물 이동 X, 물도 비버 굴 이동 X
 5. 고슴도치는 다음 시간에 물이 찰 예정인 칸으로 이동 X
[입력]
 1. R, C: 티떱숲 크기
 2. R개의 줄: 티떱숲의 지도
[출력]
 1. 고슴도치가 비버 굴로 이동할 수 있는 가장 빠른 시간 출력
 2. 비버 굴로 이동 불가능시 'KAKTUS' 출력
"""

"""
<풀이>
 1. bfs
"""
from collections import deque


# bfs
def bfs(forest):
    # 물 위치
    water = deque([])
    # 고슴도치 위치와 방문 리스트
    hedgehog = deque([])
    visited = [[0] * C for _ in range(R)]

    # 물과 고슴도치 위치 인큐
    for x in range(R):
        for y in range(C):
            # 물이라면 물에 시간과 위치 인큐
            if forest[x][y] == '*':
                water.append((0, x, y))
            # 고슴도치라면 고슴도치에 시간과 위치 인큐 및 방문 기록
            elif forest[x][y] == 'S':
                hedgehog.append((0, x, y))
                visited[x][y] = 1

    while hedgehog:
        # 새로운 물
        new_water = deque([])
        # 물 범람
        while water:
            # 물 시간 및 현재 위치
            w_time, w_x, w_y = water.popleft()
            # 물 범람
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                w_nx, w_ny = w_x + dx, w_y + dy
                # 벽 생성
                if 0 <= w_nx < R and 0 <= w_ny < C:
                    # 범람이 가능하다면 범람
                    if forest[w_nx][w_ny] == '.' or forest[w_nx][w_ny] == 'S':
                        new_water.append((w_time + 1, w_nx, w_ny))
                        forest[w_nx][w_ny] = '*'
        # 물 교체
        water = new_water

        # 새로운 고슴도치 이동
        new_hedgehog = deque([])
        while hedgehog:
            # 고슴도치 시간 및 현재 위치
            h_time, h_x, h_y = hedgehog.popleft()
            # 고슴도치 이동
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                h_nx, h_ny = h_x + dx, h_y + dy
                # 벽 생성
                if 0 <= h_nx < R and 0 <= h_ny < C:
                    # 비버 굴이라면 종료
                    if forest[h_nx][h_ny] == 'D':
                        return h_time + 1
                    # 이동이 가능하다면 이동
                    elif forest[h_nx][h_ny] == '.' and not visited[h_nx][h_ny]:
                        new_hedgehog.append((h_time + 1, h_nx, h_ny))
                        visited[h_nx][h_ny] = 1
        # 고슴도치 교체
        hedgehog = new_hedgehog

    # 이동 불가능시
    return 'KAKTUS'


# 세로 R, 가로 C
R, C = map(int, input().split())
# 티떱숲 지도
forest = [list(input().rstrip()) for _ in range(R)]

print(bfs(forest))