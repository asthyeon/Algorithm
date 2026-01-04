import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 알고리즘 수업 - 너비 우선 탐색 1 (24444)
1. bfs로 풀기
2. 정점은 오름차순 방문

[풀이]
1. bfs
"""
from collections import deque


# sudo 코드로 구현한 bfs
def bfs(visited, graph, R):
    # 시작점 방문 및 방문 순서 갱신
    turn = 1
    visited[R] = turn
    turn += 1
    q = deque([R])

    # bfs 로직
    while q:
        now = q.popleft()
        for new in graph[now]:
            if not visited[new]:
                visited[new] = turn
                turn += 1
                q.append(new)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 오름차순 방문을 위한 정렬
for g in graph:
    g.sort()

# bfs
visited = [0] * (N + 1)
bfs(visited, graph, R)

# 정답 출력
for i in range(1, N + 1):
    print(visited[i])