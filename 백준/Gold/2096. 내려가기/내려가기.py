import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 내려가기 (2096)
 1. 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 됨
 2. 바로 아래의 수 or 바로 아래의 수와 붙어 있는 수로만 이동 가능
 3. 파란 동그라미: 다음 줄로 내려갈 수 있는 위치
 4. 빨간 가위표: 원룡이가 내려갈 수 없는 위치
[입력]
 1. N: 줄 수
 2. N개의 줄: 숫자 세 개가 주어짐
[출력]
 1. 얻을 수 있는 최대 점수와 최소 점수
"""

"""
<풀이>
 1. 브루트포스 -> 메모리 초과
 2. dp -> 메모리 초과
 3. 메모리를 적게 쓰기 -> 모든 구간을 구할 필요 X
 4. 값을 받으면서 갱신하기
"""


N = int(input())
game = [[], []]
# 최댓값과 최솟값 반영할 리스트
maximum = [[0] * 3 for _ in range(2)]
minimum = [[0] * 3 for _ in range(2)]

for i in range(N):
    line = list(map(int, input().split()))

    if i % 2 == 0:
        game[0] = line
        for j in range(3):
            if j == 0:
                maximum[0][j] = max(maximum[1][j], maximum[1][j + 1])
                maximum[0][j] += game[0][j]
                minimum[0][j] = min(minimum[1][j], minimum[1][j + 1])
                minimum[0][j] += game[0][j]
            elif j == 1:
                maximum[0][j] = max(maximum[1][j - 1], maximum[1][j], maximum[1][j + 1])
                maximum[0][j] += game[0][j]
                minimum[0][j] = min(minimum[1][j - 1], minimum[1][j], minimum[1][j + 1])
                minimum[0][j] += game[0][j]
            else:
                maximum[0][j] = max(maximum[1][j - 1], maximum[1][j])
                maximum[0][j] += game[0][j]
                minimum[0][j] = min(minimum[1][j - 1], minimum[1][j])
                minimum[0][j] += game[0][j]
    else:
        game[1] = line
        for j in range(3):
            if j == 0:
                maximum[1][j] = max(maximum[0][j], maximum[0][j + 1])
                maximum[1][j] += game[1][j]
                minimum[1][j] = min(minimum[0][j], minimum[0][j + 1])
                minimum[1][j] += game[1][j]
            elif j == 1:
                maximum[1][j] = max(maximum[0][j - 1], maximum[0][j], maximum[0][j + 1])
                maximum[1][j] += game[1][j]
                minimum[1][j] = min(minimum[0][j - 1], minimum[0][j], minimum[0][j + 1])
                minimum[1][j] += game[1][j]
            else:
                maximum[1][j] = max(maximum[0][j - 1], maximum[0][j])
                maximum[1][j] += game[1][j]
                minimum[1][j] = min(minimum[0][j - 1], minimum[0][j])
                minimum[1][j] += game[1][j]

if N % 2 == 0:
    print(max(maximum[1]), min(minimum[1]))
else:
    print(max(maximum[0]), min(minimum[0]))