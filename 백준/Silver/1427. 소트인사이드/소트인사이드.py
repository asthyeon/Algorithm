import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
<문제>
# 소트인사이드 (1427)
1. 수의 각 자리수를 내림차순으로 정렬
"""

"""
<풀이>
1. 문자열로 받고 정렬
2. join 이용
"""

N = input().strip()
answer = sorted(N, reverse=True)

print(''.join(answer))