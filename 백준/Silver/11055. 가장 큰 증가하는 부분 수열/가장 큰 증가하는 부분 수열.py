import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 가장 큰 증가하는 부분 수열 (11055)
1. 수열의 증가하는 부분 수열 중 합이 가장 큰 것 구하기 

[풀이]
1. dp
"""


def dynamic_programming(A):
    # A 복사
    dp = A[:]

    # 현재 위치까지
    for end in range(N):
        # 현재 위치보다 이전 값에서부터
        for start in range(end):
            # 증가하는 수열이라면
            if A[start] < A[end]:
                # 현재 위치 값 vs 이전 위치 값 + 현재 A 값
                dp[end] = max(dp[end], dp[start] + A[end])

    # 가장 큰 합 반환
    return max(dp)


N = int(input())
A = list(map(int, input().split()))

print(dynamic_programming(A))