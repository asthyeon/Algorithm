import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

A, B = map(int, input().split())
sequence = [0]
number = 1
for i in range(1001):
    for j in range(number):
        sequence.append(number)
    number += 1

    if len(sequence) >= (B + 1):
        break

print(sum(sequence[A:B + 1]))