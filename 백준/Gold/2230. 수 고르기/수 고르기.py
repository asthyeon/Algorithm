import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 수 고르기(2230)
 1. N개의 정수로 이루어진 수열 A[1], A[2], ..., A[N]
 2. 이 수열에서 두 수를 골랐을 때 그 차이가 M 이상이면서 제일 작은 경우를 구하기
[입력]
 1. N, M: N개의 정수와 차이 M
 2. N개의 줄: A[1], ..., A[N]
[출력]
 1. M 이상이면서 가장 작은 차이 출력(항상 차이가 M이상인 두 수를 고를 수 있음)
"""

"""
<풀이>
 1. 일단 풀어보기
"""

N, M = map(int, input().split())
# 수열 A
A = []
for _ in range(N):
    A.append(int(input()))
A.sort()

# 투 포인터
start = 0
end = 0
# 차이
difference = 10e9

while start < N and end < N:
    # 차이가 M 초과일 때
    if A[end] - A[start] > M:
        difference = min(difference, A[end] - A[start])
        # 차이 좁히기
        start += 1
    # 차이가 M 일 때 종료
    elif A[end] - A[start] == M:
        print(M)
        exit()
    # 차이가 M 미만일 때
    else:
        # 차이 늘리기
        end += 1

print(difference)