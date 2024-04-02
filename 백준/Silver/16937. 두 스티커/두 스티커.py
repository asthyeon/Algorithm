import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 두 스티커 (16973)
 1. H x W 모눈종이에 스티커 N 개중 2개 붙이기
 2. 스티커는 90도 회전 가능
[입력]
 1. H, W: 모눈종이 크기
 2. N: 스티커 수
 3. N개의 줄: R, C: 스티커 크기
[출력]
 1. 두 스티커가 붙여진 넓이의 최댓값 출력
 2. 두 스티커를 못붙일 경우 0 출력
"""

"""
<풀이>
 1. 모든 경우 구하기
"""


# 스티커 붙이기
def attach(stickers):
    attached = 0

    # 스티커 2개 선택
    for first in range(N - 1):
        for second in range(first + 1, N):
            f_R, f_C = stickers[first]
            s_R, s_C = stickers[second]

            # 무회전 세로 이어 붙이기
            if f_R + s_R <= H and (f_C <= W and s_C <= W):
                attached = max(attached, f_R * f_C + s_R * s_C)
            # 무회전 가로 이어 붙이기
            if (f_R <= H and s_R <= H) and f_C + s_C <= W:
                attached = max(attached, f_R * f_C + s_R * s_C)

            # first 회전 세로 이어 붙이기
            if f_C + s_R <= H and (f_R <= W and s_C <= W):
                attached = max(attached, f_R * f_C + s_R * s_C)
            # first 회전 가로 이어 붙이기
            if (f_C <= H and s_R <= H) and f_R + s_C <= W:
                attached = max(attached, f_R * f_C + s_R * s_C)

            # second 회전 세로 이어 붙이기
            if f_R + s_C <= H and (f_C <= W and s_R <= W):
                attached = max(attached, f_R * f_C + s_R * s_C)
            # second 회전 가로 이어 붙이기
            if (f_R <= H and s_C <= H) and f_C + s_R <= W:
                attached = max(attached, f_R * f_C + s_R * s_C)

            # 쌍회전 세로 이어 붙이기
            if f_C + s_C <= H and (f_R <= W and s_R <= W):
                attached = max(attached, f_R * f_C + s_R * s_C)
            # 쌍회전 가로 이어 붙이기
            if (f_C <= H and s_C <= H) and f_R + s_R <= W:
                attached = max(attached, f_R * f_C + s_R * s_C)

    return attached


# 종이 세로 H, 가로 W
H, W = map(int, input().split())
# 스티커 수 N
N = int(input())
stickers = []
for _ in range(N):
    # 스티커 세로 R, 가로 C
    R, C = map(int, input().split())
    stickers.append((R, C))

print(attach(stickers))
