import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

dq = deque([])

N = int(input())
for _ in range(N):
    command = list(map(str, input().split()))

    if command[0] == 'push_front':
        dq.appendleft(command[1])

    elif command[0] == 'push_back':
        dq.append(command[1])

    elif command[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)

    elif command[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(dq))

    elif command[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)

    elif command[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)

    else:
        if dq:
            print(dq[-1])
        else:
            print(-1)