import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제]
# 좋은 날 싫은 날 (17211)
1. 오늘의 기분이 내일의 기분에 영향을 줌
2. N일 뒤의 재현이의 기분?
3. 오늘의 기분에 따라 다음 날의 영향을 주는 확률이 주어짐
 - 오늘O 내일O, 오늘O 내일X, 오늘X 내일O, 오늘X 내일X
 - 좋은 날 = 0, 싫은 날 = 1  
[풀이]
1. dp
"""


def dynamic_programming(now):
    dp = [[0, 0] for _ in range(N + 1)]
    # 1일 뒤의 기분
    if now == 0:
        dp[1][0] = g_g
        dp[1][1] = g_b
    else:
        dp[1][0] = b_g
        dp[1][1] = b_b
    
    # N일 뒤의 기분 구하기
    for i in range(2, N + 1):
        dp[i][0] = dp[i - 1][0] * g_g + dp[i - 1][1] * b_g
        dp[i][1] = dp[i - 1][0] * g_b + dp[i - 1][1] * b_b

    return dp[N]


N, now = map(int, input().split())
g_g, g_b, b_g, b_b = map(float, input().split())

# 정답 출력
answer = dynamic_programming(now)
print(round(answer[0] * 1000))
print(round(answer[1] * 1000))