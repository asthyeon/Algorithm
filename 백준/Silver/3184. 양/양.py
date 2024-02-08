import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 양
 1. 마당에는 양과 늑대가 있음
  - '.': 빈 필드, '#': 울타리, 'o': 양, 'v': 늑대
 2. 수평, 수직으로 울타리를 지나지 않고 이동 가능시 두 칸은 같은 영역
 3. 탈출가능한 칸 존재 X
 4. 양 > 늑대: 양 win, 양 <= 늑대: 늑대 win
[입력]
 1. 세로 R, 가로 C
 2. 마당 정보
[출력]
 1. 아침까지 살아있는 양과 늑대의 수 출력
"""

"""
<풀이>
 1. bfs로 탐색
 2. 울타리가 아닌 지역에 진입시 양과 늑대 카운트하기
"""
from collections import deque


# bfs
def bfs(yard):
    # 방문 리스트
    visited = [[0] * C for _ in range(R)]

    # 전체 양과 늑대
    sheep = 0
    wolves = 0

    # 전체 탐색
    for sx in range(R):
        for sy in range(C):
            # 울타리가 아니고 방문하지 않은 지역이라면
            if yard[sx][sy] != '#' and visited[sx][sy] == 0:

                # 이번 회차의 양과 늑대
                O, V = 0, 0

                # 시작점 인큐 및 방문 기록
                q = deque([(sx, sy)])
                visited[sx][sy] = 1

                # 양과 늑대 카운트
                if yard[sx][sy] == 'o':
                    O += 1
                elif yard[sx][sy] == 'v':
                    V += 1

                while q:
                    x, y = q.popleft()

                    # 델타 탐색
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        # 벽 형성
                        if 0 <= nx < R and 0 <= ny < C:
                            # 방문하지 않은 지역이라면
                            if visited[nx][ny] == 0:
                                # 울타리가 아니라면 이동
                                if yard[nx][ny] != '#':
                                    q.append((nx, ny))
                                    visited[nx][ny] = 1

                                    # 양과 늑대 카운트
                                    if yard[nx][ny] == 'o':
                                        O += 1
                                    elif yard[nx][ny] == 'v':
                                        V += 1

                # 살아남는 개체 카운트
                if O > V:
                    sheep += O
                else:
                    wolves += V

    return sheep, wolves


# 세로 R, 가로 C
R, C = map(int, input().split())

# 마당 정보
yard = [list(input().rstrip()) for _ in range(R)]

print(*bfs(yard))