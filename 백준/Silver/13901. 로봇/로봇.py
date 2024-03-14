import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 로봇(13901)
 1. 로봇 이동 규칙
  - 로봇은 사용자가 지정한 방향을 일직선으로 움직임
  - 이동 중 벽이나 방문한 지역, 장애물 만날 시 사용자가 지정한 다음 방향으로 움직임
  - 사용자가 지정한 다음 방향이 없다면 맨 처음 방향으로 돌아가서 위 과정 반복
  - 로봇이 움직일 수 없을 경우 동작을 멈춤
[입력]
 1. R, C: 방의 크기
 2. k: 장애물 수
 3. k개의 줄: br, bc: 장애물 위치
 4. sr, sc: 로봇 시작 위치
 5. 이동 방향 순서 4개(1: 위, 2: 아래, 3: 왼쪽, 4: 오른쪽)
[출력]
 1. 로봇의 마지막 위치 r, c 출력
"""

"""
<풀이>
 1. 구현 -> '~ 로봇은 일직선으로 움직임' = 장애물을 만나기 전까진 한 방향으로 이동
"""
# 방향 치환용
dirs = {
    1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1),
}


# 이동
def moving(room, sr, sc):
    # 시작 위치
    r, c = sr, sc
    # 누적 이동 수
    cnt = 0
    room[r][c] = cnt
    while True:
        # 모든 방향 이동 불가능 확인
        directions = 0
        for m in move:
            moved = False
            while True:
                nr, nc = r + dirs[m][0], c + dirs[m][1]
                # 이동이 가능할 경우
                if 0 <= nr < R and 0 <= nc < C and room[nr][nc] == '*':
                    cnt += 1
                    room[nr][nc] = cnt
                    r, c = nr, nc
                    moved = True
                # 이동이 불가능할 경우 방향 재탐색
                else:
                    if not moved:
                        directions += 1
                    break

        # 모든 방향 이동이 불가능할 경우 종료
        if directions == 4:
            # for _ in range(R):
            #     print(room[_])
            return r, c


# 세로 R, 가로 C
R, C = map(int, input().split())
# 방 정보
room = [['*'] * C for _ in range(R)]
# 장애물 수 및 정보 입력, 배치
k = int(input())
for _ in range(k):
    br, bc = map(int, input().split())
    room[br][bc] = 'x'

# 로봇 시작 위치
sr, sc = map(int, input().split())
# 이동 방향
move = list(map(int, input().split()))

print(*moving(room, sr, sc))














