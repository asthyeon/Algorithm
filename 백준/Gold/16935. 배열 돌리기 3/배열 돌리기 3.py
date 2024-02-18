import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 배열 돌리기 3(16935)
 1. N x M 배열에 연산 R번 적용하기
 2. 연산 종류
  1번: 상하 반전
  2번: 좌우 반전
  3번: 오른쪽 90도 회전
  4번: 왼쪽 90도 회전
  5번: 배열 4등분 후 시계방향 회전
  6번: 배열 4등분 후 반시계방향 회전
[입력]
 1. N, M: 배열 크기(둘 다 짝수) R: 연산 수
 2. N개의 줄: 배열 정보
 3. 수행해야 하는 연산
[출력]
 1. 배열에 R애ㅢ 연산을 순서대로 수행한 결과 출력
"""

"""
<풀이>
 1. 구현!
"""


# 1번 연산
def one(arr):
    # 새 배열 만들기
    new_arr = []
    # 상하 반전
    for i in range(N - 1, -1, -1):
        new_arr.append(arr[i])

    return new_arr


# 2번 연산
def two(arr):
    # 새 배열 만들기
    new_arr = [a[:] for a in arr]
    # 좌우 반전
    for i in range(N):
        for j in range(M):
            new_arr[i][j] = arr[i][M - j - 1]
            new_arr[i][M - j - 1] = arr[i][j]

    return new_arr


# 3번 연산
def three(arr):
    # 새 배열 만들기
    new_arr = []
    # 오른쪽 90도 회전
    for i in range(M):
        new_line = []
        for j in range(N - 1, -1, -1):
            new_line.append(arr[j][i])
        new_arr.append(new_line)

    return new_arr


# 4번 연산
def four(arr):
    # 새 배열 만들기
    new_arr = []
    for i in range(M - 1, -1, -1):
        new_line = []
        for j in range(N):
            new_line.append(arr[j][i])
        new_arr.append(new_line)

    return new_arr


# 5번 연산
def five(arr):
    # 새 배열 만들기
    new_arr = [a[:] for a in arr]
    # 4등분 후 시계방향 회전
    for i in range(N // 2):
        for j in range(M // 2):
            new_arr[i][j] = arr[i + N // 2][j]
            new_arr[i][j + M // 2] = arr[i][j]
            new_arr[i + N // 2][j + M // 2] = arr[i][j + M // 2]
            new_arr[i + N // 2][j] = arr[i + N // 2][j + M // 2]

    return new_arr


# 6번 연산
def six(arr):
    # 새 배열 만들기
    new_arr = [a[:] for a in arr]
    # 4등분 후 반시계방향 회전
    for i in range(N // 2):
        for j in range(M // 2):
            new_arr[i][j] = arr[i][j + M // 2]
            new_arr[i][j + M // 2] = arr[i + N // 2][j + M // 2]
            new_arr[i + N // 2][j + M // 2] = arr[i + N // 2][j]
            new_arr[i + N // 2][j] = arr[i][j]

    return new_arr


# 세로 N, 가로 M, 연산 수 R
N, M, R = map(int, input().split())
# 배열 정보
arr = [list(map(int, input().split())) for _ in range(N)]
# 연산 정보
calculations = list(map(int, input().split()))

# 연산
for calculation in calculations:

    # 각 연산 번호에 맞게 연산
    if calculation == 1:
        arr = one(arr)

    elif calculation == 2:
        arr = two(arr)

    elif calculation == 3:
        arr = three(arr)
        # 가로 세로 반전(다음 명령 수행하기 위함)
        N, M = M, N

    elif calculation == 4:
        arr = four(arr)
        # 가로 세로 반전(다음 명령 수행하기 위함)
        N, M = M, N

    elif calculation == 5:
        arr = five(arr)

    elif calculation == 6:
        arr = six(arr)

# 정답 출력
for a in arr:
    print(*a)
