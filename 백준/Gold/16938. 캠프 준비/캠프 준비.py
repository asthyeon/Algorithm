import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 캠프 준비
 1. N개의 문제, 모든 문제의 난이도를 정수로 수치화
 2. i번째 문제의 난이도는 A(i)
 3. 사용할 문제는 두 문제 이상
 4. 문제 난이도의 합은 L 이상 R 이하
 5. 가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는 X 이상
[입력]
 1. N: 문제 수, L: 난이도 최소 합, R: 난이도 최대 합, X: 난이도 최소 차이
 2. A: 문제들의 난이도
[출력]
 1. 캠프에 사용할 문제를 고르는 방법의 수 출력
"""

"""
<풀이>
 1. 조합 이용해보기
"""
from itertools import combinations

# 문제 수 N, 난이도 최소 합 L, 난이도 최대 합 R, 난이도 최소 차이 X
N, L, R, X = map(int, input().split())
# 문제들의 난이도
A = list(map(int, input().split()))

# 가능한 모든 조합 만들어내기
answer = 0
for r in range(1, N + 1):
    for choices in combinations(A, r):
        if L <= sum(choices) <= R and max(choices) - min(choices) >= X:
            answer += 1

print(answer)