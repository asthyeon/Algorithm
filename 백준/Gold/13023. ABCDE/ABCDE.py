import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# ABCDE (13023)
 1. 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E 가 존재하는지 구하기
  - A 는 B 와 친구다
  - B 는 C 와 친구다
  - C 는 D 와 친구다
  - D 는 E 와 친구다
[입력]
 1. N: 사람의 수, M: 친구 관계의 수
 2. M 개의 줄: a 와 b 가 친구다
[출력]
 1. 문제의 조건에 맞는 A, B, C, D, E 가 존재하면 1, 없으면 0 출력
"""

"""
<풀이>
 1. bfs -> 깊이를 설정하기 애매함 -> dfs
"""
from collections import deque


def dfs(now, level, friends, visited):
    # 조건을 만족한다면 종료
    if level == 5:
        print(1)
        exit()

    # 방문 처리 및 친구 탐색
    visited[now] = 1
    for new in friends[now]:
        # 방문하지 않았다면 다음 친구 탐색
        if not visited[new]:
            dfs(new, level + 1, friends, visited)
            # 새로운 관계를 찾아야 하기 때문에 이번 방문 초기화
            visited[new] = 0


N, M = map(int, input().split())
# 친구 관계
friends = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

# 친구 순회 -> 모든 사람들을 순회해야 함
for start in range(N):
    visited = [0] * N
    dfs(start, 1, friends, visited)

# 조건을 만족하는 관계가 없는 경우
print(0)