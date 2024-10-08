import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

word = input().rstrip()

targets = {'a', 'e', 'i', 'o', 'u'}
cnt = 0
for alphabet in word:
    if alphabet in targets:
        cnt += 1
print(cnt)