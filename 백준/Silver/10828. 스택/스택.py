import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    commands = list(input().split())

    if commands[0] == 'push':
        stack.append(commands[1])

    elif commands[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif commands[0] == 'size':
        print(len(stack))

    elif commands[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)

    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)