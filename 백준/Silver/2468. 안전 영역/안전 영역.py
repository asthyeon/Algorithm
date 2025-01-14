import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 안전 영역 (2468)
 1. 물에 잠기지 않는 안전한 영역
  - 물에 잠기지 않는 지점들이 상, 하, 좌, 우 인접해 있는 크기가 최대인 영역 
[입력]
 1. N: 지역의 크기
 2. N개의 줄: 지역의 높이 정보
[출력]
 1. 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수 출력
"""

"""
<풀이>
 1. bfs
"""


def bfs(height, arr):
    visited = [[0] * N for _ in range(N)]
    q = []
    area = 0

    # 안전한 지역 찾기
    for sx in range(N):
        for sy in range(N):
            if not visited[sx][sy] and arr[sx][sy] > height:
                area += 1
                visited[sx][sy] = 1
                q.append((sx, sy))

                while q:
                    x, y = q.pop()

                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            if arr[nx][ny] > height:
                                visited[nx][ny] = 1
                                q.append((nx, ny))

    return area


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 가장 큰 높이 구하기
top = 0
for i in range(N):
    top = max(top, max(arr[i]))

# 정답 갱신
answer = 0
for height in range(top):
    answer = max(answer, bfs(height, arr))

print(answer)