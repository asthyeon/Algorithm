import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 항체 인식 (22352)
 1. 백신 주사 -> 항체 생성 -> 상하좌우에 같은 데이터 값을 가지면서 인접한 칸으로 퍼져 나감
 2. 항체가 더 이상 퍼져나갈 수 없으면, 항체가 터졌던 칸들의 데이터 값은 모두 동일 값으로 됨
 3. 우연히 원래의 데이터 값과 업데이트된 데이터 값이 동일할 수도 있음
[입력]
 1. N: 세로 크기, M: 가로 크기
 2. N개의 줄: 백신을 놓기 전 촬영 결과
 3. 다음 N개의 줄: 백신을 놓은 뒤 촬영 결과
[출력]
 1. 백신을 맞았다면 YES, 아니면 NO 출력
"""

"""
<풀이>
 1. bfs
 2. 백신이 주입됐을 때 경우와 일치하는 지 확인
 3. 백신은 1번만 주입할 수 있음 -> 다른 부분이 두 영역이면 안됨
"""
from collections import deque


# bfs
def bfs(sx, sy, origin, new):
    q = deque([(sx, sy)])
    # 해당 데이터 값을 백신 후의 값으로 변경
    previous[sx][sy] = new

    while q:
        sx, sy = q.popleft()

        # 델타 탐색
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = sx + dx, sy + dy
            # 벽 형성
            if 0 <= nx < N and 0 <= ny < M:
                # 같은 데이터 값이라면
                if previous[nx][ny] == origin:
                    # 백신 후의 결과로 변경
                    previous[nx][ny] = new
                    q.append((nx, ny))


N, M = map(int, input().split())
# 백신 놓기 전
previous = [list(map(int, input().split())) for _ in range(N)]
# 백신 놓은 후
after = [list(map(int, input().split())) for _ in range(N)]

# 같은 경우 바로 종료
if previous == after:
    print('YES')
# 그 외
else:
    # 백신 놓기 전을 백신 놓은 후의 결과로 바꾸기(다른 부분 한 부분만 찾으면 됨)
    find = False
    for x in range(N):
        for y in range(M):
            # 백신 전후로 데이터 값이 다른 부분을 발견했다면 bfs
            if previous[x][y] != after[x][y]:
                bfs(x, y, previous[x][y], after[x][y])
                find = True
                break
        # 다른 부분을 찾았다면 백신 주입 종료
        if find:
            break

    # 결과 확인
    for x in range(N):
        for y in range(M):
            # 다른 부분이 하나라도 존재한다면 종료
            if previous[x][y] != after[x][y]:
                print('NO')
                exit()

    # 모든 부분이 같다면 종료
    print('YES')