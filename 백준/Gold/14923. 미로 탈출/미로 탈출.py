import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 미로 탈출(14923)
 1. N x M 미로 
  - 시작 위치: (Hx, Hy)
  - 탈출 위치: (Ex, Ey)
 2. 미로 곳곳에 벽 위치
 3. 단 한번 벽을 길로 만들 수 있음
 4. 미로 탈출할 수 있는지 알아보고, 할 수 있다면 가장 빠른 경로의 거리 구하기
[입력]
 1. N, M: 미로 크기
 2. Hx, Hy: 홍익이 시작 위치
 3. Ex, Ey: 탈출 위치
 4. 미로 정보
[출력]
 1. 가장 빠른 경로의 거리 D 출력
 2. 탈출할 수 없다면 -1 출력 
"""

"""
<풀이>
 1. 다익스트라
 2. 벽을 부수지 않고 움직일 때와 부수고 움직일 때를 고려해보기
"""
import heapq

# 최장거리
INF = 10e9


# 다익스트라
def dijkstra(maze):
    # 벽을 부수는 경우를 고려하기 위한 3차원 배열
    distances = [[[INF] * 2 for _ in range(M)] for _ in range(N)]

    # 힙큐 생성 및 거리와 시작점, 파괴 여부 인큐
    hq = [(0, Hx - 1, Hy - 1, 0)]
    distances[0][0] = [0, 0]

    while hq:
        dist, x, y, destroy = heapq.heappop(hq)

        # 델타탐색
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            # 벽 형성
            if 0 <= nx < N and 0 <= ny < M:
                # 해당 위치가 탈출 위치라면 종료
                if nx == Ex - 1 and ny == Ey - 1:
                    return dist + 1

                # 다음 위치가 통로이고 이동한 거리 + 1 보다 길게 방문했다면 방문
                if maze[nx][ny] == 0 and distances[nx][ny][destroy] > dist + 1:
                    distances[nx][ny][destroy] = dist + 1
                    heapq.heappush(hq, (dist + 1, nx, ny, destroy))

                # 다음 위치가 벽일 때 벽을 부순 적이 없다면 벽을 부수고 방문
                elif maze[nx][ny] == 1 and not destroy:
                    distances[nx][ny][destroy + 1] = dist + 1
                    heapq.heappush(hq, (dist + 1, nx, ny, destroy + 1))

    # 탈출하지 못하는 경우
    return -1


# 세로 N, 가로 M
N, M = map(int, input().split())
# 시작 위치
Hx, Hy = map(int, input().split())
# 탈출 위치
Ex, Ey = map(int, input().split())
# 미로 정보
maze = [list(map(int, input().split())) for _ in range(N)]

print(dijkstra(maze))