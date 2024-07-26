import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 도시 건설 (21924)
 1. 모든 건물이 도로를 통해 연결되도록 최소한의 도로 만들기
 2. 전체 도로비용에서 최소 비용으로 만든 비용을 제외한 절약한 비용을 구하기
[입력]
 1. N: 건물의 개수, M: 도로의 개수
 2. M개의 줄: a와 b 건물은 c의 비용의 도로로 이어짐
[출력]
 1. 예산을 얼마나 절약할 수 있는지 출력
 2. 모든 건물이 연결되어 있지 않는다면 -1 출력
"""

"""
<풀이>
 1. 다익스트라
"""
import heapq


# 다익스트라
def dijkstra(buildings, total):
    visited = [0] * (N + 1)
    pq = [(0, 1)]
    # 최소 비용
    minimum = 0

    while pq:
        cost, now = heapq.heappop(pq)
        # 방문한 경우 넘기기
        if visited[now]:
            continue

        # 방문 처리 및 비용 합산
        visited[now] = 1
        minimum += cost

        # 새 도로 연결
        for new in buildings[now]:
            if not visited[new[1]]:
                heapq.heappush(pq, (new[0], new[1]))

    # 전체 도로 연결 확인
    for visit in range(1, N + 1):
        # 연결되지 않은 도로가 있을 경우 -1 출력
        if not visited[visit]:
            return -1

    # 전체 도로가 연결되어 있을 경우: (총 비용) - (최소 비용)
    return total - minimum


N, M = map(int, input().split())
# 건물들
buildings = [[] for _ in range(N + 1)]
# 전체 비용
total = 0
for _ in range(M):
    a, b, c = map(int, input().split())

    buildings[a].append((c, b))
    buildings[b].append((c, a))
    total += c

print(dijkstra(buildings, total))