import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] DFS와 BFS (1260)
1. DFS로 탐색한 결과와 BFS로 탐색한 결과 출력
2. 정점 번호가 작은 것을 먼저 방문, 더 이상 방문 불가능한 경우 종료

[풀이]
1. DFS/BFS
"""
from collections import deque


def dfs(graph, V):
    # 방문 리스트 및 시작점 방문 설정
    visited = [0] * (N + 1)
    q = [V]
    visited[V] = 1
    answer = [V]

    while q:
        # 현재 위치
        now = q[-1]

        for new in graph[now]:
            # 방문하지 않은 곳이라면 이동
            if not visited[new]:
                visited[new] = 1
                q.append(new)
                answer.append(new)
                break
        # 현재 단계에서 다 방문했다면 이전으로 이동
        else:
            if q:
                q.pop()

    return answer


def bfs(graph, V):
    # 방문 리스트 및 시작점 방문 설정
    visited = [0] * (N + 1)
    q = deque([V])
    visited[V] = 1
    answer = [V]

    while q:
        now = q.popleft()

        for new in graph[now]:
            # 방문하지 않은 곳이라면 방문
            if not visited[new]:
                visited[new] = 1
                q.append(new)
                answer.append(new)

    return answer


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# 오름차순 정렬
for g in graph:
    g.sort()

print(*dfs(graph, V))
print(*bfs(graph, V))