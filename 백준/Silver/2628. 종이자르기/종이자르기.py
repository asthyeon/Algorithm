import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 종이자르기 (2628)
 1. 점선을 따라 종이를 칼로 자르려고 함
 2. 점선은 끝에서 끝으로 자름
 3. 종이를 자른 후 가장 큰 종이 조각의 넓이 구하기
[입력]
 1. R: 가로, C: 세로
 2. N: 칼로 잘라야 하는 점선의 개수
 3. N개의 줄: d: 자르는 방향(0: 가로, 1: 세로), n: 점선 번호
[출력]
 1. 가장 큰 종이 조각의 넓이 출력
"""

"""
<풀이>
 1. 가로, 세로 각각 모든 길이를 받아서 정렬하기
 2. 0과 최대 길이를 함께 넣기
"""

C, R = map(int, input().split())
N = int(input())
col = [0]
row = [0]
for _ in range(N):
    d, n = map(int, input().split())

    # 가로 자르기 -> 세로 길이 영향
    if d == 0:
        col.append(n)
    # 세로 자르기 -> 가로 길이 영향
    else:
        row.append(n)

# 최대 길이 붙이기 및 가로 세로 정렬
col.append(R)
row.append(C)
col.sort()
row.sort()

# 가장 큰 값 구하기
answer = 0
for x in range(1, len(row)):
    for y in range(1, len(col)):
        # 가로 세로 길이
        width = row[x] - row[x - 1]
        length = col[y] - col[y - 1]

        # 가장 큰 값 교체
        answer = max(answer, width * length)

print(answer)

