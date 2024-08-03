import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 주지수 (15724)
 1. 직사각형 범위의 사람 수를 구하기
 2. 네 개의 정수 시작 x, y와 끝 x, y가 주어짐
[입력]
 1. N, M: 영토의 크기
 2. N개의 줄: M개의 정수로 단위 구역 내 살고 있는 사람 수 정보
 3. K: 직사각형 범위의 개수
 4. K개의 줄: 네 개의 정수로 직사각형 범위 x1, y1, x2, y2
[출력]
 1. K개의 줄에 순서대로 주어진 직사각형 범위 내 살고 있는 사람 수의 합 출력
"""

"""
<풀이>
 1. 누적합
"""


# 누적합 구하기
def calculator(area):
    new_area = [[0] * (M + 1) for _ in range(N + 1)]

    # 누적합 계산
    for x in range(1, N + 1):
        for y in range(1, M + 1):
            if x == 1 and y == 1:
                new_area[x][y] = area[x - 1][y - 1]
            elif x == 1:
                new_area[x][y] = (new_area[x][y - 1] +
                                  area[x - 1][y - 1])
            elif y == 1:
                new_area[x][y] = (new_area[x - 1][y] +
                                  area[x - 1][y - 1])
            else:
                new_area[x][y] = (new_area[x - 1][y] +
                                  new_area[x][y - 1] -
                                  new_area[x - 1][y - 1] +
                                  area[x - 1][y - 1])

    return new_area


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

# 누적합 계산
prefix_sum = calculator(area)

# 질문 답하기
K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    print(prefix_sum[x2][y2] -
          prefix_sum[x1 - 1][y2] -
          prefix_sum[x2][y1 - 1] +
          prefix_sum[x1 - 1][y1 - 1])