import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 어두운 건 무서워 (16507)
 1. 사진의 일부분에 해당하는 밝기 평균 구하기
[입력]
 1. R, C: 사진의 크기, Q: 사진 일부분의 밝기 평균을 알아볼 개수
 2. R개의 줄: 사진 정보
 3. Q개의 줄: 사진의 일부분을 나타내기 위한 두 꼭짓점을 의미하는 정수 r1, c1, r2, c2
[출력]
 1. 두 꼭짓점으로 하는 직사각형의 밝기 평균 출력
 2. 평균은 정수 나눗셈으로 몫만 취할 것
"""

"""
<풀이>
 1. 누적 합
"""

R, C, Q = map(int, input().split())
# 사진 정보
photo = [list(map(int, input().split())) for _ in range(R)]
# 누적합
prefix = [[0] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if r == 0 and c == 0:
            prefix[r][c] = photo[r][c]
        elif r == 0:
            prefix[r][c] = prefix[r][c - 1] + photo[r][c]
        elif c == 0:
            prefix[r][c] = prefix[r - 1][c] + photo[r][c]
        else:
            prefix[r][c] = prefix[r - 1][c] + prefix[r][c - 1] + photo[r][c] - prefix[r - 1][c - 1]

# 일부분 정보
for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())

    # 나눌 몫
    share = (r2 - r1 + 1) * (c2 - c1 + 1)

    # 나눌 값
    if r1 == 1 and c1 == 1:
        value = prefix[r2 - 1][c2 - 1]
    elif r1 == 1:
        value = prefix[r2 - 1][c2 - 1] - prefix[r2 - 1][c1 - 2]
    elif c1 == 1:
        value = prefix[r2 - 1][c2 - 1] - prefix[r1 - 2][c2 - 1]
    else:
        value = (prefix[r2 - 1][c2 - 1] - prefix[r1 - 2][c2 - 1] -
                 prefix[r2 - 1][c1 - 2] + prefix[r1 - 2][c1 - 2])

    print(value // share)

