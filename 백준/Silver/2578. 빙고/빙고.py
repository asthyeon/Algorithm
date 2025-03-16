import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부르는 수
calls = []
for i in range(5):
    call = list(map(int, input().split()))
    calls += call

# 각 숫자들의 위치 저장
locations = {}
for x in range(5):
    for y in range(5):
        locations[board[x][y]] = (x, y)

bingo = 0
called = [[0] * 5 for _ in range(5)]
for turn in range(25):
    nx, ny = locations[calls[turn]]
    called[nx][ny] = 1

    # 빙고가 1줄 이상이 성립될 때부터 확인
    if turn >= 4:
        # 부르는 위치로부터 가로 확인
        for d in range(5):
            if not called[nx][d]:
                break
        # 빙고일 경우 추가
        else:
            bingo += 1
        # 부르는 위치로부터 세로 확인
        for d in range(5):
            if not called[d][ny]:
                break
        # 빙고일 경우 추가
        else:
            bingo += 1
        # 왼쪽 대각선이 성립할 경우
        if nx == ny:
            for d in range(5):
                if not called[d][d]:
                    break
            # 빙고일 경우 추가
            else:
                bingo += 1
        # 오른쪽 대각선이 성립할 경우
        if nx + ny == 4:
            for d in range(5):
                if not called[d][4 - d]:
                    break
            # 빙고일 경우 추가
            else:
                bingo += 1

    # 빙고가 3줄 이상일 경우 종료
    if bingo >= 3:
        print(turn + 1)
        break