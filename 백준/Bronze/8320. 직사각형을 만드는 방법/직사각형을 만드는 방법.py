import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 직사각형을 만드는 방법 (8320)
 1. 길이가 1인 정사각형 n개로 만들 수 있는 직사각형의 수?
 2. 직사각형 A와 B가 있을 때, A를 이동, 회전시켜서 B를 못만들면 두 직사각형은 다르다
[입력]
 1. n: 정사각형 개수
[출력]
 1. 만들 수 있는 직사각형의 개수 출력
"""

"""
<풀이>
 1. 가로 x 세로가 n보다 작거나 같을 때 하나의 사각형으로 보기
 2. 모든 경우의 수를 고려
"""

n = int(input())

cnt = 0
for x in range(1, n + 1):
    for y in range(x, n + 1):
        if x * y <= n:
            cnt += 1

print(cnt)