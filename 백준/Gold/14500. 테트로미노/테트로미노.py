import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 테트로미노 (14500)
 1. 폴리오미노: 크기가 1x1인 정사각형을 여러 개 이어서 붙인 도형
  - 정사각형은 서로 겹치면 안됨
  - 도형은 모두 연결되어 있어야 함
  - 정사각형의 변끼리 연결되어 있어야 함(꼭짓점과 꼭짓점만 맞닿아 있으면 안됨)
 2. 테트로미노: 정사각형 4개를 이어 붙인 폴리오미노로 5가지가 존재
 3. 크기가 NxM인 종이 위에 테트로미노 하나를 놓아, 그 칸의 합을 최대로 만들기
 4. 테트로미노는 회전이나 대칭 가능
[입력]
 1. N: 세로 크기, M: 가로 크기
 2. N개의 줄: 종이 정보
[출력]
 1. 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값 출력
"""

"""
<풀이>
 1. 구현
"""
# 도형들
diagrams = {
    # 첫 번째 도형
    1: [
        # 가로, 세로
        [(0, 1), (0, 2), (0, 3)],
        [(1, 0), (2, 0), (3, 0)]
    ],
    # 두 번째 도형
    2: [
        [(0, 1), (1, 0), (1, 1)]
    ],
    # 세 번째 도형
    3: [
        # 기본, 90도, 180도, 270도
        [(1, 0), (2, 0), (2, 1)],
        [(0, -1), (0, -2), (1, -2)],
        [(-1, 0), (-2, 0), (-2, -1)],
        [(0, 1), (0, 2), (-1, 2)],
        # 반전, 90도, 180도, 270도
        [(1, 0), (2, 0), (2, -1)],
        [(0, -1), (0, -2), (-1, -2)],
        [(-1, 0), (-2, 0), (-2, 1)],
        [(0, 1), (0, 2), (1, 2)],
    ],
    # 네 번째 도형
    4: [
        # 기본, 90도, 180도, 270도
        [(1, 0), (1, 1), (2, 1)],
        [(0, -1), (1, -1), (1, -2)],
        [(-1, 0), (-1, -1), (-2, -1)],
        [(0, 1), (-1, 1), (-1, 2)],
        # 반전, 90도, 180도, 270도
        [(1, 0), (1, -1), (2, -1)],
        [(0, -1), (-1, -1), (-1, -2)],
        [(-1, 0), (-1, 1), (-2, 1)],
        [(0, 1), (1, 1), (1, 2)],
    ],
    # 다섯 번째 도형
    5: [
        # 기본, 90도, 180도, 270도
        [(0, 1), (0, 2), (1, 1)],
        [(1, 0), (2, 0), (1, -1)],
        [(0, -1), (0, -2), (-1, -1)],
        [(-1, 0), (-2, 0), (-1, 1)],
        # 반전, 90도, 180도, 270도
        [(0, 1), (0, 2), (-1, 1)],
        [(1, 0), (2, 0), (1, 1)],
        [(0, -1), (0, -2), (1, -1)],
        [(-1, 0), (-2, 0), (-1, -1)],
    ]
}


# 테트로미노 합 구하기
def tetromino(x, y):
    global answer

    # 도형 종류 순회
    for number in range(1, 6):

        # 각 도형 경우의 수 순회
        for case in diagrams[number]:
            plus = paper[x][y]

            # 각 도형 좌표 순회
            for dx, dy in case:
                nx, ny = x + dx, y + dy
                # 좌표를 벗어나면 도형 성립 X -> 종료
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    break
                plus += paper[nx][ny]

            # 도형이 성립되면 값 비교
            else:
                answer = max(answer, plus)


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

answer = 0
# 종이 순회
for x in range(N):
    for y in range(M):
        # 종이에 테트로미노 놓기
        tetromino(x, y)
print(answer)