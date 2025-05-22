import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# queuestack (24511)
1. 큐+스택
2. 스택은 들어온 값이 나가므로 없다고 생각해도 됨
3. 큐만 생각할 것
"""
from collections import deque

N = int(input())
# 수열 A (해당 자리가 0일시 큐, 1일시 스택)
A = list(map(int, input().split()))
# 수열 A에 대응되는 수열 B (실질적인 원소)
B = list(map(int, input().split()))
# 삽입할 원소의 수열 길이 M, 수열 C
M = int(input())
C = list(map(int, input().split()))

# 큐만 구현
q = deque()
for i in range(N):
    if A[i] == 0:
        q.append(B[i])

# 큐가 없다면 C를 그대로 출력
if not q:
    print(*C)
else:
    # 가장 먼저 들어와 있는 큐의 원소 출력
    for j in range(M):
        q.appendleft(C[j])
        print(q.pop(), end=' ')
