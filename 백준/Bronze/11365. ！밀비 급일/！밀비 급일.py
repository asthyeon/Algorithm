import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    password = input().rstrip()

    if password == 'END':
        break

    print(password[::-1])