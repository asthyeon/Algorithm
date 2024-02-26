import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 연구소(14502)
 1. 연구소는 크기가 NxM인 직사각형
  - 0: 빈 칸, 1: 벽, 2: 바이러스
 2. 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있음
 3. 새로 3개의 벽을 세워야 함
 4. 바이러스가 퍼질 수 없는 곳은 안전 영역(0 인 칸)
 5. 안전 영역 크기의 최댓값 구하기
[입력]
 1. N: 세로, M: 가로
 2. N개의 줄: 지도의 모양
[출력]
 1. 얻을 수 있는 안전 영역의 최대 크기 출력
"""

"""
<풀이>
 1. 브루트 포스로 풀어보기
"""
from collections import deque


# 벽 설치 및 안전영역 체크
def construct(wall):
    global answer
    if wall < 3:
        # 벽 설치
        for x in range(N):
            for y in range(M):
                if laboratory[x][y] == 0:
                    laboratory[x][y] = 1
                    construct(wall + 1)
                    laboratory[x][y] = 0

    # 벽이 설치 되었다면
    else:
        # 연구소 복사
        laboratory_copy = [lab[:] for lab in laboratory]

        # 바이러스 찾은 경우 델타탐색
        for sx in range(N):
            for sy in range(M):
                if laboratory_copy[sx][sy] == 2:
                    q = deque([(sx, sy)])

                    while q:
                        x, y = q.popleft()

                        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < N and 0 <= ny < M:
                                if laboratory_copy[nx][ny] == 0:
                                    laboratory_copy[nx][ny] = 2
                                    q.append((nx, ny))

        # 안전지대 찾기
        safety = 0
        for x in range(N):
            for y in range(M):
                if laboratory_copy[x][y] == 0:
                    safety += 1

        answer = max(answer, safety)


# 세로 N, 가로 M
N, M = map(int, input().split())
# 연구소 지도
laboratory = [list(map(int, input().split())) for _ in range(N)]
# 정답 영역
answer = 0
# 벽 설치
construct(0)

print(answer)







