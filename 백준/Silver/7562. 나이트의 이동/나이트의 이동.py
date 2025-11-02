import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
<문제>
# 나이트의 이동 (7562)
1. 나이트가 최소 몇 번 만에 이동할 수 있는지?
<풀이>
1. bfs
"""
from collections import deque
# 나이트 이동 칸
knight = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

def bfs():
    # 초기 값 설정
    visited = [[0] * l for _ in range(l)]
    q = deque([(0, now_x, now_y)])
    visited[now_x][now_y] = 0

    while q:
        cnt, x, y = q.popleft()

        # 정답 칸 이동했을 때
        if x == target_x and y == target_y:
            return cnt

        # 나이트 이동
        for dx, dy in knight:
            nx, ny = x + dx, y + dy
            # 조건 만족시 이동
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = cnt + 1
                q.append((cnt + 1, nx, ny))


T = int(input())
for tc in range(1, T + 1):
    # l: 체스판 한 변의 길이
    l = int(input())
    # 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸
    now_x, now_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    print(bfs())
