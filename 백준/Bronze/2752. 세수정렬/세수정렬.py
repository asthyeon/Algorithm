import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

numbers = list(map(int, input().split()))
numbers.sort()
for number in numbers:
    print(number)