import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
birthdays = {}
for _ in range(n):
    name, d, m, y = map(str, input().split())

    birth = y + f'{int(m):02}' + d
    birthdays[birth] = name

print(birthdays[max(birthdays)])
print(birthdays[min(birthdays)])
