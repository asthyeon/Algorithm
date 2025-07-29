import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 배열 돌리기 1 (16926)
1. 배열과 정수가 주어졌을 때 배열을 반시계 방향으로 R번 회전시킨 결과 구하기
2. 구현 -> 브루트포스로 한 번 돌려보기 -> Python3는 시간초과, PyPy3는 통과
3. 회전수가 1바퀴 돌면 이후는 같음 -> 회전 수를 최적화
"""

def rotate(sx, ex, sy, ey):
    # 회전 수 최적화
    for r in range(R % ((ex - sx + ey - sy) * 2 - 4)):
        # 좌측상단값 저장
        left_top = arr[sx][sy]
        # 상단
        for top in range(sy, ey - 1):
            if top == ey - 1:
                arr[sx][top] = arr[sx + 1][top]
            else:
                arr[sx][top] = arr[sx][top + 1]
        # 우측
        for right in range(sx, ex - 1):
            if right == ex - 1:
                arr[right][ey - 1] = arr[right][ey - 2]
            else:
                arr[right][ey - 1] = arr[right + 1][ey - 1]
        # 하단
        for down in range(ey - 1, sy, -1):
            if down == sy:
                arr[ex - 1][down] = arr[ex - 2][down]
            else:
                arr[ex - 1][down] = arr[ex - 1][down - 1]
        # 좌측
        for left in range(ex - 1, sx, -1):
            if left == sx + 1:
                arr[left][sy] = left_top
            else:
                arr[left][sy] = arr[left - 1][sy]

    # 내부 돌리기
    if ex - sx > 2 and ey - sy > 2:
        rotate(sx + 1, ex - 1, sy + 1, ey - 1)


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

rotate(0, N, 0, M)

# 정답 출력
for _ in range(N):
    print(*arr[_])