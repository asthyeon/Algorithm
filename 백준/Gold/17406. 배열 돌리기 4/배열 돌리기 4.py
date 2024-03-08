import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 배열 돌리기 4(17406)
 1. N x M 배열의 A의 값은 각 행의 모든 수의 합 중 최솟값
 2. 회전 연산 
  - (r, c, s)
  - 가장 왼쪽 윗 칸: (r - s, c - s)
  - 가장 오른쪽 아랜 캇: (r + s, c + s)
  - 시계 방향으로 한 칸씩 돌린다는 것
 3. 연산 순서는 상관 없음
[입력]
 1. N, M: 배열 A 크기, K: 회전 연산의 개수
 2. ~ N개의 줄: 배열 A
 3. ~ K개의 줄: 회전 연산의 정보 (r, c, s)
[출력]
 1. 배열 A의 최솟값 출력
"""

"""
<풀이>
 1. 돌리자
 2. 연산 순서에 따라 최솟값이 바뀌므로 모든 경우 고려하기
"""
from copy import deepcopy
from itertools import permutations


# 돌리기
def turn(A_copy, A_copy_copy, r, c, s):
    # 더이상 회전을 못하는 경우 종료
    if s == 0:
        return

    # 테두리 돌리기
    for x in range(r - s - 1, r + s):
        # 첫 행
        if x == r - s - 1:
            for y in range(c - s - 1, c + s):
                # 첫 열
                if y == c - s - 1:
                    A_copy_copy[x][y] = A_copy[x + 1][y]
                # 그 외 열
                else:
                    A_copy_copy[x][y] = A_copy[x][y - 1]
        # 마지막 행
        elif x == r + s - 1:
            for y in range(c - s - 1, c + s):
                # 마지막 열
                if y == c + s - 1:
                    A_copy_copy[x][y] = A_copy[x - 1][y]
                # 그 외 열
                else:
                    A_copy_copy[x][y] = A_copy[x][y + 1]
        # 그 외 행
        else:
            # 첫 행
            A_copy_copy[x][c - s - 1] = A_copy[x + 1][c - s - 1]
            # 마지막 행
            A_copy_copy[x][c + s - 1] = A_copy[x - 1][c + s - 1]

    # 내부 회전
    turn(A_copy, A_copy_copy, r, c, s - 1)


# 최솟값 구하기
def min_value(A_copy):
    answer = 10e9
    for x in range(N):
        answer = min(answer, sum(A_copy[x]))

    return answer


# 세로 N, 가로 M, 회전 수 K
N, M, K = map(int, input().split())
# 배열 A
A = [list(map(int, input().split())) for _ in range(N)]
# 회전하는 경우의 수 받기
cases = []
for _ in range(K):
    # 행 r, 열 c, 변화량 s
    r, c, s = map(int, input().split())
    cases.append((r, c, s))

# 회전 순서 경우의 수
answer = 10e9
for case in list(permutations(cases)):
    # 이번 경우에 사용할 A 복사
    A_copy = deepcopy(A)
    # 이번 경우의 회전
    for r, c, s in case:
        # 이번 회전에 사용할 A_copy 복사
        A_copy_copy = deepcopy(A_copy)
        # 회전
        turn(A_copy, A_copy_copy, r, c, s)
        # 교체
        A_copy = A_copy_copy

    # 최솟값 계산
    answer = min(answer, min_value(A_copy))

print(answer)
