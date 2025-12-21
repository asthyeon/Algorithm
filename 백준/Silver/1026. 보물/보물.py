import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 보물 (1026)
1. S = A[0] x B[0] + ... + A[N-1] x B[N-1]
2. S의 값을 가장 작게 만들기 위해 A의 수를 재배열, B에 있는 수는 재배열 X
3. S의 최솟값 구하기

[풀이]
1. A, B 정렬 후 큰 값 찾기
2. B도 정렬해도 됨 -> A 재배치 자체가
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A 오름차순, B 내림차순 정렬
A_sort = sorted(A)
B_sort = sorted(B, reverse=True)

S = 0
for i in range(N):
    S += A_sort[i] * B_sort[i]

print(S)