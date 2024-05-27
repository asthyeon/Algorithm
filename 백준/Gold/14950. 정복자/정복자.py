import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 정복자 (14950)
 1. 처음 점거하고 있는 도시는 1번 도시
 2. 특정 도시 B를 정복하고 싶다면, B와 연결된 도시들 중 적어도 하나 정복해 있어야 함
 3. 정복하는 과정에서 조건을 만족하는 도시와 연결된 도로 비용 소모
 4. 한 번 도시가 정복되면, 모든 도로의 비용이 t만큼 증가하게 됨
[입력]
 1. N: 도시 수, M: 도로 수, t: 정복시 증가하는 도로 비용
 2. M개의 줄: A와 B 사이에 비용이 C인 도로가 존재
[출력]
 1. 모든 도시를 정복하는데 사용되는 최소 비용 출력
"""

"""
<풀이>
 1. 다익스트라
"""
import heapq


def dijkstra(cities):
    visited = [0] * (N + 1)
    hq = [(0, 1)]
    # 총 비용
    total = 0
    # 정복 수
    cnt = -1

    while hq:
        cost, loc = heapq.heappop(hq)
        
        # 방문 시 스킵
        if visited[loc]:
            continue
        # 정복한 횟수만큼 비용 더하기
        if cnt >= 1:
            total += t * cnt

        cnt += 1
        visited[loc] = 1
        total += cost
        
        # 방문하지 않은 곳 탐색
        for new in cities[loc]:
            new_loc = new[1]
            new_cost = new[0]
            heapq.heappush(hq, (new_cost, new_loc))

    return total


N, M, t = map(int, input().split())
cities = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    
    # 양방향
    cities[A].append((C, B))
    cities[B].append((C, A))

print(dijkstra(cities))