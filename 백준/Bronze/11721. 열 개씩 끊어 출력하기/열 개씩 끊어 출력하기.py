import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

word = input().rstrip()

for i in range(1, len(word) + 1):
    print(word[i - 1], end="")
    if i % 10 == 0:
        print()