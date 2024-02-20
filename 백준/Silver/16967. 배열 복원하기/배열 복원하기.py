import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 배열 복원하기
 1. 크기가 H x W인 배열 A와 두 정수 X, Y 존재
 2. 크기가 (H + X) x (W + Y)인 열 B는 배열 A를 아래로 X칸, 오른쪽으로 Y칸 이동시켜 만듦
 3. 수가 겹쳐지만 수가 합쳐짐
 4. 배열 B의 (i, j)에 들어있는 값
  - (i, j)가 두 배열 모두에 포함X: 0
  - (i, j)가 두 배열 모두에 포함O: A(i, j) + A(i - X, j - Y)
  - (i, j)가 두 배열 중 하나에 포함: A(i, j) or A(i - X, j - Y)
 5. 배열 B와 정수 X, Y가 주어졌을 때 배열 A를 구해보자
[입력]
 1. H, W: 크기, X, Y: 두 정수
 2. 2번째 줄 ~ H + X개 줄에 배열 B의 원소가 주어짐
[출력]
 1. 총 H개의 줄에 배열 A의 원소 출력
"""

"""
<풀이>
 1. 일단 풀어보기
"""

# 세로 H, 가로 W, 정수 X, 정수 Y
H, W, X, Y = map(int, input().split())
# 배열 B
B = [list(map(int, input().split())) for _ in range(H + X)]

# 겹치는 부분에서 겹치는 요소 제거하기
for x in range(X, H):
    for y in range(Y, W):
        B[x][y] -= B[x - X][y - Y]

# A부분까지만 출력
for x in range(H):
    print(*B[x][:W])
