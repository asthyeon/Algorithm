import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 이분 그래프 (1701)
 1. 그래프가 주어졌을 때 이분 그래프인지 아닌지 판별하기
[입력]
 1. K: 테스트 케이스의 수
 2. V: 정점의 수, E: 간선의 수
 3. E개의 줄: 각 줄에 인접한 두 정점의 번호 u, v
[출력]
 1. K개의 줄에 걸쳐 주어진 그래프가 이분 그래프이면 YES, 아니면 NO 출력
"""

"""
<풀이>
 1. bfs
 2. 비연결 그래프도 생각하기
"""
from collections import deque


def bfs(graph):
    # 비연결 그래프를 고려하여 모든 정점에서 출발
    visited = [0] * (V + 1)
    for start in range(1, V + 1):
        if visited[start]:
            continue
        q = deque([start])
        visited[start] = 1

        while q:
            now = q.popleft()

            # 새로운 정점 탐색
            for new in graph[now]:
                # 방문하지 않았다면
                if not visited[new]:
                    # 반대의 숫자로 체크
                    if visited[now] == 1:
                        visited[new] = 2
                    else:
                        visited[new] = 1
                    q.append(new)

    # 모든 정점을 돌며 체크하기
    for now in range(1, V + 1):
        # 1일 때는 인접 정점이 2이어야 함
        if visited[now] == 1:
            for new in graph[now]:
                if visited[new] != 2:
                    return 'NO'
        # 2일 때는 인접 정점이 1이어야 함
        else:
            for new in graph[now]:
                if visited[new] != 1:
                    return 'NO'

    # 모두 돌았다면 이분 그래프
    return 'YES'


K = int(input())
for tc in range(1, K + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())

        graph[u].append(v)
        graph[v].append(u)

    print(bfs(graph))

