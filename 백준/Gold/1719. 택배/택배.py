import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 택배 (1719)
 1. 정점간의 간선은 두 집하장간에 화물 이동이 가능함
 2. 가중치는 이동에 걸리는 시간
 3. 경로표 만들기
  - 이 집하장에서 최단경로로 화물을 이동시키기 위해 가장 먼저 거쳐야 하는 집하장 나타내기
[입력]
 1. n: 집하장 개수, m: 집하장간 경로 개수
 2. 두 집하장의 번호와 그 사이를 오가는데 필요한 시간이 주어짐
[출력]
 1. 예시된 것과 같은 형식의 경로표 출력
"""

"""
<풀이>
 1. 다익스트라
 2. 각 정점간 최단 거리 구하기
"""
import heapq


# 다익스트라
def dijkstra(storage, start):
    visited = [0] * (n + 1)
    # 거리, 거쳐온 횟수, 현재 위치
    hq = [(0, 1, [start])]

    while hq:
        distance, cnt, now = heapq.heappop(hq)

        # 방문한 곳이라면 넘기기
        if visited[now[-1]]:
            continue

        # 방문 기록
        if start == now[-1]:
            visited[now[-1]] = '-'
        else:
            visited[now[-1]] = now[1]

        # 새로운 곳 방문
        for new in storage[now[-1]]:
            heapq.heappush(hq, (distance + new[1], cnt + 1, now + [new[0]]))

    return visited[1:]


n, m = map(int, input().split())
storage = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, dist = map(int, input().split())

    storage[a].append((b, dist))
    storage[b].append((a, dist))

# 정답 출력
for i in range(1, n + 1):
    print(*dijkstra(storage, i))