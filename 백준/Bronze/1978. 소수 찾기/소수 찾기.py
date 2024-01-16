import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

answer = 0
for number in numbers:
    if number == 1:
        continue
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        answer += 1
print(answer)
