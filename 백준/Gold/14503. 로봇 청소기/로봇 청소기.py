import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 로봇 청소기 (14503)
 1. 로봇 청소기가 있는 방은 N x M 크기의 직사각형
 2. 각각의 칸은 벽 또는 빈 칸
 3. 청소기가 바라보는 방향은 동, 서, 남, 북 중 하나
 4. 처음에 빈 칸은 전부 청소되지 않은 상태
 5. 로봇 청소기 작동 방식
  (1) 현재 칸이 아직 청소되지 않은 경우, 현재 칸 청소
  (2) 현재 칸 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
   ㄱ. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면, 한 칸 후진하고 (1)번으로 돌아감
   ㄴ. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춤
  (3) 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
   ㄱ. 반시계 방향으로 90도 회전
   ㄴ. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
   ㄷ. (1)번으로 돌아감
[입력]
 1. N, M: 방의 크기
 2. r, c: 처음에 로봇 청소기가 있는 칸의 좌표, d: 처음에 로봇 청소기가 바라보는 방향
   (d = 0: 북, 1: 동, 2: 남, 3: 서)
 3. N개의 줄: 각 장소의 상태를 나타냄 (0: 청소되지 않은 빈 칸, 1: 벽이 있는 것)
[출력]
 1. 로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력
"""

"""
<풀이>
 1. 구현
"""
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def cleaning(arr, r, c, d):
    answer = 0

    while True:
        # 청소
        if arr[r][c] == 0:
            answer += 1
            arr[r][c] = 2

        # 로봇 작동
        for i in range(1, 5):
            # 방향 설정
            nd = d - i
            if nd < 0:
                nd = 4 + d - i

            nr = r + dr[nd]
            nc = c + dc[nd]
            if 0 <= nr < N and 0 <= nc < M:
                # 청소되지 않은 빈 칸을 찾았다면 전진
                if arr[nr][nc] == 0:
                    r, c = nr, nc
                    d = nd
                    break
        # 청소되지 않은 빈 칸이 없다면
        else:
            nd = d - 2
            if nd < 0:
                nd = 4 + d - 2

            nr = r + dr[nd]
            nc = c + dc[nd]
            # 후진이 가능하다면 후진
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 1:
                r, c = nr, nc
            # 후진이 불가능하면 멈추기
            else:
                break

    return answer


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))

print(cleaning(arr, r, c, d))