import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 공유기 설치 (2110)
1. 최대한 많은 곳에서 와이파이를 설치
2. 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치

[풀이]
1. 이진 탐색
2. 설치 갯수가 크거나 같을 때도 정답 갱신하기
"""


def binary_search(N, C, houses):
    start = 1
    end = houses[-1]
    answer = 0

    while start <= end:
        middle = (start + end) // 2

        # 공유기 설치 수, 설치된 위치
        install = 0
        installed = 0
        for i in range(N):
            # 처음에는 무조건 설치
            if i == 0:
                install += 1
                installed = houses[i]
                continue
            # 현재 위치에 설치할 수 있는 경우 설치
            if abs(houses[i] - installed) >= middle:
                install += 1
                installed = houses[i]

        # 더 많이 설치할 수 있거나 같으면 정답 갱신 및 간격 늘리기
        if install >= C:
            start = middle + 1
            answer = middle
        # 적게 설치되면 간격 줄이기
        else:
            end = middle - 1

    return answer


N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

print(binary_search(N, C, houses))