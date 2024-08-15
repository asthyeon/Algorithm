import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 소셜 네트워킹 어플리케이션 (7511)
 1. 친구 관계 그래프 만들기
 2. 한 사람이 다른 사람 방문했을 때 친구 관계 그래프에서 두 사람 사이의 경로를 보여주기
 3. 경로가 없는 경우 보여주지 않음
[입력]
 1. 첫째 줄: 테스트케이스 수
 2. n: 유저의 수
 3. k: 친구 관계의 수
 4. k개의 줄: a와 b는 친구
 5. m: 미리 구할 쌍의 수
 6. m개의 줄: 구해야하는 쌍 u, v
[출력]
 1. 각 테스트 케이스마다 "Scenario i:" 출력
 2. i는 테스트 케이스 번호 출력
 3. 각각의 쌍마다 두 사람을 연결하는 경로가 있으면 1, 없으면 0
"""

"""
<풀이>
 1. 그래프
"""
from collections import deque


# 친구관계 연결
def bfs(friends, connections, visited, start):
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()

        for new in friends[now]:
            if not visited[new]:
                connections[new] = start
                visited[new] = 1
                q.append(new)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    k = int(input())
    # 친구관계
    friends = [[] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)

    # 친구관계 연결도 및 방문리스트
    connections = [i for i in range(n)]
    visited = [0] * n
    # 친구관계 연결
    for start in range(n):
        if not visited[start]:
            bfs(friends, connections, visited, start)

    # 시나리오 출력
    print(f'Scenario {tc}:')
    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())

        # 정답 출력
        if connections[u] == connections[v]:
            print(1)
        else:
            print(0)
    print()