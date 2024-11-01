import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 특정 거리의 도시 찾기 (18352)
 1. 도시 X 로부터 최단 거리가 K 인 모든 도시들의 번호를 출력하기
 2. 도시 X -> X 의 최단 거리는 0
[입력]
 1. N: 도시의 개수, M: 도로의 개수, K: 거리 정보, X: 출발 도시의 번호
 2. M 개의 줄: A 번 도시에서 B 번 도시로 이동하는 단방향 도로 존재
[출력]
 1. 최단 거리가 K 인 모든 도시 번호를 오름차순으로 출력
 2. 하나도 존재하지 않으면 -1 출력
"""

"""
<풀이>
 1. 다익스트라
"""
import heapq


# 다익스트라
def dijkstra(cities):
    # 우선순위 큐 및 각 거리 정보
    hq = [(0, X)]
    distances = [10e9] * (N + 1)
    distances[X] = 0

    while hq:
        dist, now = heapq.heappop(hq)

        # 연결된 도시 탐색
        for new in cities[now]:
            # 거리 갱신
            new_dist = dist + 1
            # 기존 거리가 더 짧은 경우에 교체
            if distances[new] > new_dist:
                distances[new] = new_dist
                heapq.heappush(hq, (new_dist, new))

    # 거리가 K인 경우 정답 리스트에 넣기
    for check in range(1, N + 1):
        if check == X:
            continue

        if distances[check] == K:
            K_list.append(check)


N, M, K, X = map(int, input().split())
# 도시 정보
cities = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())

    cities[A].append(B)

# 정답 리스트
K_list = []
dijkstra(cities)

# 조건에 따라 정답 출력
if K_list:
    for city in K_list:
        print(city)
else:
    print(-1)