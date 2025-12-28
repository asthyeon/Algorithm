import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 좌표 정렬하기 2
1. 좌표를 y 좌표 증가 순 -> x 좌표 증가 순으로 정렬

[풀이]
1. 정렬 
"""

N = int(input())
locations = []
for i in range(N):
    x, y = map(int, input().split())
    locations.append((x, y))

# y좌표 순으로 정렬
locations.sort(key=lambda x: (x[1], x[0]))

for location in locations:
    print(*location)