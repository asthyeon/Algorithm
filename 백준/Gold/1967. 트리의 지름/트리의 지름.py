import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 트리의 지름 (1967)
 1. 트리에서 어떤 두 노드를 선택해 양쪽으로 쫙 당길 때 가장 길게 늘어나는 경우가 있음
  - 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 됨
  - 이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 함
 2. 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이 = 트리의 지름
[입력]
 1. n: 노드의 개수
 2. n - 1 개의 줄: 부모 노드, 자식 노드, 간선의 가중치
 3. 루트의 노드 번호는 항상 1
[출력]
 1. 트리의 지름 출력
"""

"""
<풀이>
 1. bfs
"""
from collections import deque


def bfs(tree, start):
    # 가장 큰 지름과 노드 번호
    diameter = 0
    node = 0

    # 끝 노드부터 시작
    q = deque([(0, start)])
    visited = [0] * (n + 1)
    visited[start] = 1

    while q:
        dist, now = q.popleft()

        # 새로운 노드 탐색
        for new_dist, new in tree[now]:
            if not visited[new]:
                visited[new] = 1
                q.append((dist + new_dist, new))

                # 거리 갱신
                if diameter < dist + new_dist:
                    diameter = dist + new_dist
                    node = new

    return diameter, node


n = int(input())
# 트리 만들기
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    parent, child, weight = map(int, input().split())

    # 양방향
    tree[child].append((weight, parent))
    tree[parent].append((weight, child))

# 루트 노드에서 가장 먼 노드 찾아 시작할 노드로 지정
_, start_node = bfs(tree, 1)

# 가장 먼 노드에서 지름 구하기
answer, far_node = bfs(tree, start_node)

print(answer)