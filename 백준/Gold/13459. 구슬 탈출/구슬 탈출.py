import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 구슬 탈출 (13459)
 1. 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음,
 2. 빨간 구슬을 구멍을 통해 빼내는 게임
 3. 파란 구슬이 구멍에 들어가면 안됨
 4. 중력을 이용해서 이리 저리 굴려야 함
  - 상하좌우 기울이기 네 동작 가능
  - 기울이기 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때까지
 5. 구슬은 동시에 같은 칸에 있을 수 없음
[입력]
 1. N, M: 보드의 세로, 가로 크기
 2. N개의 줄: 보드 모양
  - '.': 빈 칸
  - '#': 공이 이동할 수 없는 장애물 또는 벽
  - 'O': 구멍의 위치
  - 'R': 빨간 구슬의 위치
  - 'B': 파란 구슬의 위치
[출력]
 1. 빨간 구슬을 10번 이하로 움직여서 빼낼 수 있으면 1, 없으면 0 출력
"""

"""
<풀이>
 1. 일단 풀어보기
"""
from pprint import pprint
# 왼, 오, 위, 아래
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 기울이기
def tilt(board, direction, orx, ory, rx, ry, obx, oby, bx, by, cnt):
    # 이동 횟수 초과시 종료
    if cnt > 10:
        return

    # 빨간 구슬 이동
    red_move = 0
    while True:
        nrx = rx + dx[direction]
        nry = ry + dy[direction]
        red_move += 1

        # 벽 내부일 때
        if 0 <= nrx < N and 0 <= nry < M:
            # 벽이 아닐 때 이동
            if board[nrx][nry] != '#':
                rx += dx[direction]
                ry += dy[direction]

                # 구멍일 때 멈추기
                if board[rx][ry] == 'O':
                    break
            else:
                break
        else:
            break

    # 파란 구슬 이동
    blue_move = 0
    while True:
        nbx = bx + dx[direction]
        nby = by + dy[direction]
        blue_move += 1

        if 0 <= nbx < N and 0 <= nby < M:
            # 벽이 아닐 때 이동
            if board[nbx][nby] != '#':
                bx += dx[direction]
                by += dy[direction]

                # 구멍일 때 멈추기
                if board[bx][by] == 'O':
                    break
            else:
                break
        else:
            break

    # 파란 구슬이 구멍에 도착했다면 종료
    if board[bx][by] == 'O':
        return

    # 빨간 구슬이 구멍에 도착했다면 1 출력
    if board[rx][ry] == 'O':
        print(1)
        exit()

    # 구슬의 위치가 같다면
    if rx == bx and ry == by:
        # 더 많이 이동한 구슬을 한 칸 이전으로 옮기기
        if red_move > blue_move:
            rx -= dx[direction]
            ry -= dy[direction]
        else:
            bx -= dx[direction]
            by -= dy[direction]

    # 보드 복사 및 구슬 자리 교체
    board_copy = [b[:] for b in board[:]]
    board_copy[orx][ory] = '.'
    board_copy[obx][oby] = '.'
    board_copy[rx][ry] = 'R'
    board_copy[bx][by] = 'B'

    # 각 방향 재귀
    tilt(board, 0, rx, ry, rx, ry, bx, by, bx, by, cnt + 1)
    tilt(board, 1, rx, ry, rx, ry, bx, by, bx, by, cnt + 1)
    tilt(board, 2, rx, ry, rx, ry, bx, by, bx, by, cnt + 1)
    tilt(board, 3, rx, ry, rx, ry, bx, by, bx, by, cnt + 1)


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

# 빨간 구슬 및 파란 구슬 위치 찾기
for x in range(N):
    for y in range(M):
        if board[x][y] == 'R':
            rx, ry = x, y
        elif board[x][y] == 'B':
            bx, by = x, y

# 각 방향에 대해 탐색
tilt(board, 0, rx, ry, rx, ry, bx, by, bx, by, 1)
tilt(board, 1, rx, ry, rx, ry, bx, by, bx, by, 1)
tilt(board, 2, rx, ry, rx, ry, bx, by, bx, by, 1)
tilt(board, 3, rx, ry, rx, ry, bx, by, bx, by, 1)

# 10번 안에 불가능 하다면 0 출력
print(0)








