import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 특정한 최단 경로 (1504)
1. 다익스트라 이용(임의의 두 정점은 반드시 통과)
2. 두 가지 경로만 고려하기
"""
import heapq


def dijkstra(graph, start, end, dist):
    distances = [200000 * 1001] * (N + 1)
    distances[start] = dist
    hq = [(dist, start)]

    while hq:
        now_dist, now = heapq.heappop(hq)
        # 목적지 도달 시 종료
        if now == end:
            return now_dist
        # 다음 장소 탐색
        for new_dist, new in graph[now]:
            new_dist += now_dist
            if new_dist < distances[new]:
                distances[new] = new_dist
                heapq.heappush(hq, (new_dist, new))

    # 목적지 도달 못할 시
    return maximum


N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
v1, v2 = map(int, input().split())

maximum = 200000 * 1001 * 3
v1_dist = 0
v2_dist = 0
# v1 - v2
for start, end in [(1, v1), (v1, v2), (v2, N)]:
    dist = dijkstra(graph, start, end, v1_dist)
    # 도달 가능할 시 거리 갱신
    if dist != maximum:
        v1_dist = dist
    # 도달 불가능
    else:
        print(-1)
        exit()

# v2 - v1
for start, end in [(1, v2), (v2, v1), (v1, N)]:
    dist = dijkstra(graph, start, end, v2_dist)
    # 도달 가능할 시 거리 갱신
    if dist != maximum:
        v2_dist = dist
    # 도달 불가능
    else:
        print(-1)
        exit()

print(min(v1_dist, v2_dist))