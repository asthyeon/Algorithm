import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
chang = 100
sang = 100
for _ in range(n):
    c, s = map(int, input().split())

    if c > s:
        sang -= c
    elif c < s:
        chang -= s

print(chang)
print(sang)