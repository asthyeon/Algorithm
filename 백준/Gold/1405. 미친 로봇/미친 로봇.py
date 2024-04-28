import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 미친 로봇 (1405)
 1. 로봇은 N번의 행동에서 4개의 방향 중 하나로 한 칸 이동
 2. 이동 경로가 단순 = 로봇이 같은 곳을 한 번보다 많이 이동하지 않을 때
 3. 같은 방향이 아닌 같은 위치를 말하는 것
[입력]
 1. N: 행동 수, 동쪽 / 서쪽 / 남쪽 / 북쪽 이동할 확률
[출력]
 1. 로봇의 이동 경로가 단순한 확률
"""

"""
<풀이>
 1. 일단 풀어보기 -> 백트래킹
"""
sys.setrecursionlimit(10**9)
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 백트래킹(x, y, 이동 수, 현재 확률)
def back_tracking(x, y, cnt, now_percent):
    global total_percent

    # 이동 수가 다되면 확률 더하기
    if cnt == N:
        total_percent += now_percent
        return

    # 델타 탐색
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]

        # 방문하지 않았을 때
        if not visited[nx][ny]:
            # 방문 처리
            visited[nx][ny] = 1
            # 재귀
            back_tracking(nx, ny, cnt + 1, now_percent * directions[dir])
            # 방문 취소
            visited[nx][ny] = 0


# 행동 수 N, 동쪽 / 서쪽/ 남쪽/ 북쪽 이동할 확률
N, east, west, south, north = map(int, input().split())
# 총 확률
total_percent = 0
# 방향 인덱스(동서남북)
directions = [east / 100, west / 100, south / 100, north / 100]
# 방문 기록(N만큼은 뻗어나갈 수 있어야 함)
visited = [[0] * (N * 2 + 1) for _ in range(N * 2 + 1)]
# 시작점 방문
visited[N][N] = 1

back_tracking(N, N, 0, 1)

print(total_percent)