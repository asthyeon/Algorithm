import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 최단경로 (1753)
1. 다익스트라
2. 우선순위 큐로 최적화
"""
import heapq


def dijkstra(start, graph):
    # 각 시작점에서의 거리(간선수 * 가중치를 초과한 최대값), 시작점 초기화 및 인큐
    distances = [300001 * 10] * (V + 1)
    distances[start] = 0
    hq = [(0, start)]

    while hq:
        # 현재 거리, 현재 위치
        now_dist, now = heapq.heappop(hq)

        # 새로운 위치 탐색
        for new, new_dist in graph[now]:
            total = now_dist + new_dist
            # 더 짧게 방문할 수 있는 경우 방문
            if total < distances[new]:
                distances[new] = total
                heapq.heappush(hq, (total, new))

    # 정답 출력
    for i in range(1, V + 1):
        # 방문하지 못한 경우만 예외 처리
        if distances[i] == 300001 * 10:
            print('INF')
            continue
        print(distances[i])


V, E = map(int, input().split())
K = int(input())
# 그래프 간선 연결
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(K, graph)