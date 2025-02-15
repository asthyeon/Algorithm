import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def bfs(graph, start):
    global answer
    q = deque([(1, start)])
    visited = [0] * (N + 1)
    visited[start] = 1
    connection = 0

    while q:
        cnt, now = q.popleft()

        for new in graph[now]:
            if not visited[new]:
                visited[new] = 1
                q.append((cnt + 1, new))
                connection += cnt

    return connection


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

answer = 0
connections = 100 * 5000
for start in range(1, N + 1):
    temp = bfs(graph, start)
    if connections > temp:
        answer = start
        connections = temp

print(answer)