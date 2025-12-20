import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 거스름돈 (5585)
1. 500/100/50/10/5/1 엔의 거스름돈
2. 1000엔을 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하기

[풀이]
1. 그리디
"""

price = int(input())
# 현재 잔돈 구하기
change = 1000 - price

# 잔돈 종류
changes = [500, 100, 50, 10, 5, 1]
answer = 0

# 큰 잔돈부터 개수 세기
for c in changes:
    answer += change // c
    change %= c

print(answer)

