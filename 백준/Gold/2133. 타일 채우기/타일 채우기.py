import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 타일 채우기 (2133)
 1. 3 x N 크기의 벽을 2 x 1, 1 x 2 크기의 타일로 채우는 경우의 수 구하기
[입력]
 1. N: 벽 크기
[출력]
 1. 경우의 수 출력
"""

"""
<풀이>
 1. dp
n = 1 [0가지]
n = 2 [3가지]
 - 새로 생긴 것 3가지(A)
n = 3 [0가지]
n = 4 [3 * 3 + 2가지]
 - 자기 자신 3가지 붙인 경우(A)
 - 새로 생긴 것 2가지(B)
n = 5 [0가지]
n = 6 [(11 * 3) + (3 * 2) + 2가지]
 - 자기 자신 3가지 붙인 경우(A)
 - 자기 자신 2가지 붙인 경우(B)
 - 새로 생긴 것 2가지(C)
 2. 누적합도 함께 저장하기
"""


def dynamic_programming(N):
    dp = [0] * (N + 1)
    prefix_sum = [0] * (N + 1)

    # 2 이상일 때
    if N >= 2:
        dp[2] = 3
        prefix_sum[2] = 3

        for i in range(4, N + 1):
            # 짝수
            if i % 2 == 0:
                # (이전의 개수 * 3) + (이전의 개수 * 2) + 새로운 것(2가지)
                dp[i] = (dp[i - 2] * 3) + (prefix_sum[i - 4] * 2) + 2
                # 누적 합 갱신
                prefix_sum[i] = dp[i] + prefix_sum[i - 2]
    
    return dp[N]


N = int(input())

print(dynamic_programming(N))