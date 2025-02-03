import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

numbers = []
for _ in range(10):
    number = int(input())
    numbers.append(number)

print(sum(numbers) // 10)
print(max(numbers, key=numbers.count))