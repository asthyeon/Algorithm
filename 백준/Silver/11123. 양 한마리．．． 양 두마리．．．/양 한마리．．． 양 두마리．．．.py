import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 양 한마리... 양 두마리... (11123)
 1. #: 양, .: 풀, 서로 다른 # 두 개 이상이 붙어있다면 한 무리의 양들이 있는 것
[입력]
 1. T: 테스트 케이스 수
 2. H: 높이, W: 너비
 3. H줄: 양 정보가 담긴 그리드
[출력]
 1. 양 무리가 몇 개인가?
"""

"""
<풀이>
 1. bfs
"""
from collections import deque


# bfs
def bfs(greed):
    visited = [[0] * W for _ in range(H)]
    cnt = 0

    for x in range(H):
        for y in range(W):
            # 양이고 방문하지 않았다면
            if greed[x][y] == '#' and not visited[x][y]:
                # 카운트 및 방문 처리 및 bfs
                cnt += 1
                visited[x][y] = 1
                q = deque([(x, y)])

                while q:
                    sx, sy = q.popleft()

                    # 델타 탐색
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = sx + dx, sy + dy
                        # 벽 형성 및 방문하지 않았다면
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny]:
                            # 양의 무리라면 방문 처리
                            if greed[nx][ny] == '#':
                                visited[nx][ny] = 1
                                q.append((nx, ny))

    return cnt


T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    greed = [list(input().rstrip()) for _ in range(H)]

    print(bfs(greed))
