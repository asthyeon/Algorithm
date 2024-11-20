import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 색종이 (2563)
 1. 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지 존재
 2. 가로, 세로 크기가 각각 10인 정사각형 모양의 색종이를 도화지의 변이 평행하도록 붙임
 3. 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이 구하기
[입력]
 1. N: 색종이의 수
 2. N개의 줄
  - 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리
  - 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리
[출력]
 1. 색종이가 붙은 검은 영역의 넓이 출력
"""

"""
<풀이>
 1. 일단 풀어보기
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

# 칠해진 영역 세기
answer = 0
for cnt in range(101):
    answer += paper[cnt].count(1)

print(answer)

