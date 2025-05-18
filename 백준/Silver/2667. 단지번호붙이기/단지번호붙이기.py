import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 단지번호붙이기 (2667)
1. bfs
"""
from collections import deque


def bfs(houses):
    visited = [[0] * N for _ in range(N)]
    answers = []

    # 전 지역 탐색
    for sx in range(N):
        for sy in range(N):
            if houses[sx][sy] == 1 and not visited[sx][sy]:
                visited[sx][sy] = 1
                q = deque([(sx, sy)])
                answer = 1

                # bfs
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and houses[nx][ny] == 1 and not visited[nx][ny]:
                            answer += 1
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                answers.append(answer)

    print(len(answers))
    answers.sort()
    for ans in answers:
        print(ans)


# 단지 정보
N = int(input())
houses = [list(map(int, list(input().rstrip()))) for _ in range(N)]

bfs(houses)