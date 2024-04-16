import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

row = 1
col = 1
answer = 0
for r in range(9):
    numbers = list(map(int, input().split()))
    for c in range(9):
        if numbers[c] >= answer:
            row = r + 1
            col = c + 1
            answer = numbers[c]

print(answer)
print(row, col)
