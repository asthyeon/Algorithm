import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 민준이와 마산 그리고 건우 (18223)
 1. 최단 경로 구하기
 2. 양방향 그래프, 출발지는 1번 정점, 마산은 V번 정점
 3. 만약 최단 경로랑 같은 거리상에 건우를 만날 수 있다면 만나기
[입력]
 1. V: 정점의 개수, E: 간선의 개수, P: 건우가 위치한 정점
 2. E 개의 줄: a 번 정점과 b 번 정점 사이의 거리가 c 임
[출력]
 1. 찾은 최단 경로 위에 건우가 있다면 "SAVE HIM", "GOOD BYE" 를 출력
"""

"""
<풀이>
 1. 다익스트라
 2. 건우까지의 최단 거리를 구하고 비교해보기
 3. P가 1일 때 고려하기
"""
import heapq


def dijkstra(roads, start, end):
    # 각 정점 거리 및 우선순위큐
    distances = [10000 * 10001] * (V + 1)
    hq = [(0, start)]
    distances[start] = 0

    while hq:
        now_dist, now = heapq.heappop(hq)

        # 인접 길 탐색
        for new_dist, new in roads[now]:
            sum_dist = now_dist + new_dist
            # 더 짧게 방문할 수 있다면 방문
            if distances[new] > sum_dist:
                distances[new] = sum_dist
                heapq.heappush(hq, ((sum_dist, new)))

    # 목적지까지의 거리 출력
    return distances[end]


V, E, P = map(int, input().split())
# 길 정보
roads = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())

    roads[a].append((c, b))
    roads[b].append((c, a))

# 최단 거리 (민준 -> V)
shortest = dijkstra(roads, 1, V)
# 민준 -> 건우 -> V
m_to_k = dijkstra(roads, 1, P) + dijkstra(roads, P, V)

# 조건에 맞게 출력
if shortest == m_to_k:
    print("SAVE HIM")
else:
    print("GOOD BYE")