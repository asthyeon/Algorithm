import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 수 찾기 (1920)
1. N개의 정수가 주어졌을 때, 이 안에 X라는 정수가 존재하는 지 알아내기

[풀이]
1. 이진 탐색
2. 값의 범위가 아니라 A의 범위에서 찾아야함
"""


def binary_search(A, integer):
    # 인덱스 범위로 지정
    start = 0
    end = N - 1

    while start <= end:
        # 인덱스 범위를 추정
        middle = (start + end) // 2

        # 정답을 찾으면 1 반환
        if A[middle]== integer:
            return 1
        # 정답보다 작으면 간격 늘리기
        elif A[middle] < integer:
            start = middle + 1
        # 정답보다 크면 간격 줄이기
        else:
            end = middle - 1

    return 0


N = int(input())
A = list(map(int, input().split()))
M = int(input())
integers = list(map(int, input().split()))
A.sort()

for integer in integers:
    print(binary_search(A, integer))