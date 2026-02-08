import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 트리의 지름 (1967]
1. 트리는 사이클이 없는 무방향 그래프
2. 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재
3. 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때 가장 길게 늘어나는 경우 구하기
4. 루트 노드는 1
5. 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력됨

[풀이]
1. 다익스트라
"""
from collections import deque


def dijkstra(tree, start):
    distances = [10**9] * (n + 1)
    q = deque([(start, 0)])
    distances[start] = 0

    while q:
        now, now_weight = q.popleft()

        # 다음 노드 탐색
        for new, new_weight in tree[now]:
            total_weight = now_weight + new_weight
            # 다음 방문을 더 적은 값으로 방문한다면 방문
            if distances[new] > total_weight:
                q.append((new, total_weight))
                distances[new] = total_weight

    # 가장 긴 지름 반환
    return max(distances[1:])


n = int(input())
# 트리 연결
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

# 모든 간선 간의 거리 구하기
answer = 0
for start in range(1, n + 1):
    # 정답 교체
    answer = max(answer, dijkstra(tree, start))

print(answer)