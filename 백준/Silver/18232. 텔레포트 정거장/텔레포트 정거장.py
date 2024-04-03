import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 텔레포트 정거장 (18232)
 1. 점 S -> 점 E
 2. 텔레포트 가능: X + 1 or X - 1 or X에 위치한 텔레포트와 연결된 지점으로 이동 가능
[입력]
 1. N: 점 길이, M: 텔레포트 위치 수
 2. S: 주예 위치, E: 목표 위치
 3. M개의 줄: x와 y가 텔레포트가 연결되어 있음
[출력]
 1. S에서 E 도달하는 최소 시간
"""

"""
<풀이>
 1. bfs
 2. 같은 위치에 여러 개의 텔레포트가 존재할 수 있음
"""
from collections import deque


# bfs
def bfs(locations, S, E):
    # 큐 형성 및 시간과 위치 인큐
    q = deque([(0, S)])
    # 방문 리스트 및 기록
    visited = [0] * (N + 1)
    visited[S] = 1

    while q:
        time, now = q.popleft()

        if now == E:
            return time

        # 우측 이동
        if now + 1 <= N:
            if not visited[now + 1]:
                visited[now + 1] = 1
                q.append((time + 1, now + 1))

        # 좌측 이동
        if now - 1 >= 1:
            if not visited[now - 1]:
                visited[now - 1] = 1
                q.append((time + 1, now - 1))

        # 텔레포트 이용
        if locations[now]:
            for teleport in locations[now]:
                if not visited[teleport]:
                    visited[teleport] = 1
                    q.append((time + 1, teleport))


N, M = map(int, input().split())
S, E = map(int, input().split())
# 위치 정보
locations = [[] for _ in range(N + 1)]
# 텔레포트 정보
for _ in range(M):
    x, y = map(int, input().split())
    locations[x].append(y)
    locations[y].append(x)

print(bfs(locations, S, E))