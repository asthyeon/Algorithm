import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 사다리 (2022)
 1. 길이가 x인 사다리는 오른쪽 빌딩의 아래를 받침대로 하여 왼쪽 빌딩에 기대져 있음
 2. 길이가 y인 사다리는 위와 반대
 3. 두 사다리는 땅에서부터 정확하게 c인 지점에서 서로 교차
[입력]
 1. x, y, c 입력
[출력]
 1. 두 빌딩 사이에 너비가 되는 수치를 출력
 2. 절대/상대 오차는 10 ** (-3) 까지 허용
"""

"""
<풀이>
 1. 수학, 이분탐색
 2. 삼각형의 높이와 관련된 비율 계산
  - 두 빌딩 사이에 너비가 되는 수치를 t라고 할 때
  - c를 기준으로 왼쪽은 t1, 오른쪽은 t2
  - 왼쪽 삼각형의 높이는 h1, 오른쪽의 삼각형의 높이는 h2 일 때
  - t1 : c = t : h2, t2 : c = t : h1
  - c * t = t1 * h2, c * t = t2 * h1
  - t1 = c * t / h2, t2 = c * t / h1
  - t = (c * t / h2) + (c * t / h1) = c * t * (h1 + h2) / (h1 * h2)
  - 1 = c * (h1 + h2) / (h1 * h2)
  - c = (h1 * h2) / (h1 + h2)
 3. 피타고라스의 정리
  - x ** 2 = h1 ** 2 + t ** 2
  - h1 = (x ** 2 - t ** 2) ** 0.5
  - y ** 2 = h2 ** 2 + t ** 2
  - h2 = (y ** 2 - t ** 2) ** 0.5
 4. 이분탐색으로 t 값을 적절하게 넣어보며 c를 구했을 때 차이가 얼마나 나는지 확인 
"""


# c 구하기
def calculate(mid):
    # h1과 h2 구하기
    h1 = (x ** 2 - mid ** 2) ** 0.5
    h2 = (y ** 2 - mid ** 2) ** 0.5
    # 그에 따른 c 구하기
    new_c = (h1 * h2) / (h1 + h2)
    return new_c


# 이분 탐색
def binary_search(x, y, c):
    start = 0
    # x, y 중 더 작은 값을 t의 최대 값으로
    end = min(x, y)
    # 절대/상대 오차 범위 포함
    while start + (10 ** (-3)) <= end:
        mid = (start + end) / 2

        # 이번에 구한 t 값이 c보다 크거나 같으면 증가
        if calculate(mid) >= c:
            start = mid
        # 반대일 경우 감소 시키기
        else:
            end = mid

    return start


x, y, c = map(float, input().split())

print(binary_search(x, y, c))