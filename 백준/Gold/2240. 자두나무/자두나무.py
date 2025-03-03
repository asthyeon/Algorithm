import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 자두나무 (2240)
 1. 매 초마다 두 나무 중 하나에서 열매가 떨어짐
 2. 열매가 떨어지는 순간 그 나무 아래에 서 있으면 열매를 받아먹을 수 있음
 3. 처음에는 1번 자두나무 아래에 위치
[입력]
 1. T: 자두가 떨어지는 시간
 2. W: 움직일 수 있는 최대 횟수
[출력]
 1. 받을 수 있는 자두의 최대 개수
"""

"""
<풀이>
 1. dp
 2. W가 홀수 -> 1번에서 2번으로 이동한 것
"""


def dynamic_programming(plum):
    # 행: 안움직일 때를 포함(W + 1), 열: 0초부터 포함(T + 1)
    dp = [[0] * (W + 1) for _ in range(T + 1)]

    # 1초 후부터 매 초 탐색
    for second in range(1, T + 1):
        # 한 번도 안움직일 때의 경우
        if plum[second] == 1:
            dp[second][0] = dp[second - 1][0] + 1
        else:
            dp[second][0] = dp[second - 1][0]

        # 한 번 이상 움직일 때
        for move in range(1, W + 1):
            # 1번 나무 아래서 1번 자두가 떨어질 때
            if move % 2 == 0 and plum[second] == 1:
                # (가만히 받기 vs 움직여서 받기) + 1
                dp[second][move] = max(dp[second - 1][move], dp[second - 1][move - 1]) + 1
            # 2번 나무 아래서 2번 자두가 떨어질 때
            elif move % 2 == 1 and plum[second] == 2:
                # (가만히 받기 vs 움직여서 받기) + 1
                dp[second][move] = max(dp[second - 1][move], dp[second - 1][move - 1]) + 1
            # 떨어지는 위치가 달라서 자두를 못받을 때
            else:
                # 가만히 있기 vs 움직이기
                dp[second][move] = max(dp[second - 1][move], dp[second - 1][move - 1])

    # 최대 개수 출력
    return max(dp[T])


T, W = map(int, input().split())
# 0초부터 떨어지는 자두 나무 번호
plum = [0] + [int(input()) for _ in range(T)]

print(dynamic_programming(plum))