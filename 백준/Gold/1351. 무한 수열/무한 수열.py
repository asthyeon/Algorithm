import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 무한 수열 (1351)
 1. A(0) = 1
 2. A(i) = A(⌊i/P⌋) + A(⌊i/Q⌋)
 3. ⌊x⌋ -> x를 넘지 않는 가장 큰 정수
[입력]
 1. N, P, Q
[출력]
 1. A(N)
"""

"""
<풀이>
 1. dp 바텀업 -> N이 커서 메모리 초과날 것 같음
 2. 탑다운
"""


# 재귀
def recursion(N, P, Q):
    # 값 발견 시 재귀 X
    if N in dp:
        return dp[N]

    # 값이 없을 시 재귀하며 값 생성
    dp[N] = recursion(N // P, P, Q) + recursion(N // Q, P, Q)
    return dp[N]


N, P, Q = map(int, input().split())

dp = {0: 1}
print(recursion(N, P, Q))