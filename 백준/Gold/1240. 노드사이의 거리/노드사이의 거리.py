import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
<문제>
# 노드사이의 거리 (1240)
1. N개의 노드로 이루어진 트리에서, 두 노드 쌍을 입력받을 때 두 노드 사이의 거리 출력
<풀이>
1. 그래프 문제 -> 최단거리 찾기 -> 다익스트라
2. 우선순위큐 -> 거리를 기준으로 정렬해야함
3. 최대 거리가 10000 * 1001 이 되어야함
"""
import heapq


def dijkstra(start, end):
    # 각 노드별 최대 거리, 우선순위큐, 시작점 초기화
    distances = [10000 * 1001] * (N + 1)
    hq = [(0, start)]
    distances[start] = 0

    while hq:
        now_dist, now = heapq.heappop(hq)

        # 도착지에 도달하면 최종거리 return
        if now == end:
            return distances[end]

        # 다음 노드까지의 거리 탐색
        for new_dist, new in graph[now]:
            if distances[new] > now_dist + new_dist:
                distances[new] = now_dist + new_dist
                heapq.heappush(hq, (now_dist + new_dist, new))


# N: 노드의 개수, M: 거리를 알고 싶은 노드 쌍의 개수
N, M = map(int, input().split())
# graph 연결
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B, D = map(int, input().split())
    # 거리를 기준으로 정렬
    graph[A].append((D, B))
    graph[B].append((D, A))

# 정답 출력
for _ in range(M):
    start, end = map(int, input().split())

    print(dijkstra(start, end))