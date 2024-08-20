import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 함께 블록 쌓기 (18427)
 1. 학생마다 최대 M개의 블록을 가지며, 가진 모든 블록들의 높이가 서로 다름
 2. 어떤 학생의 블록은 사용하지 않아도 되고, 한 학생당 최대 1개의 블록만 사용 가능
[입력]
 1. N: 학생 수, M: 한 학생당 블록 수, H: 탑의 높이
 2. N개의 줄: 각 학생이 가진 블록들의 높이
[출력]
 1. 높이가 H인 탑을 만드는 경우의 수를 10,007로 나눈 나머지 출력
"""

"""
<풀이>
 1. dp
"""


# dp
def dynamic_programming(students):
    dp = [[0] * (H + 1) for _ in range(N + 1)]

    # 높이 0을 만드는 경우는 1가지
    dp[0][0] = 1
    # 학생 순회
    for n in range(1, N + 1):
        # 블록을 사용하지 않는 경우 복사
        dp[n] = dp[n - 1][:]
        # 각 블록 순회
        for block in students[n]:
            # 이번 블록보다 크거나 같은 높이 순회
            for h in range(block, H + 1):
                # 이번 경우의 수에 이전에 블록을 사용하지 않았을 때 경우의 수 더하기
                dp[n][h] += dp[n - 1][h - block]
    
    return dp[N][H] % 10007


N, M, H = map(int, input().split())
students = [[]]
for _ in range(N):
    student = list(map(int, input().split()))
    students.append(student)

print(dynamic_programming(students))