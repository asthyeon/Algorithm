import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 암벽 등반 (2412)
 1. 암벽에 n개의 홈이 파져 있음
 2. 각각의 홈의 좌표는 (x, y)
  - |a - x| <= 2 이고 |b - y| <= 2 라면, (x, y)에서 (a, b)로 이동 가능
 3. y = T 일 때까지, 즉 암벽의 정상까지 오르기
[입력]
 1. n: 홈의 수, T: 정상
 2. n개의 줄: x, y 좌표(현재 위치인 (0, 0)은 주어지지 않음)
[출력]
 1. 최소 이동 회수 출력, 정상에 오를 수 없으면 -1 출력
"""

"""
<풀이>
 1. 일단 풀어보기 -> bfs
"""
from collections import deque

n, T = map(int, input().split())
# 각 좌표들
locations = set()
for _ in range(n):
    x, y = map(int, input().split())
    locations.add((x, y))

q = deque([(0, 0, 0)])

while q:
    x, y, cnt = q.popleft()

    # 정상에 도달했을 경우 종료
    if y == T:
        print(cnt)
        exit()

    # 등반하기
    for up_x in range(2, -3, -1):
        for up_y in range(2, -3, -1):
            nx, ny = x + up_x, y + up_y
            # 해당 지점이 존재한다면
            if (nx, ny) in locations:
                # 인큐 후 해당 지점은 삭제
                q.append((nx, ny, cnt + 1))
                locations.remove((nx, ny))

# 정상에 도달하지 못한 경우
print(-1)