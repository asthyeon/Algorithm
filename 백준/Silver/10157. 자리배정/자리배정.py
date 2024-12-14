import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 자리배정 (10157)
 1. 왼쪽아래 시작 -> 가운데로 회전하며 배정
[입력]
 1. C: 가로, R: 세로
 2. K: 관객의 대기번호
[출력]
 1. 관객 K에게 배정될 좌석 번호 (x, y)를 출력 (좌석 배정 불가능할 경우 0 출력)
"""

"""
<풀이>
 1. dfs
"""


def dfs():
    seats = [[0] * C for _ in range(R)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    x = R - 1
    y = 0
    direction = 0
    number = 1

    while True:
        seats[x][y] = number
        
        # 관객 K 좌석 번호 출력
        if number == K:
            return y + 1, R - x
        
        # dfs
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < R and 0 <= ny < C and not seats[nx][ny]:
            x, y = nx, ny
            number += 1
        else:
            direction += 1
            if direction == 4:
                direction = 0


C, R = map(int, input().split())
K = int(input())

# 배정이 불가능한 경우
if K > C * R:
    print(0)
# 배정이 가능한 경우
else:
    print(*dfs())