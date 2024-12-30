import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 편세권 (31849)
 1. 방을 고르는 기준: 월세와 편의점까지의 거리
 2. 편세권 점수가 가장 낮은 집을 고르기
  - 편세권 점수 = (방에서 가장 가까운 편의점까지의 거리) X (월세)
 3. 방의 위치가 (a, b), 편의점의 위치가 (c, d)일 때,
  - 방에서 편의점까지의 거리: |a - c| + |b - d|
[입력]
 1. N, M: 지도의 크기, R: 방의 개수, C: 편의점의 개수
 2. R개의 줄: i번째 방이 (a, b)에 있으며, 월세가 p
 3. C개의 줄: j번째 편의점이 (c, d)에 있음
 4. 한 위치에는 최대 한 개의 방이나 한 개의 편의점만 존재
[출력]
 1. 현성이가 고른 방의 편세권 점수 출력
"""

"""
<풀이>
 1. bfs -> 모든 집에서 가장 가까운 편의점을 찾기 -> 시간초과
 2. 모든 편의점을 q에 넣고 각 지점에서 모든 격자까지의 거리를 구해놓기
"""
from collections import deque


def bfs(visited, houses, q):
    # 편의점들로부터 각 격자 위치 최소 거리 구하기
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 1 <= nx < N + 1 and 1 <= ny < M + 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    # 각 집으로부터 편세권 점수 구하기
    answer = 10e9
    for a, b, p in houses:
        score = visited[a][b] * p
        # 정답 갱신
        answer = min(answer, score)

    return answer


N, M, R, C = map(int, input().split())
# 방문 리스트
visited = [[-1] * (M + 1) for _ in range(N + 1)]
houses = []
q = deque()
# 집 위치들
for i in range(R):
    a, b, p = map(int, input().split())
    houses.append((a, b, p))
# 편의점 위치들 인큐
for j in range(C):
    c, d = map(int, input().split())
    q.append((c, d))
    # 편의점 거리 초기화
    visited[c][d] = 0

print(bfs(visited, houses, q))