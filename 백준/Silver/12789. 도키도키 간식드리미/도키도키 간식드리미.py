import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 도키도키 간식드리미 (12789)
1. 스택 이용
"""
from collections import deque

# 승환이 앞의 학생들의 수, 모든 학생들의 번호표
N = int(input())
numbers = deque(map(int, input().split()))

# 대기하는 공간
stack = []
# 번호를 받을 차례
turn = 1
while numbers:
    # 대기가 있을 경우
    if stack:
        if turn == stack[-1]:
            stack.pop()
            turn += 1
            continue
    # 다음 차례 찾기
    while numbers:
        if turn == numbers[0]:
            numbers.popleft()
            turn += 1
            break
        else:
            stack.append(numbers.popleft())
# 대기가 남았을 경우
while stack:
    if turn == stack[-1]:
        turn += 1
        stack.pop()
    else:
        break

if not stack:
    print('Nice')
else:
    print('Sad')








