import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

line = []
for i in range(n):
    if numbers[i] == 0:
        line.append(i + 1)
    else:
        line.insert(len(line) - numbers[i], i + 1)

print(*line)

