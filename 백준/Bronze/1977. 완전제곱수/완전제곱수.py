import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

M = int(input())
N = int(input())

numbers = set()
for number in range(M, N + 1):
    if int(number ** (1 / 2)) ** 2 == number:
        numbers.add(number)

if not numbers:
    print(-1)
else:
    print(sum(numbers))
    print(min(numbers))