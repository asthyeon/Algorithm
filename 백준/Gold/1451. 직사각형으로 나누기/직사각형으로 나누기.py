import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 직사각형으로 나누기 (1451)
 1. N * M 크기로 직사각형에 수를 N * M개 써놓았다
 2. 이 직사각형을 겹치지 않는 3개의 작은 직사각형으로 나누기
 3. 각각의 칸은 단 하나의 작은 직사각형에 포함되어야 함
 4. 각각의 작은 직사각형은 적어도 하나의 숫자를 포함해야 함
 5. 어떤 작은 직사각형의 합은 그 속에 있는 수의 합
[입력]
 1. N: 세로 크기, M: 가로 크기
 2. N개의 줄: 윗줄부터 한 줄에 하나씩 M개의 수가 주어짐
[출력]
 1. 세 개의 작은 직사각형의 합의 곱의 최댓값 출력
"""

"""
<풀이>
 1. 일단 풀어보기
 2. 직사각형을 3개의 직사각형으로 나누는 경우의 수 = 6가지
 3. 각각의 경우의 수를 모두 탐색
  (1) ㅡㅡ  (2) ㅣㅣㅣ (3) ㅣㅡㅡ  (4) ㅡㅡㅣ  (5) ㅡㅡ  (6) ㅣㅣ
      ㅡㅡ      ㅣㅣㅣ     ㅣㅡㅡ      ㅡㅡㅣ      ㅣㅣ      ㅣㅣ
      ㅡㅡ                                         ㅣㅣ      ㅡㅡ
 4. 누적 합으로 영역별 합 구해놓기
"""


# 각 직사각형의 합 구하기
def calculator(x1, y1, x2, y2, prefix_sum):
    # 해당 영역의 합 구하기
    return prefix_sum[x2][y2] + prefix_sum[x1 - 1][y1 - 1] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1]


N, M = map(int, input().split())
# 인덱스 조정을 위해 0 추가
rectangle = [[0] * (M + 1)]
for _ in range(N):
    # 인덱스 조정을 위해 0 추가
    numbers = [0] + list(map(int, list(input().rstrip())))

    rectangle.append(numbers)

# 각 영역별 누적합
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
for x in range(1, N + 1):
    for y in range(1, M + 1):
        if x == 0 and y == 0:
            prefix_sum[x][y] = rectangle[x][y]
        elif x == 0:
            prefix_sum[x][y] = prefix_sum[x][y - 1] + rectangle[x][y]
        elif y == 0:
            prefix_sum[x][y] = prefix_sum[x - 1][y] + rectangle[x][y]
        else:
            prefix_sum[x][y] = (prefix_sum[x - 1][y] +
                                prefix_sum[x][y - 1] +
                                rectangle[x][y] -
                                prefix_sum[x - 1][y - 1])

# 최대 곱
maximum = 0
# (1) 경우
for i in range(1, M - 1):
    for j in range(i + 1, M):
        small_rectangle1 = calculator(1, 1, N, i, prefix_sum)
        small_rectangle2 = calculator(1, i + 1, N, j, prefix_sum)
        small_rectangle3 = calculator(1, j + 1, N, M, prefix_sum)
        maximum = max(maximum, small_rectangle1 * small_rectangle2 * small_rectangle3)

# (2) 경우
for i in range(1, N - 1):
    for j in range(i + 1, N):
        small_rectangle1 = calculator(1, 1, i, M, prefix_sum)
        small_rectangle2 = calculator(i + 1, 1, j, M, prefix_sum)
        small_rectangle3 = calculator(j + 1, 1, N, M, prefix_sum)
        maximum = max(maximum, small_rectangle1 * small_rectangle2 * small_rectangle3)

# (3) 경우
for i in range(1, M):
    for j in range(1, N):
        small_rectangle1 = calculator(1, 1, N, i, prefix_sum)
        small_rectangle2 = calculator(1, i + 1, j, M, prefix_sum)
        small_rectangle3 = calculator(j + 1, i + 1, N, M, prefix_sum)
        maximum = max(maximum, small_rectangle1 * small_rectangle2 * small_rectangle3)

# (4) 경우
for i in range(1, N):
    for j in range(1, M):
        small_rectangle1 = calculator(1, 1, i, j, prefix_sum)
        small_rectangle2 = calculator(i + 1, 1, N, j, prefix_sum)
        small_rectangle3 = calculator(1, j + 1, N, M, prefix_sum)
        maximum = max(maximum, small_rectangle1 * small_rectangle2 * small_rectangle3)

# (5) 경우
for i in range(1, N):
    for j in range(1, M):
        small_rectangle1 = calculator(1, 1, i, M, prefix_sum)
        small_rectangle2 = calculator(i + 1, 1, N, j, prefix_sum)
        small_rectangle3 = calculator(i + 1, j + 1, N, M, prefix_sum)
        maximum = max(maximum, small_rectangle1 * small_rectangle2 * small_rectangle3)

# (6) 경우
for i in range(1, N):
    for j in range(1, M):
        small_rectangle1 = calculator(1, 1, i, j, prefix_sum)
        small_rectangle2 = calculator(1, j + 1, i, M, prefix_sum)
        small_rectangle3 = calculator(i + 1, 1, N, M, prefix_sum)
        maximum = max(maximum, small_rectangle1 * small_rectangle2 * small_rectangle3)

print(maximum)