import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 등수 찾기 (17616)
 1. 두 학생 A, B가 대회 본부에 찾아가면 두 학생 중 어느 학생이 더 잘했는 지 알려줌
[입력]
 1. N: 학생 수, M: 질문 수, X: 등수를 알고 싶은 학생
 2. M 개의 줄: 학생 A 가 학생 B 보다 더 잘했음
[출력]
 1. U: 학생 X 의 가능한 가장 높은 등수, V: 가능한 가장 낮은 등수
"""

"""
<풀이>
 1. bfs -> 아래에서 위방향, 위에서 아래방향 풀기
"""
from collections import deque


def bfs(rank, direction):
    # 큐 생성 및 방문 처리
    q = deque([X])
    visited = [0] * (N + 1)
    visited[X] = 1
    # 밀리는 등수
    grade = 0

    while q:
        now = q.popleft()

        # 방향에 따라 탐색
        for new in rank[now][direction]:
            if not visited[new]:
                visited[new] = 1
                q.append(new)
                # 등수가 밀릴 때마다 + 1
                grade += 1

    return grade


N, M, X = map(int, input().split())
# 등수 매기기 [높은 등수, 낮은 등수]
rank = [[[], []] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())

    rank[A][1].append(B)
    rank[B][0].append(A)

# 가능한 가장 높은 등수 (아래 -> 위)
U = bfs(rank, 0) + 1
# 가능한 가장 낮은 등수 위 -> 아래
V = N - bfs(rank, 1)

print(U, V)