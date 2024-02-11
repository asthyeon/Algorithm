import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 필터(1895)
 1. 중앙값은 다섯 번째 숫자
 2. 필터의 크기는 3 x 3(이미지의 중앙값을 찾으면서 잡음 제거)
 3. 이미지 I는 크기가 R x C인 2차원 픽셀, 각 픽셀은 어두운 정도 V를 나타냄
 4. 이미지 I가 주어졌을 때 필터링된 이미지 J를 구하고 값이 T보다 크거나 같은 픽셀의 수 구하기
[입력]
 1. 이미지의 크기 R, C
 2. 이미지 정보
 3. 기준치 T
[출력]
 1. 필터링된 이미지 J의 각 픽셀 값 중에서 T보다 크거나 같은 것의 개수 출력
"""

"""
<풀이>
 1. 일단 풀어보기
"""


# 필터링
def filtering(I, sx, sy):
    # 필터링된 숫자들
    filtered = []

    # 필터링한 숫자들을 다 집어넣기
    for x in range(sx, sx + 3):
        for y in range(sy, sy + 3):
            filtered.append(I[x][y])

    # 중앙값 찾기
    filtered.sort()
    if filtered[4] >= T:
        return 1
    else:
        return 0


# 세로 R, 가로 C
R, C = map(int, input().split())
# 이미지 I
I = [list(map(int, input().split())) for _ in range(R)]
# 기준치 T
T = int(input())

# 필터링하기
answer = 0
for sx in range(R - 2):
    for sy in range(C - 2):
        answer += filtering(I, sx, sy)

print(answer)