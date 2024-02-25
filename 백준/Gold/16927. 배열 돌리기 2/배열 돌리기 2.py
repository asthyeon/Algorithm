import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 배열 돌리기 2
 1. 크기가 N x M인 배열이 있을 때 반시계 방향으로 돌리기
 2. 배열과 정수 R이 주어졌을 때 배열을 R번 회전시킨 결과 구하기
[입력]
 1. N, M: 배열의 크기, R: 회전 수
 2. N개의 줄: 배열 정보
[출력]
 1. 주어진 배열을 R번 회전시킨 결과 출력
"""

"""
<풀이>
 1. 구현!
 2. 테두리 하나씩 회전시키기 -> 시간초과
 3. 회전이 한 바퀴를 도는 경우 원상태라는 점 고려
"""


# 회전
def turn(start_N, end_N, start_M, end_M, length):
    global arr
    # 범위보다 작아지면 종료
    if end_N - start_N <= 1 or end_M - start_M <= 1:
        return

    # 회전 횟수: R을 테두리 길이만큼 나눈 나머지
    for _ in range(R % length):
        # 배열 복사
        arr_copy = [a[:] for a in arr[:]]

        for n in range(start_N, end_N):
            # 첫 행
            if n == start_N:
                for m in range(start_M, end_M):
                    # 마지막 열
                    if m == end_M - 1:
                        arr_copy[n][m] = arr[n + 1][m]
                    # 그 외 열
                    else:
                        arr_copy[n][m] = arr[n][m + 1]
            # 마지막 행
            elif n == end_N - 1:
                for m in range(start_M, end_M):
                    # 첫 열
                    if m == start_M:
                        arr_copy[n][m] = arr[n - 1][m]
                    # 그 외 열
                    else:
                        arr_copy[n][m] = arr[n][m - 1]
            # 그외 행
            else:
                arr_copy[n][start_M] = arr[n - 1][start_M]
                arr_copy[n][end_M - 1] = arr[n + 1][end_M - 1]

        # 배열 교체
        arr = arr_copy

    # 다음 안쪽 바꾸기
    turn(start_N + 1, end_N - 1, start_M + 1, end_M - 1, length - 8)


# 세로 N, 가로 M, 회전 수 R
N, M, R = map(int, input().split())
# 배열 정보
arr = [list(map(int, input().split())) for _ in range(N)]

# 가장 바깥쪽 테두리 길이 구하기
length = (N - 1) * 2 + (M - 1) * 2
# 회전
turn(0, N, 0, M, length)

# 정답 출력
for i in range(N):
    print(*arr[i])