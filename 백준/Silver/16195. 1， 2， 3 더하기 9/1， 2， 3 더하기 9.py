import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 1, 2, 3 더하기 9 (16195)
 1. 정수 n과 m이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수 구하기
 2. 단, 사용한 개수는 m개 이하여야 함
[입력]
 1. T: 테스트 케이스의 개수
 2. n: 나타내야 할 정수, m: 사용할 수 있는 수의 개수
[출력]
 1. n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지 출력
 2. 단, 사용한 수의 개수는 m개 이하여야 함
"""

"""
<풀이>
 1. dp
1: 1개 1 > 1개
2: 1개 2 > 1개
   2개 1 + 1 > 1개
3: 1개 3 > 1개
   2개 1 + 2, 2 + 1 > 2개
   3개 1 + 1 + 1 > 1개
4: 1개 X
   2개 1 + 3, 2 + 2, 3 + 1 > 3개
   3개 1 + 1 + 2, 1 + 2 + 1, 2 + 1 + 1 > 3개
   4개 1 + 1 + 1 + 1 > 1개

4의 1개 -> X
4의 2개 -> 1의 1개 + 2의 1개 + 3의 1개 = 3
4의 3개 ->           2의 2개 + 3의 2개 = 3
4의 4개 ->                     3의 3개 = 1
"""
REST = 1000000009

dp = [[0] * 1001 for _ in range(1001)]

# 1을 1개의 수로
dp[1][1] = 1
# 2를 1개, 2개의 수로
dp[2][1] = 1
dp[2][2] = 1
# 3을 1개, 2개, 3개의 수로
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1

# 4 이후
for i in range(4, 1001):
    # 1개부터 i개까지
    for j in range(1, i + 1):
        # 이번 수의 각 개수는 -1한 수, -2한 수, -3한 수의 j - 1개
        dp[i][j] = (dp[i - 3][j - 1] + dp[i - 2][j - 1] + dp[i - 1][j - 1]) % REST

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())

    # 1개 ~ m개 이하
    print(sum(dp[n][1:m + 1]) % REST)