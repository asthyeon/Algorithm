import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 그대, 그머가 되어 (14496)
 1. 치환하기
 2. (a, b), (a, c), (b, d), (c, d)가 주어지는 경우
  - a -> d: a-b-d, a-c-d
 3. (a, b), (b, c), (a, c)가 주어지는 경우
  - a -> c: a-b-c, a-c (치환횟수 차이 발생)
[입력]
 1. a, b: a -> b로 바꾸기
 2. N: 전체 문자의 수, M: 치환 가능한 문자쌍의 수
 3. M개의 줄: 치환 가능한 문자쌍
[출력]
 1. 최소 치환 횟수 출력(불가능할시 -1 출력)
"""

"""
<풀이>
 1. bfs
"""
from collections import deque


# bfs
def bfs(locations, a, b):
    visited = [0] * (N + 1)
    q = deque([(0, a)])
    visited[a] = 1

    while q:
        cnt, now = q.popleft()

        # 치환 가능시 현재 횟수 출력
        if now == b:
            return cnt

        # 다음 장소 탐색
        for new in locations[now]:
            if not visited[new]:
                visited[new] = 1
                q.append((cnt + 1, new))

    # 치환이 불가능한 경우
    return -1


# a -> b 치환하기
a, b = map(int, input().split())
# 전체 문자의 수 N, 치환 가능한 문자쌍의 수 M
N, M = map(int, input().split())
# 위치 리스트
locations = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    locations[x].append(y)
    locations[y].append(x)

print(bfs(locations, a, b))