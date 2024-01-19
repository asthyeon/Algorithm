import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 페그 솔리테어
1. 구멍이 뚫려 있는 이차원 게임판에서 하는 게임
2. 각 구멍에는 핀을 하나 꽂을 수 있음
3. 핀은 수평, 수직 방향으로 인접한 핀을 뛰어넘어 그 핀의 다음 칸으로 이동하는 것만 허용됨
4. 인접한 핀의 다음 칸은 비어있어야 하고 그 인접한 핀은 제거됨
5. 게임판의 핀을 적절히 움직여서 게임판에 남아 있는 핀의 개수를 최소로 만들기
* 입력
- 첫째 줄: 테스트 케이스의 개수 N 
- 둘째 줄 이후: 게임판의 초기 상태가 주어짐
  ('.': 빈 칸, 'o': 핀이 꽂힌 칸, '#': 구멍이 없는 칸, 핀의 개수는 최대 8개)
[출력: 남길 수 있는 핀의 최소 개수와 필요한 최소 이동 횟수 출력]
"""

"""
# 풀이
(1) 백트래킹 이용해보기
"""


# 백트래킹 함수
def back_tracking(board, move):
    global answer_cnt
    global answer_move
    # 핀 탐색
    for x in range(5):
        for y in range(9):
            # 핀을 발견하면 델타탐색 후 이동
            if board[x][y] == 'o':
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    # 벽형성
                    if 0 <= nx < 5 and 0 <= ny < 9:
                        # 다른 핀을 만나면
                        if board[nx][ny] == 'o':
                            # 다른 핀의 다음 칸 좌표 받기
                            nnx, nny = nx + dx, ny + dy
                            # 벽 형성
                            if 0 <= nnx < 5 and 0 <= nny < 9:
                                # 다음 칸이 구멍이라면 핀 옮기기
                                if board[nnx][nny] == '.':
                                    # 게임판 복사 후 재귀
                                    new_board = [b[:] for b in board]
                                    new_board[x][y] = '.'
                                    new_board[nx][ny] = '.'
                                    new_board[nnx][nny] = 'o'
                                    back_tracking(new_board, move + 1)
    # 핀 갯수 세기
    cnt = 0
    for x in range(5):
        for y in range(9):
            if board[x][y] == 'o':
                cnt += 1
    if answer_cnt > cnt:
        answer_cnt = cnt
        answer_move = move


# 테스트 케이스의 개수 N
N = int(input())
for tc in range(1, N + 1):
    # 게임판 상태
    board = [list(input().rstrip()) for _ in range(5)]
    # 마지막 게임판이 아니면 빈 칸을 입력받아서 처리
    if tc != N:
        space = input()

    # 최소 핀 수 및 최소 이동 횟수
    answer_cnt = 50
    answer_move = 10000
    back_tracking(board, 0)

    print(answer_cnt, answer_move)