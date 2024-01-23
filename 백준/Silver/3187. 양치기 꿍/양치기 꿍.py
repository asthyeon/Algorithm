import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 양치기 꿍
1. 울타리 영역 안에서
 - 양 > 늑대: 늑대가 전부 잡아먹힘
 - 약 <= 늑대: 양이 전부 잡아먹힘
2. 영역 정보
 - '.': 빈 공간
 - '#': 울타리
 - 'v': 늑대
 - 'k': 양
3. 울타리로 막히지 않은 영역에는 양과 늑대 X, 양과 늑대는 대각선 이동 불가
* 입력
- 첫째 줄: 세로 R, 가로 C
- 각 R줄: 영역 정보
[출력: 살아남게 되는 양과 늑대의 수 순서대로 출력]
"""

"""
@ 풀이
(1) 울타리가 아니라면 bfs 탐색하기
"""


# bfs
def bfs(area, visited, sx, sy):
    # 양과 늑대의 수
    s, w = 0, 0
    # 양인지 늑대인지 확인
    if area[sx][sy] == 'k':
        s += 1
    elif area[sx][sy] == 'v':
        w += 1
    # 큐 생성 및 시작점 인큐
    q = [(sx, sy)]
    # 방문 체크
    visited[sx][sy] = 1

    while q:
        sx, sy = q.pop()

        # 델타 탐색
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = sx + dx, sy + dy
            # 벽 형성
            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0:
                # 빈 공간이면 방문 체크 후 인큐
                if area[nx][ny] == '.':
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                # 양이라면 카운트 후 방문 체크 및 인큐
                elif area[nx][ny] == 'k':
                    s += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                # 늑대라면 카운트 후 방문 체크 및 인큐
                elif area[nx][ny] == 'v':
                    w += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    # 살아남는 동물 확인
    if s > w:
        return True, s
    else:
        return False, w


# 세로 R, 가로 C
R, C = map(int, input().split())
# 영역 정보
area = [list(input().rstrip()) for _ in range(R)]

# 방문 리스트
visited = [[0] * C for _ in range(R)]
# 늑대와 양 수
sheep, wolves = 0, 0
# bfs 탐색
for x in range(R):
    for y in range(C):
        # 울타리가 아니고 방문하지 않았다면 탐색
        if area[x][y] != '#' and visited[x][y] == 0:
            flag, cnt = bfs(area, visited, x, y)
            if flag:
                sheep += cnt
            else:
                wolves += cnt

print(sheep, wolves)
