import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 숫자 정사각형 (1051)
 1. N x M 크기의 직사각형 각 칸에는 한 자리 숫자가 있음
 2. 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형 찾기
 3. 이 때, 정사각형은 행 또는 열에 평행해야 함
[입력]
 1. N: 세로, M: 가로
 2. N개의 줄: 직사각형 정보
[출력]
 1. 정답 직사각형의 크기 출력
"""

"""
<풀이>
 1. 브루트포스
"""


# 브루트포스
def brute_force(square):
    answer = 1
    # 시작점
    for sx in range(N):
        for sy in range(M):
            # 사각형 늘리려는 길이
            length = 1
            # 시작점에서 사각형 사이즈 재기
            while True:
                # 사이즈 안에 들어올 때
                if sx + length < N and sy + length < M:
                    # 모든 수가 같을 때 길이 증가 및 정답 교체
                    if square[sx][sy] == square[sx + length][sy] == square[sx][sy + length] == square[sx + length][sy + length]:
                        length += 1
                        answer = max(answer, length ** 2)
                    # 같지 않으면 길이 증가
                    else:
                        length += 1
                # 사이즈를 넘어서면 종료
                else:
                    break

    return answer


N, M = map(int, input().split())
square = [list(input().rstrip()) for _ in range(N)]

print(brute_force(square))

