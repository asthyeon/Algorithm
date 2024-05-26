import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 무한 수열 2 (1354)
 1. Ai = 1 (i <= 0)
 2. Ai = A(i // P)- X + A(i // Q) - Y (i >= 1)
[입력]
 1. N, P, Q, X, Y
[출력]
 1. AN
"""

"""
<풀이>
 1. dp
 2. 딕셔너리를 만들어서 확인하기
"""
dp = {}


def dynamic_programming(N, P, Q, X, Y):
    # 조건 Ai = 1 (i <= 0)
    if N <= 0:
        return 1

    # 저장되지 않은 수라면 저장하기
    if N not in dp:
        # 무한수열
        dp[N] = (dynamic_programming(N // P - X, P, Q, X, Y) +
                 dynamic_programming(N // Q - Y, P, Q, X, Y))
    
    # N이 저장된다면 반환
    return dp[N]


N, P, Q, X, Y = map(int, input().split())

print(dynamic_programming(N, P, Q, X, Y))