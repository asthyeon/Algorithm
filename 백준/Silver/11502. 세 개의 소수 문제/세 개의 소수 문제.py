import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 세 개의 소수 문제(11502)
 1. 세 개의 소수 문제
  - 5보다 큰 임의의 홀수는 정확히 세 개의 소수들의 합으로 나타낼 수 있음
  - 하나의 소수를 여러 번 더할 수 있음
[입력]
 1. T: 테스트 케이스 수
 2. K: 하나의 정수(5보다 큰 임의의 홀수)
[출력]
 1. T줄에 걸쳐서 각 줄에 K가 어떻게 세 소수의 합으로 오름차순으로 출력
 2. 여러 개의 답이 가능하다면 하나만 출력, 불가능하다면 0 출력
"""

"""
<풀이>
 1. 에라토스테네스의 체 이용
 2. 가장 큰 K 값으로 한 번에 만들기
"""


# 에라토스테네스의 체
def era(number):
    prime_numbers = [True] * (number + 1)
    primes = []
    # 2부터 시작
    for i in range(2, number + 1):
        # 이번 수가 소수라면
        if prime_numbers[i]:
            # 소수 리스트에 집어넣기
            primes.append(i)
            j = 2
            # 배수들 모두 False 처리
            while i * j <= number:
                prime_numbers[i * j] = False
                j += 1

    return primes


# 각 수가 소수인지 판별
def check(K_set):
    # 각 수에 배정할 딕셔너리
    K_dict = {}

    # 세 소수의 조합 찾기
    for p1 in primes:
        for p2 in primes:
            for p3 in primes:
                # 세 수의 합이 K가 된다면
                if p1 + p2 + p3 in K_set:
                    # 딕셔너리에 배정이 되지 않았다면
                    if p1 + p2 + p3 not in K_dict:
                        K_dict[p1 + p2 + p3] = [p1, p2, p3]

    return K_dict


T = int(input())
# 정수 K 리스트
K_list = []
for tc in range(1, T + 1):
    # 정수 K
    K = int(input())
    K_list.append(K)

# 소수 리스트
primes = era(max(K_list))
# 소수임을 판별하기 위한 세트
K_set = set(K_list)
# 각 수의 소수 조합 찾기
K_dict = check(K_set)

# 각 K의 조합 출력
for K in K_list:
    if K in K_dict:
        print(*K_dict[K])
    else:
        print(0)
