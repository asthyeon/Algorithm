import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 치킨 배달 (15686)
 1. 치킨 거리: 집과 가장 가까운 치킨집 사이의 거리
 2. 도시의 치킨 거리는 모든 집의 치킨 거리의 합
 3. 치킨집 중 최대 M개를 고르고, 도시의 치킨 거리가 가장 작게 될지 구하기
[입력]
 1. N: 도시의 크기, M: 최대 치킨집 수
 2. N개의 줄: 도시의 정보(0: 빈 칸, 1: 집, 2: 치킨집)
[출력]
 1. 도시의 치킨 거리의 최솟값 출력
"""

"""
<풀이>
 1. M개 치킨집이 뽑히는 경우의 수를 이용
"""
from itertools import combinations
from collections import deque


def bfs(case, houses):
    global answer
    visited = [[-1] * N for _ in range(N)]
    q = deque(case)

    # 치킨집 초기화
    for sx, sy in case:
        visited[sx][sy] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    # 이번 경우의 거리합
    distance = 0
    for hx, hy in houses:
        distance += visited[hx][hy]
    return distance


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 치킨집, 집 위치 저장
stores = []
houses = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            stores.append((i, j))
# 치킨집 경우의 수
cases = list(combinations(stores, M))

# 도시의 치킨 거리의 최솟값
answer = 10e9
for case in cases:
    answer = min(answer, bfs(case, houses))

print(answer)