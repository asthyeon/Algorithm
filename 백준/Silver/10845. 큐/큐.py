import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N = int(input())
q = deque([])
for _ in range(N):
    commands = input().split()

    if commands[0] == 'push':
        q.append(int(commands[1]))

    elif commands[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)

    elif commands[0] == 'size':
        print(len(q))

    elif commands[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)

    elif commands[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)

    else:
        if q:
            print(q[-1])
        else:
            print(-1)
