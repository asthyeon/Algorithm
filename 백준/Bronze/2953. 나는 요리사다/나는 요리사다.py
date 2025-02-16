import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

number = 0
answer = 0
for i in range(1, 6):
    score = list(map(int, input().split()))
    total = sum(score)

    if answer < total:
        number = i
        answer = total

print(number, answer)