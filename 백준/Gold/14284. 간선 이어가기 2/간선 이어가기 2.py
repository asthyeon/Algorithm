import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 간선 이어가기 2(14284)
 1. 무방향 그래프와 가중치 간선 정보가 담긴 리스트가 주어짐
 2. 간선 리스트의 간선 하나씩을 추가해가며 정점 s와 t가 연결되는 시점에서 멈춤
[입력]
 1. n: 정점 수, m: 간선 수
 2. m개의 줄의 a, b, c: a와 b는 c의 가중치를 가짐
 3. s, t: 마지막 연결 정점들
 4. 모든 간선을 연결하면 그래프는 연결 그래프가 됨
[출력]
 1. s와 t가 연결되는 시점의 간선의 가중치 합의 최솟값 구하기
"""

"""
<풀이>
 1. 다익스트라
 2. 길게 먼저 도착하는 경우도 있으므로 다 돌아보기
 3. 간선을 정렬하면 도착지에 먼저 도착 가능시 종료 가능할까?
  - 다음 탐색시에 도달하는 건 불가능
  - 현재 위치가 도달했을 때는? -> 간선 정렬 안해도 상관없음
"""
import heapq
INF = 10e9


def dijkstra(graph, s, t):
    # 거리 정보
    distances = [INF] * (n + 1)
    # 힙큐 생성 및 시작점 인큐, 초기화
    hq = [(0, s)]
    distances[s] = 0

    while hq:
        dist, now = heapq.heappop(hq)

        # 목적지에 도달하면 종료
        if now == t:
            return dist

        # 다음 탐색
        for new in graph[now]:
            new_dist = dist + new[0]
            # 다음 위치를 더 짧게 방문할 수 있다면 방문
            if distances[new[1]] > new_dist:
                heapq.heappush(hq, (new_dist, new[1]))
                distances[new[1]] = new_dist

    return distances[t]


# 정점 수 n, 간선 수 m
n, m = map(int, input().split())
# 그래프 정보
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    # 간선 정보(정점 a와 b의 가중치 c)
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

# 마지막 정점
s, t = map(int, input().split())
print(dijkstra(graph, s, t))