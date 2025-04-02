import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
q = deque(i for i in range(1, N + 1))

sequence = deque()
while q:
    # K번 순회하여 K번째 사람을 맨 마지막으로 보내기
    for _ in range(K):
        q.append(q.popleft())
    # K번째 사람을 정답 순열에 붙이기
    sequence.append(q.pop())

answer = '<'
for i in range(N):
    if i == N- 1:
        answer += str(sequence.popleft())
    else:
        answer += f'{sequence.popleft()}, '
answer += '>'

print(answer)
