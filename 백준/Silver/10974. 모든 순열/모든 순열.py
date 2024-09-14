import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 모든 순열 (10974)
 1. N이 주어졌을 때, 1부터 N까지 이루어진 순열을 사전 순으로 출력
[입력]
 1. N
[출력]
 1. N!개의 줄에 걸쳐서 모든 순열을 사전 순으로 출력
"""

"""
<풀이>
 1. 순열
"""
from itertools import permutations

N = int(input())

# 순열 만들기
N_list = [i for i in range(1, N + 1)]
permutation = list(permutations(N_list, N))

# 수열 출력
for sequence in permutation:
    print(*sequence)