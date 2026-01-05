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
"""
from collections import deque


def bfs(K, start, graph, maximum):
    visited = [0] * (N + 1)
    q = deque([(maximum, start)])
    visited[start] = 1

    while q:
        now_cost, now = q.popleft()

        for new_cost, new in graph[now]:
            # 방문하지 않았다면
            if not visited[new]:
                # 더 작은 값으로 갱신, 다음 가중치도 더 작은 값
                next_cost = min(now_cost, new_cost)
                visited[new] = next_cost
                q.append((next_cost, new))

    # 정답 세기
    answer = 0
    for i in range(1, N + 1):
        # 자기자신이 아닐 때만
        if i != start:
            # USADO가 K보다 크거나 같다면 카운트
            if visited[i] >= K:
                answer += 1
    return answer



N, Q = map(int, input().split())
# 그래프 연결 및 최댓값 저장
graph = [[] for _ in range(N + 1)]
maximum = 0
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((r, q))
    graph[q].append((r, p))
    # 최댓값 갱신
    maximum = max(maximum, r)

# K = k일 때, v를 보고 있는 소들에게 몇 개의 동영상이 추천?
for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(k, v, graph, maximum))