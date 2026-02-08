import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 트리의 부모 찾기 (11725)
1. 루트 없는 투리가 주어짐
2. 트리의 루트를 1이라고 했을 때, 각 노드의 부모를 구하기

[풀이]
1. bfs -> 루트에서 탐색하기(이전 방문 노드가 부모)
"""
from collections import deque


def bfs(graph):
    visited = [0] * (N + 1)
    q = deque([1])
    visited[1] = 1

    while q:
        now = q.popleft()
        
        # 다음 방문 노드 탐색
        for new in graph[now]:
            if not visited[new]:
                # 다음 방문 노드의 부모 노드
                visited[new] = now
                q.append(new)

    for i in range(2, N + 1):
        print(visited[i])


N = int(input())
# 그래프 연결
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

# 루트에서 탐색
bfs(graph)

