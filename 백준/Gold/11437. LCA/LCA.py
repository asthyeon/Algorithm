import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# LCA (11437)
 1. N개의 정점으로 이루어진 트리
 2. 루트는 1번
 3. 두 노드의 쌍 M개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상은?
[입력]
 1. N: 노드의 개수
 2. N - 1개의 줄: 트리 상에서 연결된 두 정점
 3. 그 다음 줄: 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M
 4. M개의 줄: 정점 쌍
[출력]
 1. M개의 줄에 두 정점의 가장 가까운 공통 조상 출력
"""

"""
<풀이>
 1. 트리
 2. LCA = 최소 공통 조상
 3. bfs로 각 노드의 공통 부모 찾기
"""
from collections import deque


# bfs
def bfs(tree, parents, depth):
    # 큐 및 방문 리스트
    q = deque([1])
    visited = [0] * (N + 1)

    while q:
        now = q.popleft()
        # 방문 체크
        visited[now] = 1
        # 자식 탐색
        for new in tree[now]:
            # 방문하지 않았다면
            if not visited[new]:
                # 부모 노드 설정
                parents[new] = now
                # 자식 인큐
                q.append(new)
                # 깊이 설정(부모 노드 + 1)
                depth[new] = depth[now] + 1


# 조상 탐색
def LCA(n1, n2):
    # 깊이가 다르다면 깊이를 맞춰주기
    while depth[n1] != depth[n2]:
        # 값이 큰 쪽을 부모 노드로 이동
        if depth[n1] > depth[n2]:
            n1 = parents[n1]
        else:
            n2 = parents[n2]

    # 깊이가 같다면 공통 조상 찾기
    while n1 != n2:
        n1 = parents[n1]
        n2 = parents[n2]

    # 공통 조상 반환
    return n1


N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    # 트리 연결
    tree[a].append(b)
    tree[b].append(a)

# 각 노드의 부모 노드
parents = [i for i in range(N + 1)]
# 각 노드의 깊이
depth = [0] * (N + 1)
# 각 노드의 부모 설정
bfs(tree, parents, depth)

M = int(input())
for _ in range(M):
    n1, n2 = map(int, input().split())

    # 공통 조상 찾기
    print(LCA(n1, n2))

