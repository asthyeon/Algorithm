import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 사탕 게임 (3085)
 1. N x N 크기에 사탕을 채워 놓음
 2. 사탕의 색은 모두 같지 않을 수 있음
 3. 사탕의 색이 다른 인접한 두 칸을 고름
 4. 그 다음 고른 칸에 들어 있는 사탕을 서로 교환
 5. 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 or 열)을 고른 다음 사탕을 먹음
[입력]
 1. N: 보드의 크기
 2. N개의 줄: 보드에 채워져 있는 사탕의 색상(C: 빨강, P: 파랑, Z: 초록, Y: 노랑)
[출력]
 1. 상근이가 먹을 수 있는 사탕의 최대 개수 출력
"""

"""
<풀이>
 1. 브루트포스
 2. 사탕을 바꾸지 않을 때는 먹지 않음
"""


def brute_force(board):
    answer = 0
    # 시작점
    for start in range(N):
        # print('# X line')
        new_x = board[start]
        # x축
        for i in range(1, N):
            # 왼쪽과 다른 경우 교환
            if board[start][i - 1] != board[start][i]:
                # print(f'{i} left_prev: {new_x}')
                left = board[start][i - 1]
                origin = board[start][i]
                new_x[i] = left
                new_x[i - 1] = origin
                # 최대 개수 세기
                answer = max(answer, count_candy(new_x))
                # print(f'{i} left_next: {new_x}')
                # 원복
                new_x[i] = origin
                new_x[i - 1] = left

            # 맨 위줄이 아닐 때, 위쪽과 다른 경우 교환
            if start != 0:
                if board[start - 1][i] != board[start][i]:
                    # print(f'{i} up_prev: {new_x}')
                    up = board[start - 1][i]
                    origin = board[start][i]
                    new_x[i] = up
                    # 최대 개수 세기
                    answer = max(answer, count_candy(new_x))
                    # print(f'{i} up_next: {new_x}')
                    # 원복
                    new_x[i] = origin

            # 맨 아래줄이 아닐 때, 아래쪽과 다른 경우 교환
            if start != N - 1:
                if board[start + 1][i] != board[start][i]:
                    # print(f'{i} down_prev: {new_x}')
                    down = board[start + 1][i]
                    origin = board[start][i]
                    new_x[i] = down
                    # 최대 개수 세기
                    answer = max(answer, count_candy(new_x))
                    # print(f'{i} down_next: {new_x}')
                    # 원복
                    new_x[i] = origin

            # 최대 개수 세기
            answer = max(answer, count_candy(new_x))

        # print('# Y line')
        # y축
        new_y = []
        for _ in range(N):
            new_y.append(board[_][start])
        for j in range(1, N):
            # 위쪽과 다른 경우 교환
            if board[j - 1][start] != board[j][start]:
                # print(f'{j} up_prev: {new_y}')
                up = board[j - 1][start]
                origin = board[j][start]
                new_y[j] = up
                new_y[j - 1] = origin
                # 최대 개수 세기
                answer = max(answer, count_candy(new_y))
                # print(f'{j} up_next: {new_y}')
                # 원복
                new_y[j] = origin
                new_y[j - 1] = up

            # 맨 왼쪽 줄이 아닐 때, 왼쪽과 다른 경우 교환
            if start != 0:
                if board[j][start - 1] != board[j][start]:
                    # print(f'{j} left_prev: {new_y}')
                    left = board[j][start - 1]
                    origin = board[j][start]
                    new_y[j] = left
                    # 최대 개수 세기
                    answer = max(answer, count_candy(new_y))
                    # print(f'{j} left_next: {new_y}')
                    # 원복
                    new_y[j] = origin

            # 맨 오른쪽 줄이 아닐 때, 오른쪽과 다른 경우 교환
            if start != N - 1:
                if board[j][start + 1] != board[j][start]:
                    # print(f'{j} right_prev: {new_y}')
                    right = board[j][start + 1]
                    origin = board[j][start]
                    new_y[j] = right
                    # 최대 개수 세기
                    answer = max(answer, count_candy(new_y))
                    # print(f'{j} right_next: {new_y}')
                    # 원복
                    new_y[j] = origin

            # 최대 개수 세기
            answer = max(answer, count_candy(new_y))

    return answer


# 사탕 개수 세기
def count_candy(line):
    maximum = 1
    cnt = 1
    previous = line[0]
    for i in range(1, N):
        if previous == line[i]:
            cnt += 1
        else:
            maximum = max(maximum, cnt)
            cnt = 1
            previous = line[i]

    return max(maximum, cnt)


N = int(input())
board = [list(input().rstrip()) for _ in range(N)]

print(brute_force(board))