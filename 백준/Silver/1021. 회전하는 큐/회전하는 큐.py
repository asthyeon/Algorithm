import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
locations = list(map(int, input().split()))

q = deque(list(i for i in range(1, N + 1)))
cnt = 0
for number in locations:
    while True:
        if q[0] == number:
            q.popleft()
            break
        else:
            if q.index(number) < len(q) / 2:
                while q[0] != number:
                    q.append(q.popleft())
                    cnt += 1
            else:
                while q[0] != number:
                    q.appendleft(q.pop())
                    cnt += 1

print(cnt)