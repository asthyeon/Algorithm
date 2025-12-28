import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 랜선 자르기 (1654)
1. 랜선을 모두 N개의 같은 길이의 랜선으로 만들기
2. 만들 수 있는 최대 랜선의 길이를 구하기

[풀이]
1. 이진 탐색
"""


def binary_search(K, cables):
    start = 1
    end = cables[-1]
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        
        # 랜선 수
        cnt = 0
        # 현재의 mid 값으로 각 케이블을 잘라서 나오는 개수 더하기
        for cable in cables:
            cnt += cable // mid
        
        # 만들어진 랜선 수가 더 많거나 같다면 정답 갱신 및 간격 늘리기
        if cnt >= K:
            start = mid + 1
            answer = mid
        # 만들어진 랜선 수가 더 적다면 간격 줄이기
        else:
            end = mid - 1

    return answer


N, K = map(int, input().split())
cables = [int(input()) for _ in range(N)]
cables.sort()

print(binary_search(K, cables))