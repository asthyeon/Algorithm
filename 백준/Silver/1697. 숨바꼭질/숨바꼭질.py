import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 숨바꼭질 (1697)
1. 다익스트라
"""
from collections import deque


def dijkstra(start, end):
    distances = [200000] * 100001
    q = deque([start])
    distances[start] = 0

    while q:
        now = q.popleft()

        # 뒤로 이동
        if now - 1 >= 0 and distances[now - 1] > distances[now] + 1:
                distances[now - 1] = distances[now] + 1
                q.append(now - 1)
        # 앞으로 이동
        if now + 1 <= 100000 and distances[now + 1] > distances[now] + 1:
                distances[now + 1] = distances[now] + 1
                q.append(now + 1)
        # 순간이동
        if 0 <= now * 2 <= 100000 and distances[now * 2] > distances[now] + 1:
                distances[now * 2] = distances[now] + 1
                q.append(now * 2)

    return distances[end]


# 시작점과 도착점
N, K = map(int, input().split())

# 시작점과 도착점이 같을 때
if N == K:
    print(0)
# 그 외
else:
    print(dijkstra(N, K))