import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 경쟁적 전염 (18405)
 1. 모든 바이러스는 1초마다 상, 하, 좌, 우 방향으로 증식
 2. 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식
 3. 이미 바이러스가 존재하는 칸에는 다른 바이러스가 들어갈 수 없음
[입력]
 1. N: 시험관 크기, K: 바이러스 종류 수
 2. N개의 줄: 시험관 정보
 3. S초가 지난 후에 (X, Y)에 존재하는 바이러스의 종류
[출력]
 1. 조건 바이러스 출력, 바이러스 없다면 0 출력
"""

"""
<풀이>
 1. bfs, 우선순위큐
"""
import heapq


def bfs(examiner):
    hq = []
    # 초기 바이러스 인큐
    for sx in range(N):
        for sy in range(N):
            if examiner[sx][sy] > 0:
                heapq.heappush(hq, (0, examiner[sx][sy], sx, sy))

    while hq:
        second, virus, x, y = heapq.heappop(hq)

        # 시간이 다되면 종료
        if second == S:
            return examiner[X - 1][Y - 1]

        # 델타탐색
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if examiner[nx][ny] == 0:
                    examiner[nx][ny] = virus
                    heapq.heappush(hq, (second + 1, virus, nx, ny))

    # 바이러스 증식 완료시 종료
    return examiner[X - 1][Y - 1]


N, K = map(int, input().split())
examiner = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

print(bfs(examiner))