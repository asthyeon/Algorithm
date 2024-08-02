import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 귀찮은 해강이 (24391)
 1. 강의 시간표 순서대로 모든 강의를 들으며 한 건물에서 밖으로 나오는 횟수 최소화
[입력]
 1. N: 강의의 개수, M: 건물의 쌍의 개수
 2. M개의 줄: i번 건물과 j번 건물이 연결되어 있음
 3. A: N갱의 강의코드가 시간표 순서대로 주어짐
[출력]
 1. 해강이가 밖에 나와야 하는 최소 횟수
"""

"""
<풀이>
 1. bfs
"""
from collections import deque


# bfs
def bfs(building, connection, start):
    # 방문한 경우 넘기기
    if visited[start]:
        return
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()

        for new in building[now]:
            # 방문하지 않은 경우
            if not visited[new]:
                q.append(new)
                visited[new] = 1
                # 같은 그룹으로 묶기
                connection[new] = start


N, M = map(int, input().split())
# 건물 연결
building = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    building[i].append(j)
    building[j].append(i)
A = list(map(int, input().split()))

# 그룹 연결하기
connection = [i for i in range(N + 1)]
visited = [0] * (N + 1)
for start in range(1, N + 1):
    bfs(building, connection, start)

# 건물 옮겨다니기
cnt = 0
now = 0
for a in A:
    # 첫 출발시에는 카운트 X
    if now == 0:
        now = a

    # 연결되지 않은 곳이라면 카운트 후 위치 변경
    if connection[a] != connection[now]:
        now = connection[a]
        cnt += 1

print(cnt)
