import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 행성 탐사 (5549)
 1. 조사 대상 영역 K개 중, 정글, 바다, 얼음이 각각 몇 개씩 있는가?
  - 정글: J, 바다: O, 얼음: I
[입력]
 1. M, N: 지도 크기
 2. K: 조사 대상 영역 개수
 3. M개 줄: 상근이가 본내 지도의 내용
 4. K개 줄: 조사 대상 영역 정보 (a, b): 왼쪽 위 모서리 좌표, (c, d): 오른쪽 아래 모서리 좌표
[출력]
 1. 각 조사 대상 영역에 포함되어 있는 정글, 바다, 얼음 수 한 줄에 한 정보씩 출력
"""

"""
<풀이>
 1. bfs -> 시간초과
 2. 누적합 이용
"""

M, N = map(int, input().split())
K = int(input())
planet = [list(input().rstrip()) for _ in range(M)]

# 누적합 배열
prefix_sum = [[[0, 0, 0] for _ in range(N + 1)] for _ in range(M + 1)]
# 누적합 계산
for x in range(1, M + 1):
    for y in range(1, N + 1):
        # 첫 줄, 첫 칸일 때
        if x == 1 and y == 1:
            if planet[x - 1][y - 1] == 'J':
                prefix_sum[x][y][0] += 1
            elif planet[x - 1][y - 1] == 'O':
                prefix_sum[x][y][1] += 1
            else:
                prefix_sum[x][y][2] += 1
        # 첫 줄일 때
        elif x == 1:
            # 이전 값
            for i in range(3):
                prefix_sum[x][y][i] = prefix_sum[x][y - 1][i]
            if planet[x - 1][y - 1] == 'J':
                prefix_sum[x][y][0] += 1
            elif planet[x - 1][y - 1] == 'O':
                prefix_sum[x][y][1] += 1
            else:
                prefix_sum[x][y][2] += 1
        # 첫 칸일 때
        elif y == 1:
            # 이전 값
            for i in range(3):
                prefix_sum[x][y][i] = prefix_sum[x - 1][y][i]
            if planet[x - 1][y - 1] == 'J':
                prefix_sum[x][y][0] += 1
            elif planet[x - 1][y - 1] == 'O':
                prefix_sum[x][y][1] += 1
            else:
                prefix_sum[x][y][2] += 1
        # 그 외
        else:
            # 이전 값
            for i in range(3):
                prefix_sum[x][y][i] = (prefix_sum[x][y - 1][i] +
                                       prefix_sum[x - 1][y][i] -
                                       prefix_sum[x - 1][y - 1][i])
            if planet[x - 1][y - 1] == 'J':
                prefix_sum[x][y][0] += 1
            elif planet[x - 1][y - 1] == 'O':
                prefix_sum[x][y][1] += 1
            else:
                prefix_sum[x][y][2] += 1

# 조사
for _ in range(K):
    a, b, c, d = map(int, input().split())

    # 누적 합 구하기
    base = prefix_sum[c][d][:]
    for j in range(3):
        base[j] -= prefix_sum[c][b - 1][j]
        base[j] -= prefix_sum[a - 1][d][j]
        base[j] += prefix_sum[a - 1][b - 1][j]

    print(*base)

