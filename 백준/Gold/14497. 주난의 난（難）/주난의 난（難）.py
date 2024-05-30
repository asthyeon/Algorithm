import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 주난의 난(難) (14497)
 1. 주난이의 한 번의 점프는 상하좌우 4방향으로 한 겹의 친구들을 쓰러뜨림
 2. 초코바를 가진 학생을 찾을 때까지 점프함
[입력]
 1. N, M: 교실의 크기
 2. x1, y1: 주난이 위치, x2, y2: 초코바 범인 위치
 3. 이후 N x M 크기의 교실 정보
  - 0: 빈 공간, 1: 친구, *: 주난, #: 범인
[출력]
 1. 범인을 잡기 위해 최소 몇 번의 점프를 해야 하는지?
"""

"""
<풀이>
 1. bfs
"""
import heapq

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(classroom, x1, y1, x2, y2):
    # 방문 리스트 생성
    visited = [[0] * (M + 1) for _ in range(N)]
    # 점프 횟수, 주난이 위치 시작 및 방문 기록
    hq = [(0, x1 - 1, y1 - 1)]
    visited[x1 - 1][y1 - 1] = 1

    while hq:
        cnt, x, y = heapq.heappop(hq)

        # 델타 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 벽 형성
            if 0 <= nx < N and 0 <= ny < M:
                # 방문하지 않았을 시 방문
                if not visited[nx][ny]:
                    # 방문 기록
                    visited[nx][ny] = 1
                    # 친구를 만났을 때
                    if classroom[nx][ny] == '1':
                        heapq.heappush(hq, (cnt + 1, nx, ny))
                    # 빈 공간일 때
                    elif classroom[nx][ny] == '0':
                        heapq.heappush(hq, (cnt, nx, ny))
                    # 범인일 때
                    else:
                        return cnt + 1


N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
classroom = [list(input().rstrip()) for _ in range(N)]

print(bfs(classroom, x1, y1, x2, y2))