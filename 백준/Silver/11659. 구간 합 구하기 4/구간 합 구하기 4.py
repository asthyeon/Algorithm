import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 구간 합 구하기 4 (11659)
1. 누적 합
"""

# 수의 개수 N, 합을 구해야 하는 횟수 M
N, M = map(int, input().split())
sequence = list(map(int, input().split()))

# 누적 합 구하기 (계산의 편의를 위해 0 투입)
prefix_sum = [0, sequence[0]]
for n in range(2, N + 1):
    prefix_sum.append(prefix_sum[n - 1] + sequence[n - 1])

# 합을 구해야 하는 구간
for m in range(M):
    i, j = map(int, input().split())

    print(prefix_sum[j] - prefix_sum[i - 1])