import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque


def MST(start, graph, visited):
    global cnt
    cnt += 1
    visited[start] = 1
    q = deque([start])

    while q:
        now = q.popleft()

        for new in graph[now]:
            if not visited[new]:
                visited[new] = 1
                q.append(new)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)
cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        MST(i, graph, visited)

print(cnt)