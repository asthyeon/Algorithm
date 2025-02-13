import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 1로 만들기 2 (12852)
 1. 사용할 수 있는 연산
  (1) X가 3으로 나누어 떨어지면, 3으로 나눔
  (2) X가 2으로 나누어 떨어지면, 2으로 나눔
  (3) 1을 뺌
[입력]
 1. N: 자연수
[출력]
 1. 첫째 줄: 연산을 하는 횟수의 최솟값 출력
 2. 둘째 줄: N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력 
"""

"""
<풀이>
 1. dp
"""


def dynamic_programming(N):
    dp = [0] * (N + 1)

    # 역순으로 구하기
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1
        # 2로 나누어 떨어질 때
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        # 3으로 나누어 떨어질 때
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    # 정답 리스트
    answers = [N]
    # 현재 값과, 정답이 되기 이전의 개수
    cnt = dp[N] - 1
    now = N
    # N - 1 부터 줄여 나가기
    for prev in range(N - 1, 0, -1):
        # 정답이 되기 이전의 개수이고, 조건을 만족할 때
        if dp[prev] == cnt and (prev + 1 == now or prev * 2 == now or prev * 3 == now):
            # 답 추가 및, 현재 값과 개수 갱신
            answers.append(prev)
            now = prev
            cnt -= 1

    print(dp[N])
    print(*answers)


N = int(input())

dynamic_programming(N)