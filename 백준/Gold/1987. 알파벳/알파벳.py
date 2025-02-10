import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 알파벳 (1987)
 1. 좌측상단 칸 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동 가능
 2. 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과 달라야 함
[입력]
 1. R: 세로, C: 가로
 2. R개의 줄: 알파벳 정보
[출력]
 1. 말이 지날 수 있는 최대의 칸 수 출력
"""

"""
<풀이>
 1. dfs
 2. 리스트 -> 시간초과 세트 사용
"""


def dfs(board, passed, x, y, cnt):
    global answer
    answer = max(answer, cnt)

    # 가능한 곳을 찾으면 재귀
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in passed:
            passed.add(board[nx][ny])
            dfs(board, passed, nx, ny, cnt + 1)
            passed.remove(board[nx][ny])


R, C = map(int, input().split())
board = list(list(input().rstrip()) for _ in range(R))

answer = 1
dfs(board, {board[0][0]}, 0, 0, 1)
print(answer)