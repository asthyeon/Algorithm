import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 수강 과목 (17845)
 1. 공부 시간의 한계 초과 X
 2. 과목의 중요도 합이 최대가 되도록 몇 개만 선택하기
[입력]
 1. N: 최대 공부시간, K: 과목 수
 2. K개의 줄: I: 중요도, T: 필요한 공부시간
[출력]
 1. 얻을 수 있는 최대 중요도 출력
"""

"""
<풀이>
 1. dp
"""


def dynamic_programming(N, K, subjects):
    # 최대 공부시간 * K
    dp = [[0] * (N + 1) for _ in range(1 + K)]

    # 과목 K개 순회
    for turn in range(1, K + 1):
        # 시간만큼 순회
        for time in range(1, N + 1):
            # 이번 시간에 이번 과목을 못 들을 때
            if time < subjects[turn][1]:
                # 이전에 과목을 들었던 값으로 교체
                dp[turn][time] = dp[turn - 1][time]
            # 이번 시간에 이번 과목을 들을 수 있을 때
            else:
                # 이전에 과목을 들었던 값 vs 이전 과목에서 이번 시간을 뺀 값 + 이번 과목 중요도
                dp[turn][time] = max(dp[turn - 1][time],
                                     dp[turn - 1][time - subjects[turn][1]] + subjects[turn][0])

    return dp[K][N]


# 최대 공부시간 N, 과목 수 K
N, K = map(int, input().split())
subjects = [(0, 0)]
for _ in range(K):
    # 중요도 I, 필요한 공부시간 T
    I, T = map(int, input().split())
    subjects.append((I, T))

print(dynamic_programming(N, K, subjects))