import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 기타줄 (1049)
 1. 6줄 패키지 or 1개 또는 그 이상의 줄을 낱개로 구매 가능
 2. 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하기
[입력]
 1. N: 끊어진 기타줄의 개수, M: 브랜드 수
 2. M개의 줄: 각 브랜드의 패키지 가격과 낱개의 가격
[출력]
 1. 기타줄을 적어도 N개 사기 위해 필요한 돈의 최솟값 출력
"""

"""
<풀이>
 1. 일단 풀어보기
 2. 경우의 수 3가지를 다 구하고 최솟값 출력하기
"""

N, M = map(int, input().split())
packages = []
singles = []
for _ in range(M):
    package, single = map(int, input().split())
    packages.append(package)
    singles.append(single)

# 최솟값들
min_p = min(packages)
min_s = min(singles)

# 몫과 나머지
share = N // 6
remainder = N % 6

# 패키지로만 구매할 때
only_p = min_p * share
if remainder > 0:
    only_p += min_p

# 낱개로만 구매할 때
only_s = min_s * share * 6 + min_s * remainder

# 혼합
mix_ps = min_p * share + min_s * remainder

print(min(only_p, only_s, mix_ps))