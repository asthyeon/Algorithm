import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

total = 0
for _ in range(5):
    score = int(input())

    total += score

print(total)