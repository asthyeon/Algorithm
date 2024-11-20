import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 색종이 - 2 (2567)
 1. 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지 존재
 2. 가로, 세로 크기가 각각 10인 정사각형 모양의 색종이를 도화지의 변이 평행하도록 붙임
 3. 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 둘레 구하기
[입력]
 1. N: 색종이의 수
 2. N개의 줄
  - 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리
  - 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리
[출력]
 1. 색종이가 붙은 검은 영역의 둘레 출력
"""

"""
<풀이>
 1. 델타탐색
"""

N = int(input())
# 도화지
paper = [[0] * 101 for _ in range(101)]
for _ in range(N):
    i, j = map(int, input().split())

    # 영역 칠하기
    for x in range(i, i + 10):
        for y in range(j, j + 10):
            paper[x][y] = 1

# 둘레 구하기
answer = 0
for i in range(1, 101):
    for j in range(1, 101):
        if paper[i][j]:
            circumference = 0
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 1 <= ni < 101 and 1 <= nj < 101:
                    if paper[ni][nj]:
                        circumference += 1
            # 모서리
            if circumference == 2:
                answer += 2
            # 변
            elif circumference == 3:
                answer += 1

print(answer)

