import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 마법사 상어와 토네이도 (20057)
 1. 토네이도 이동 경로: 가운데부터 반시계 방향으로 (1, 1)으로 이동
 2. 토네이도 한 칸 이동시 이동하려는 칸의 모래가 비율과 a가 적혀 있는 칸으로 이동함
 3. a로 이동하는 모래 양은 비율 칸 선 이동후 남은 모래의 양
 4. 소수점 아래는 버릴 것
 5. 모래는 격자 밖으로 이동할 수 있음
 6. 비율 칸 정보
  [  %   %  2%   %   %]
  [  % 10%  7%  1%   %]
  [ 5%   a   y ← x   %]
  [  % 10%  7%  1%   %]
  [  %   %  2%   %   %]
  * 다른 방향으로 이동하는 경우 해당 방향으로 회전하면 됨
 
[입력]
 1. N: 격자의 크기
 2. N개의 줄: 격자 정보
[출력]
 1. 격자 밖으로 나간 모래의 양 출력
"""

"""
<풀이>
 1. 구현
 2. 토네이도 이동 거리: 2번 방향 전환 후 + 1
"""
import math
# 토네이도
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

# 토네이도 좌우
lx = (1, 0, -1, 0)
ly = (0, 1, 0, -1)
rx = (-1, 0, 1, 0)
ry = (0, -1, 0, 1)


# 모래 흩날리기
def sand(arr, x, y, nx, ny, order):
    # 현재 남은 모래 양
    rest = arr[nx][ny]
    # 격자 밖으로 이동되는 모래
    out = 0
    # 남은 모래가 날아갈 위치
    ax, ay = nx + dx[order], ny + dy[order]

    # 1% 모래 이동
    one_lx, one_ly = x + lx[order], y + ly[order]
    one_rx, one_ry = x + rx[order], y + ry[order]
    if 0 <= one_lx < N and 0 <= one_ly < N:
        arr[one_lx][one_ly] += math.floor(arr[nx][ny] * 0.01)
    else:
        out += math.floor(arr[nx][ny] * 0.01)
    rest -= math.floor(arr[nx][ny] * 0.01)
    if 0 <= one_rx < N and 0 <= one_ry < N:
        arr[one_rx][one_ry] += math.floor(arr[nx][ny] * 0.01)
    else:
        out += math.floor(arr[nx][ny] * 0.01)
    rest -= math.floor(arr[nx][ny] * 0.01)

    # 2% 모래 이동
    two_lx, two_ly = nx + lx[order] * 2, ny + ly[order] * 2
    two_rx, two_ry = nx + rx[order] * 2, ny + ry[order] * 2
    if 0 <= two_lx < N and 0 <= two_ly < N:
        arr[two_lx][two_ly] += math.floor(arr[nx][ny] * 0.02)
    else:
        out += math.floor(arr[nx][ny] * 0.02)
    rest -= math.floor(arr[nx][ny] * 0.02)
    if 0 <= two_rx < N and 0 <= two_ry < N:
        arr[two_rx][two_ry] += math.floor(arr[nx][ny] * 0.02)
    else:
        out += math.floor(arr[nx][ny] * 0.02)
    rest -= math.floor(arr[nx][ny] * 0.02)

    # 5% 모래 이동
    five_x, five_y = ax + dx[order], ay + dy[order]
    if 0 <= five_x < N and 0 <= five_y < N:
        arr[five_x][five_y] += math.floor(arr[nx][ny] * 0.05)
    else:
        out += math.floor(arr[nx][ny] * 0.05)
    rest -= math.floor(arr[nx][ny] * 0.05)

    # 7% 이동
    seven_lx, seven_ly = nx + lx[order], ny + ly[order]
    seven_rx, seven_ry = nx + rx[order], ny + ry[order]
    if 0 <= seven_lx < N and 0 <= seven_ly < N:
        arr[seven_lx][seven_ly] += math.floor(arr[nx][ny] * 0.07)
    else:
        out += math.floor(arr[nx][ny] * 0.07)
    rest -= math.floor(arr[nx][ny] * 0.07)
    if 0 <= seven_rx < N and 0 <= seven_ry < N:
        arr[seven_rx][seven_ry] += math.floor(arr[nx][ny] * 0.07)
    else:
        out += math.floor(arr[nx][ny] * 0.07)
    rest -= math.floor(arr[nx][ny] * 0.07)

    # 10% 이동
    ten_lx, ten_ly = ax + lx[order], ay + ly[order]
    ten_rx, ten_ry = ax + rx[order], ay + ry[order]
    if 0 <= ten_lx < N and 0 <= ten_ly < N:
        arr[ten_lx][ten_ly] += math.floor(arr[nx][ny] * 0.1)
    else:
        out += math.floor(arr[nx][ny] * 0.1)
    rest -= math.floor(arr[nx][ny] * 0.1)
    if 0 <= ten_rx < N and 0 <= ten_ry < N:
        arr[ten_rx][ten_ry] += math.floor(arr[nx][ny] * 0.1)
    else:
        out += math.floor(arr[nx][ny] * 0.1)
    rest -= math.floor(arr[nx][ny] * 0.1)

    # 남은 모래 이동
    if 0 <= ax < N and 0 <= ay < N:
        arr[ax][ay] += rest
    else:
        out += rest

    # 모래 초기화
    arr[nx][ny] = 0

    return arr, out


# 토네이도 회전
def tornado(arr):
    # 시작 위치
    x, y = N // 2, N // 2
    # 이동할 거리, 방향 전환 수, 전환 방향
    distance = 1
    turn = 0
    order = 0
    # 격자 밖으로 나간 모래 양
    total = 0

    while True:
        # 토네이도 이동
        for _ in range(distance):
            nx, ny = x + dx[order], y + dy[order]
            arr, out = sand(arr, x, y, nx, ny, order)
            total += out
            x, y = nx, ny

            if x == y == 0:
                return total

        # 방향 전환 수 계산 후 이동 거리 계산
        turn += 1
        if turn == 2:
            distance += 1
            turn = 0
        # 방향 전환
        order += 1
        if order == 4:
            order = 0


# 격자 크기
N = int(input())
# 격자 정보
arr = [list(map(int, input().split())) for _ in range(N)]

print(tornado(arr))