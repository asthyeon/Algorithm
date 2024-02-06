import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 숨바꼭질(6118)
 1. 재서기는 농장의 헛간에 숨어야 함
 2. 헛간은 양방향 길로 언제나 다른 헛간으로 도달 가능
 3. 최대한 멀리 숨을 수 있는 헛간 찾기
[입력]
 1. N: 헛간의 개수, M: 헛간에 연결된 양방향 길의 개수
 2. M줄에 걸쳐서 A: 헛간 길 시작점, B: 헛간 길 도착점
[출력]
 1. 숨어야 하는 헛간 번호(여러 개라면 가장 작은 번호), 헛간까지의 거리, 같은 거리를 갖는 개수
"""

"""
<풀이>
 1. bfs로 거리 계산하기
 2. 덱 사용
"""
from collections import deque

INF = 10e9


# bfs
def bfs(barns):
    # 시작점(거리, 위치) 인큐 및 방문 기록
    q = deque([(0, 1)])
    visited = [-1] * (N + 1)
    visited[1] = 0

    while q:
        dist, now = q.popleft()

        # 다음 위치 탐색
        for new in barns[now]:
            new_dist = dist + 1

            # 방문하지 않은 곳이라면 방문
            if visited[new] == -1:
                visited[new] = new_dist
                q.append((new_dist, new))

    # 가장 긴 거리
    distance = max(visited)
    # 가장 긴 거리 중 가장 가까운 헛간
    barn = visited.index(distance)
    # 가장 긴 거리의 개수
    cnt = visited.count(distance)

    return barn, distance, cnt


# 헛간의 개수 N, 양방향 길의 개수 M
N, M = map(int, input().split())
# 헛간 정보
barns = [[] for _ in range(N + 1)]

# 양방향 길 연결
for _ in range(M):
    start, end = map(int, input().split())

    barns[start].append(end)
    barns[end].append(start)

print(*bfs(barns))