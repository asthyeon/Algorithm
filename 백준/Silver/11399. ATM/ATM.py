import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] ATM (11399)
1. 줄을 서는 순서에 따라 돈을 인출하는데 필요한 시간의 합이 달라짐
2. 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값 구하기

[풀이]
1. 정렬
2. P가 적은 순서대로 정렬후 누적합
"""

N = int(input())
P = list(map(int, input().split()))

# 정렬 및 누적합
P_sort = sorted(P)
Prefix_sum = [0] * N
for i in range(N):
    if i == 0:
        Prefix_sum[i] = P_sort[0]
    else:
        Prefix_sum[i] = Prefix_sum[i-1] + P_sort[i]

print(sum(Prefix_sum))