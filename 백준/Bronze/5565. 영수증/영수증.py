import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

total = int(input())
for _ in range(9):
    read = int(input())
    total -= read

print(total)