import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

sequence = []
for _ in range(n):
    num = int(input())
    sequence.append(num)

answer = []
numbers = [i for i in range(n, 0, -1)]
before = []
after = []

for target in sequence:
    while True:
        if not before:
            answer.append('+')
            before.append(numbers.pop())
        else:
            if before[-1] < target:
                answer.append('+')
                before.append(numbers.pop())
            elif before[-1] == target:
                answer.append('-')
                after.append(before.pop())
                break
            else:
                print('NO')
                exit()

for ans in answer:
    print(ans)