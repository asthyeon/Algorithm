import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 이항계수(11050)
 1. 자연수 N과 정수 K가 주어졌을 때 N과 K의 이항 계수 구하기
[입력]
 1. N: 자연수, K: 정수
[출력]
 1. N과 K의 이항 계수 출력
"""

"""
<풀이>
 1. 이항계수: 주어진 크기 집합에서 원하는 개수만큼 순서없이 뽑는 조합의 가짓수를 일컫음
 (이항: 하나의 아이템에 대해서 '뽑거나, 안 뽑거나' 두 가지의 선택만이 존재함)
 (N) = NCK의 조합과 같음
 (K)
 2. 조합 이용
"""

from itertools import combinations

# 자연수 N, 정수 K
N, K = map(int, input().split())
# 자연수 리스트
N_list = [i for i in range(1, N + 1)]
# 조합 구하기
print(len(list(combinations(N_list, K))))