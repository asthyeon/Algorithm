import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 배열 돌리기
1. 크기가 N x M인 배열을 반시계 방향으로 돌리기
* 입력
- 첫째 줄: 배열의 크기 N, M, 수행해야 하는 회전의 수 R
- 둘째 ~ N개의 줄: 배열 정보
[출력: 배열을 R번 회전시킨 결과 출력]
"""

"""
@ 풀이
(1) 일단 풀어보기 -> 구현
(2) 한 테두리씩 바꿔나가기
"""


# 회전 함수
def turn(arr_copy, start, N, M):
    # 종료(2칸보다 작아지면 종료)
    if M - start < 2 or N - start < 2:
        return
    # 회전하기
    for n in range(start, N):
        # 첫째 줄 회전
        if n == start:
            for m in range(start, M):
                if m == M - 1:
                    arr_copy[n][m] = arr[n + 1][m]
                else:
                    arr_copy[n][m] = arr[n][m + 1]
        # 마지막 줄 회전
        elif n == N - 1:
            for m in range(start, M):
                if m == start:
                    arr_copy[n][m] = arr[n - 1][m]
                else:
                    arr_copy[n][m] = arr[n][m - 1]
        # 그 외 회전
        else:
            for m in range(2):
                arr_copy[n][start] = arr[n - 1][start]
                arr_copy[n][M - 1] = arr[n + 1][M - 1]
    # for i in range(N):
    #     print(*arr_copy[i])
    # 재귀
    turn(arr_copy, start + 1, N - 1, M - 1)


# 배열의 크기 N, M 회전 수 R
N, M, R = map(int, input().split())
# 배열 정보
arr = [list(map(int, input().split())) for _ in range(N)]
# 회전
for _ in range(R):
    # 배열 복사
    arr_copy = [a[:] for a in arr]
    # 회전(start와 N, M으로 테두리를 하나씩 좁히기)
    turn(arr_copy, 0, N, M)
    # 원본 교체
    arr = arr_copy

for i in range(N):
    print(*arr[i])


