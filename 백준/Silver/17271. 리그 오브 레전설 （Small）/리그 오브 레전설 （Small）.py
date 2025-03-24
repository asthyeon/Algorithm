import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def dynamic_programming(N, M):
    dp = [1] * (N + 1)

    for i in range(M, N + 1):
        dp[i] = (dp[i - 1] + dp[i - M]) % 1000000007

    return dp[N]


N, M = map(int, input().split())
print(dynamic_programming(N, M))