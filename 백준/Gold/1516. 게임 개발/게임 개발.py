import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 게임 개발 (1516)
 1. 모든 건물을 짓는데 걸리는 최소의 시간을 이용하여 근사하기로 함
 2. 건물의 순서가 있을 수 있음, 동시에 짓는 것은 불가능
[입력]
 1. N: 건물의 종류 수
 2. N개의 줄: 각 건물을 짓는데 걸리는 시간과 먼저 지어져야 하는 건물들의 번호가 주어짐
[출력]
 1. N개의 각 건물이 완성되기까지 걸리는 최소 시간 출력
"""

"""
<풀이>
 1. 위상정렬 및 dp
"""
from collections import deque


# dp
def dynamic_programming(times, preceding, orders):
    dp = [0] * (N + 1)
    q = deque([])

    for i in range(1, N + 1):
        # 선행 건물이 없는 경우
        if not orders[i]:
            # 첫번째 건물들 시간 배정 및 인큐
            dp[i] = times[i]
            q.append(i)

    # 큐를 이용해 순서대로 처리하기
    while q:
        now = q.popleft()

        # 후행 건물들 처리하기
        for new in preceding[now]:
            # 선행 건물 수 -1
            orders[new] -= 1
            # dp 값 갱신 (현재 값 or 이전 값 + 현재 시간)
            dp[new] = max(dp[new], dp[now] + times[new])

            # 선행 건물이 없어진 경우 인큐
            if not orders[new]:
                q.append(new)

    # 정답 출력
    for j in range(1, N + 1):
        print(dp[j])


N = int(input())
# 각 건물들 걸리는 시간
times = [0] * (N + 1)
# 각 건물들의 선행 건물들
preceding = [[] for _ in range(N + 1)]
# 각 건물들의 선행 건물 순서
orders = [0] * (N + 1)

# 건물 입력 받기
for number in range(1, N + 1):
    building = list(map(int, input().split()))
    # 건물 시간 배정
    times[number] = building[0]
    # 선행 건물 번호가 있는 경우
    if len(building) > 2:
        # 선행 해야 하는 위치에 붙이기
        for pre in building[1:len(building) - 1]:
            preceding[pre].append(number)
            # 선행 건물 순서 조정
            orders[number] += 1

dynamic_programming(times, preceding, orders)