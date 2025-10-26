import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
<문제>
# DFS와 BFS
1. DFS로 탐색한 결과, BFS로 탐색한 결과 출력
 - 정점 번호가 작은 것을 먼저 방문
 - 더 이상 방문할 수 있는 점이 없는 경우 종료
 - 양방향 그래프
<풀이>
1. DFS, BFS
"""
from collections import deque


def dfs(graph, V):
    # 정점 순서 정렬(역방향) -> 정방향으로 탐색이 되게끔
    for i in range(1, N + 1):
        graph[i].sort(reverse=True)

    # 변수 및 시작점 설정
    visited = [0] * (N + 1)
    answer = []
    stack = [V]

    while stack:
        # 현재 방문 노드 처리
        now = stack.pop()
        if not visited[now]:
            answer.append(now)
            visited[now] = 1

            # 다음 방문 노드 처리
            for new in graph[now]:
                if not visited[new]:
                    stack.append(new)

    return answer


def bfs(graph, V):
    # 정점 순서 정렬(정방향)
    for i in range(1, N + 1):
        graph[i].sort()

    # 변수 및 시작점 설정
    visited = [0] * (N + 1)
    q = deque([V])
    answer = []
    visited[V] = 1

    while q:
        # 현재 방문 노드 처리
        now = q.popleft()
        answer.append(now)

        # 다음 방문 노드 처리
        for new in graph[now]:
            if not visited[new]:
                visited[new] = 1
                q.append(new)

    return answer


# 정점 수 N, 간선 수 M, 시작점 V
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(*dfs(graph, V))
print(*bfs(graph, V))