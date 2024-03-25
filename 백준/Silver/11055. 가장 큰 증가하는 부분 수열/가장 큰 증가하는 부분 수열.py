import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 가장 큰 증가하는 부분 수열(11055)
 1. 수열 A가 주어졌을 때 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것 구하기
[입력]
 1. N: 수열 A의 크기
 2. A: 수열
[출력]
 1. 수열 A의 합이 가장 큰 증가하는 부분 수열의 합 출력
"""

"""
<풀이>
 1. dp
 2. 배열을 2개를 만들어서 가장 큰 증가하는 부분 수열의 길이와 합을 구하기
"""


# dp
def dynamic_programming(A):
    # 길이(기본 길이 1)
    dp_len = [1] * N
    # 합(기본 값
    dp_sum = A[:]

    for i in range(1, N):
        # 자신보다 작은 수의길이 및 합 갱신
        for j in range(i):
            if A[j] < A[i]:
                dp_len[i] = max(dp_len[i], dp_len[j] + 1)
                dp_sum[i] = max(dp_sum[i], dp_sum[j] + A[i])

    # 가장 큰 합 반환
    return max(dp_sum)


# 수열 A의 크기 N
N = int(input())
# 수열 A
A = list(map(int, input().split()))

print(dynamic_programming(A))