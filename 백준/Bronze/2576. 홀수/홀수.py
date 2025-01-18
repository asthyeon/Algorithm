import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

odd = []
for _ in range(7):
    number = int(input())

    if number % 2 != 0:
        odd.append(number)

if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)