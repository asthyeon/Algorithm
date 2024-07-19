import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
1 -> 1 [1]
2 -> 1 + 1, 2 [2]
3 -> 1 + 1 + 1, 1 + 2, 2 + 1, 3 [4]
4 -> [7]
"""

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 11):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())

    print(dp[n])
