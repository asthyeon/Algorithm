import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 사냥꾼 (8983)
 1. 사냥꾼은 일직선 상에 위치한 M 개의 사대에서만 사격 가능
 2. 사냥꾼은 한 사대에서 거리가 L 보다 작거나 같은 위치의 동물들을 잡을 수 있음
  - 거리 계산: |x - a| + b
  - 사대 위치: x
  - 동물 위치: (a, b)
[입력]
 1. M: 사대의 수, N: 동물의 수, L: 사정거리
 2. M개의 x 좌표 값
 3. N개의 줄: 동물의 위치 x 좌표 값, y 좌표 값
[출력]
 1. 잡을 수 있는 동물의 수를 음수가 아닌 정수로 출력
"""

"""
<풀이>
 1. 일단 풀어보기 -> 이분 탐색
"""


# 이분 탐색
def binary_search(a, shooting):
    start = 0
    end = M - 1

    while start < end:
        middle = (start + end) // 2

        # 더 작으면 늘리기
        if shooting[middle] < a:
            start = middle + 1
        # 더 크면 줄이기
        elif shooting[middle] > a:
            end = middle - 1
        # 일치할 경우 끝내기
        else:
            start = middle
            break

    return start


M, N, L = map(int, input().split())
# 사대 위치, 정렬
shooting = list(map(int, input().split()))
shooting.sort()

# 잡을 수 있는 동물 수
total = 0
# 동물 위치
for _ in range(N):
    a, b = map(int, input().split())

    # 가장 가까운 사대 찾기
    closest = binary_search(a, shooting)

    # 가장 가까운 사대일 때 거리 계산
    if abs(shooting[closest] - a) + b <= L:
        total += 1
    # 가장 가까운 사대 오른쪽 사대가 범위 안일 때
    elif closest + 1 < M:
        if abs(shooting[closest + 1] - a) + b <= L:
            total += 1
    # 가장 가까운 사대 왼쪽 사대가 범위 안일 때
    elif closest - 1 >= 0:
        if abs(shooting[closest - 1] - a) + b <= L:
            total += 1

print(total)