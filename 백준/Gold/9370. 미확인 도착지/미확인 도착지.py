import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 미확인 도착지 (9370)
1. t 후보지 중에서 s에서 출발하여 g-h를 지나는 경로가 최단경로인 경우만 구하기

[풀이]
1. 다익스트라 
2. 출발지에서 모든 목적지 최단 경로 구하기
3. 각 후보 목적지에서 최단 경로 구하기
"""
import heapq
INF = 10e9


def dijkstra(start, graph):
    # 거리 초기화 및 시작값 설정
    distances = [INF] * (n + 1)
    distances[start] = 0
    hq = [(start, distances[start])]

    while hq:
        now, now_dist = heapq.heappop(hq)

        # 현재 거리가 더 적거나 같을 때만
        if now_dist <= distances[now]:
            for new, new_dist in graph[now]:
                total_dist = now_dist + new_dist
                # 다음 방문지에 더 짧게 도착할 수 있을 때만 방문
                if total_dist < distances[new]:
                    distances[new] = total_dist
                    heapq.heappush(hq, (new, total_dist))

    return distances


T = int(input())
for tc in range(1, T + 1):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    # 그래프 연결
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    # s, g, h 각 거리 구하기
    s_dist = dijkstra(s, graph)
    g_dist = dijkstra(g, graph)
    h_dist = dijkstra(h, graph)

    answer = []
    # 목적지 후보 순회
    for _ in range(t):
        x = int(input())

        # 실제 최단 겅로
        shortest = s_dist[x]
        # 필수 교차로를 거친 최단 경로 (s-g-h-x or s-h-g-x)
        essential = min(s_dist[g] + g_dist[h] + h_dist[x], s_dist[h] + h_dist[g] + g_dist[x])

        # 두 거리가 같다면 정답 추가
        if shortest == essential:
            answer.append(x)

    # 정렬된 값 출력
    print(*sorted(answer))



