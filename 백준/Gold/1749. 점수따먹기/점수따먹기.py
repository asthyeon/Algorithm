import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 점수따먹기 (1749)
 1. NxM 행렬에서 부분행렬을 그려 그 안에 적힌 정수의 합을 구하기
 2. 정수의 합이 최대가 되는 부분행렬을 구하기
[입력]
 1. N: 세로, M: 가로
 2. N개의 줄: M개씩 행렬의 원소가 주어짐
[출력]
 1. 최대의 합 출력
"""

"""
<풀이>
 1. 누적합
"""


def dynamic_programming(matrix):
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

    # 누적합 구하기
    for x in range(1, N + 1):
        for y in range(1, M + 1):
            if x == 1 and y == 1:
                prefix_sum[x][y] = matrix[x][y]
            elif x == 1:
                prefix_sum[x][y] = prefix_sum[x][y - 1] + matrix[x][y]
            elif y == 1:
                prefix_sum[x][y] += prefix_sum[x - 1][y] + matrix[x][y]
            else:
                prefix_sum[x][y] = (matrix[x][y] +
                                    prefix_sum[x][y - 1] +
                                    prefix_sum[x - 1][y] -
                                    prefix_sum[x - 1][y - 1])

    # 최대값
    maximum = -10e9
    # 시작점
    for sx in range(1, N + 1):
        for sy in range(1, M + 1):
            # 끝점
            for ex in range(sx, N + 1):
                for ey in range(sy, M + 1):
                    total = (prefix_sum[ex][ey] -
                             prefix_sum[ex][sy - 1] -
                             prefix_sum[sx - 1][ey] +
                             prefix_sum[sx - 1][sy - 1])

                    # 최대값 갱신
                    if maximum < total:
                        maximum = total

    return maximum


N, M = map(int, input().split())
# 인덱스 조정을 위해 앞부분 삽입
matrix = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

print(dynamic_programming(matrix))