import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 신나는 함수 실행 (9184)
1. if a <= 0 or b <= 0 or c <= 0:
     1
2. if a > 20 or b > 20 or c > 20:
     w(20, 20, 20)
3. if a < b and b < c:
     w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
4. else:
     w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) + w(a - 1, b - 1, c - 1)

[풀이]
1. dp
2. 각 값을 미리 저장하기
3. 20 초과는 20
"""

# 3중 배열
w = [[[0] * 21 for _ in range(21)] for _ in range(21)]


for a in range(21):
    for b in range(21):
        for c in range(21):
            # 첫 번째 조건
            if a <= 0 or b <= 0 or c <= 0:
                w[a][b][c] = 1
            # 세 번째 조건
            elif a < b and b < c:
                w[a][b][c] = w[a][b][c - 1] + w[a][b - 1][c - 1] - w[a][b - 1][c]
            # 네 번째 조건
            else:
                w[a][b][c] = w[a - 1][b][c] + w[a - 1][b - 1][c] + w[a - 1][b][c - 1] - w[a - 1][b - 1][c - 1]


while True:
    a, b, c = map(int, input().split())

    # 종료 조건
    if a == b == c == -1:
        break

    # 첫 번째 조건
    if a <= 0 or b <= 0 or c <= 0:
        answer = 1
    # 두 번째 조건
    elif a > 20 or b > 20 or c > 20:
        answer = w[20][20][20]
    # 세 번째 조건 + 네 번째 조건
    else:
        answer = w[a][b][c]

    print(f'w({a}, {b}, {c}) = {answer}')