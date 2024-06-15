import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 지구 온난화 (5212)
 1. 50년이 지나면 인접한 세 칸 또는 네 칸에 바다가 있는 땅은 모두 잠겨버림
 2. 지도의 크기는 모든 섬을 포함하는 가장 작은 직사각형(크기도 작아짐)
 3. 지도의 범위를 벗어나는 칸은 모두 바다
 4. 지도 정보
  - X: 땅, .: 바다
[입력]
 1. R: 세로, C: 가로
 2. R개의 줄: 지도 정보
[출력]
 1. 50년 후의 지도
"""

"""
<풀이>
 1. 일단 풀어보기
"""


# 인접한 세 칸 또는 네 칸에 바다가 있는 땅 확인
def check_sea(x, y, earth):
    # 인접한 땅 바다인지 확인
    cnt = 0
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        # 지도 안일 경우 -> 바다일 경우 카운트
        if 0 <= nx < R and 0 <= ny < C:
            if earth[nx][ny] == '.':
                cnt += 1
        # 지도 밖일 경우 -> 바다이므로 카운트
        else:
            cnt += 1

    # 잠기는 경우
    if cnt >= 3:
        return '.'
    # 잠기지 않는 경우
    else:
        return 'X'


# 지구 온난화
def global_warming(earth):
    # 살아남는 땅
    land = [['.'] * C for _ in range(R)]

    # 살아남는 땅 확인
    for x in range(R):
        for y in range(C):
            if earth[x][y] == 'X':
                land[x][y] = check_sea(x, y, earth)

    # land를 순회하며 가로 세로 시작점, 끝점 찾기
    start_x = 10
    end_x = 0
    start_y = 10
    end_y = 0

    for x in range(R):
        for y in range(C):
            # 살아남은 땅일 경우 사이즈 재기
            if land[x][y] == 'X':
                start_x = min(start_x, x)
                end_x = max(end_x, x)
                start_y = min(start_y, y)
                end_y = max(end_y, y)
    
    # 가장 작은 정사각형 출력
    for i in range(start_x, end_x + 1):
        print(*land[i][start_y:end_y + 1], sep='')


R, C = map(int, input().split())
earth = [list(input().rstrip()) for _ in range(R)]

global_warming(earth)