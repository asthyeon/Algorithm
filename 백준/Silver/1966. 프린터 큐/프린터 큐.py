import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    q = deque(list(map(int, input().split())))

    turn = 0
    while q:
        # 순번 앞당기기
        M -= 1

        # 가장 큰 숫자일 경우
        if q[0] == max(q):
            turn += 1
            q.popleft()

            if M < 0:
                print(turn)
                break

        # 가장 큰 숫자가 아닐 경우
        else:
            q.append(q.popleft())

            if M < 0:
                M = len(q) - 1




