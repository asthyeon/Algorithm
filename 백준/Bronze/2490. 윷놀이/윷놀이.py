import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

answer = {3: 'A', 2: 'B', 1: 'C', 0: 'D', 4: 'E'}
for _ in range(3):
    throw = list(map(int, input().split()))
    print(answer[sum(throw)])