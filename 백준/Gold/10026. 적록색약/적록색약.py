import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 적록색약 (10026)
 1. 구역은 같은 색으로 이루어져 있음
 2. 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속함
 3. 적록색약은 빨간색과 초록색의 차이를 느끼지 못함
[입력]
 1. N: 크기
 2. N개의 줄: 그림의 정보
[출력]
 1. 적록색약이 아닌 사람이 봤을 때의 구역의 개수, 적록색약인 사람이 봤을 때의 구역의 수 출력
"""

"""
<풀이>
 1. bfs
"""


# 적록색약이 아닌 사람
def colorful(painting):
    # 방문 리스트, 구역 수
    visited = [[0] * N for _ in range(N)]
    zone = 0

    # 시작 색상 정하기
    for sx in range(N):
        for sy in range(N):
            if not visited[sx][sy]:
                color = painting[sx][sy]
                q = [(sx, sy)]
                visited[sx][sy] = 1
                zone += 1

                # bfs
                while q:
                    x, y = q.pop()

                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            # 같은 색상만 한 구역으로 인식
                            if color == painting[nx][ny]:
                                visited[nx][ny] = 1
                                q.append((nx, ny))

    return zone


# 적록색약인 사람
def not_colorful(painting):
    # 방문 리스트, 구역 수
    visited = [[0] * N for _ in range(N)]
    zone = 0

    # 시작 색상 정하기
    for sx in range(N):
        for sy in range(N):
            if not visited[sx][sy]:
                color = painting[sx][sy]
                q = [(sx, sy)]
                visited[sx][sy] = 1
                zone += 1

                # bfs
                while q:
                    x, y = q.pop()

                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            # 같은 색상일 때
                            if color == painting[nx][ny]:
                                visited[nx][ny] = 1
                                q.append((nx, ny))
                            # 빨간색일 땐 초록색 포함
                            elif color == 'R':
                                if painting[nx][ny] == 'G':
                                    visited[nx][ny] = 1
                                    q.append((nx, ny))
                            # 초록색일 땐 빨간색 포함
                            elif color == 'G':
                                if painting[nx][ny] == 'R':
                                    visited[nx][ny] = 1
                                    q.append((nx, ny))

    return zone


N = int(input())
painting = [list(input().rstrip()) for _ in range(N)]

print(colorful(painting), not_colorful(painting))