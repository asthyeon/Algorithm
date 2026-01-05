import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] MooTube (Silver) (15591)
1. USADO: 간선 가중치
2. USADO가 정해지지 않은 정점끼리는 연결된 경로를 지나는 USADO 값중 최솟값
3. K 값 이상인 경로를 찾기

[풀이]
1. bfs
2. 가중치가 K 이상인 간선만 이동해보기
"""
from collections import deque


def bfs(K, start, graph):
    visited = [0] * (N + 1)
    q = deque([start])
    visited[start] = 1

    answer = 0
    while q:
        now = q.popleft()

        for cost, new in graph[now]:
            # 방문하지 않고, 가중치가 K 이상이라면
            if not visited[new] and cost >= K:
                # 방문 처리 후 정답 세기
                visited[new] = 1
                answer += 1
                q.append(new)

    return answer



N, Q = map(int, input().split())
# 그래프 연결
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((r, q))
    graph[q].append((r, p))


# K = k일 때, v를 보고 있는 소들에게 몇 개의 동영상이 추천?
for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(k, v, graph))