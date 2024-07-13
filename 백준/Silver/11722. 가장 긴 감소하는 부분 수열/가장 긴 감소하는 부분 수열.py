import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 가장 긴 감소하는 부분 수열 (11722)
 1. 수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열 구하기
[입력]
 1. N: 수열 A의 크기
 2. 둘째 줄: 수열 A가 주어짐
[출력]
 1. 정답 출력
"""

"""
<풀이>
 1. dp
"""


# dp
def dynamic_programming(sequence):
    # 각 부분 수열의 최소 길이 = 1
    dp = [1] * N

    # 2번째 수부터 순회
    for target in range(1, N):
        # 이번 수의 이전 수들
        for previous in range(target):
            # 이번 수가 이전 수보다 작으면
            if A[target] < A[previous]:
                # 이번 수 값 vs 이전 수에 하나를 더한 것 중 큰 값
                dp[target] = max(dp[target], dp[previous] + 1)
    
    # 가장 큰 값 출력
    return max(dp)


N = int(input())
A = list(map(int, input().split()))

print(dynamic_programming(A))
