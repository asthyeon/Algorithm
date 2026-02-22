import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 최소비용 구하기 (1916)
1. 버스 비용 최소화하기

[풀이]
1. 다익스트라 -> 시간초과
2. 현재 비용이 더 적거나 같을 때만 방문하기
"""
import heapq


def dijkstra(cities, start, end):
    # 거리 초기화
    distances = [10e9] * (N + 1)
    hq = [(start, 0)]
    distances[start] = 0

    while hq:
        now, now_cost = heapq.heappop(hq)

        # 현재 비용이 더 적거나 같을 때만
        if now_cost <= distances[now]:
            # 다음 도시 탐색
            for new, new_cost in cities[now]:
                total_cost = now_cost + new_cost
                # 이번 비용이 더 적을 때만 방문
                if total_cost < distances[new]:
                    distances[new] = total_cost
                    heapq.heappush(hq, (new, total_cost))

    return distances[end]


N = int(input())
M = int(input())
# 그래프 연결
cities = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    cities[A].append((B, C))
start, end = map(int, input().split())

print(dijkstra(cities, start, end))