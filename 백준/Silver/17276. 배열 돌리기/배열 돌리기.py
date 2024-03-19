import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 배열 돌리기(17276)
 1. 크기가 n x n 인 2차원 정수 배열 X
 2. X를 45도의 배수만큼 시계 혹은 반시계로 돌리려고 함
 3. X를 시계방향으로 45도 돌릴 때의 연산
  - 주 대각선을 가운데 열로 옮긴다
  - 가운데 열을 부 대각선으로 옮긴다
  - 부 대각선을 가운데 행으로 옮긴다
  - 가운데 행을 주 대각선으로 옮긴다
 4. 네 가지 모두 원소의 기존 순서는 유지되어야 함
 5. X의 다른 원소의 위치는 변하지 않음
 6. 반시계로 45도 돌려도 같은 원리 적용
[입력]
 1. T: 테스트 수
 2. n: 배열의 크기, d: 각도(|d|는45의 배수)
 3. X 정보
"""

"""
<풀이>
 1. 구현
 2. 45도 회전
  - 0, 2, 4
  - 1, 2, 3
  - 0, 1, 2, 3, 4
  - 1, 2, 3
  - 0, 2, 4
"""
from copy import deepcopy


# 회전
def turn(X, d):
    # 360도의 경우 원상태
    if d == 360:
        for i in range(n):
            print(*X[i])
        return

    # 회전 수
    cnt = abs(d) // 45

    # 회전
    for _ in range(cnt):
        if d > 0:
            X = clockwise(X)
        else:
            X = counterclockwise(X)

    # 정답 출력
    for i in range(n):
        print(*X[i])


# 시계 방향 회전
def clockwise(X):
    new_X = deepcopy(X)

    start = 0
    end = n - 1
    for _ in range(n // 2):
        new_X[start][start] = X[n // 2][start]
        new_X[start][n // 2] = X[start][start]
        new_X[start][end] = X[start][n // 2]
        new_X[n // 2][end] = X[start][end]
        new_X[end][end] = X[n // 2][end]
        new_X[end][n // 2] = X[end][end]
        new_X[end][start] = X[end][n // 2]
        new_X[n // 2][start] = X[end][start]

        start += 1
        end -= 1

    return new_X


# 반시계 방향 회전
def counterclockwise(X):
    new_X = deepcopy(X)

    start = 0
    end = n - 1
    for _ in range(n // 2):
        new_X[start][start] = X[start][n // 2]
        new_X[start][n // 2] = X[start][end]
        new_X[start][end] = X[n // 2][end]
        new_X[n // 2][end] = X[end][end]
        new_X[end][end] = X[end][n // 2]
        new_X[end][n // 2] = X[end][start]
        new_X[end][start] = X[n // 2][start]
        new_X[n // 2][start] = X[start][start]

        start += 1
        end -= 1

    return new_X


T = int(input())
for tc in range(1, T + 1):
    # 맵의 크기 n, 각도 d
    n, d = map(int, input().split())
    # X의 정보
    X = [list(map(int, input().split())) for _ in range(n)]

    turn(X, d)




