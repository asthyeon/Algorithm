import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 소수&팰린드롬(1747)
 1. N이 주어졌을 때 N보다 크거나 같고 소수이면서 팰린드롬인 수 중에서 가장 작은 수 구하기
[입럭]
 1. N: 기준 수
[출력]
 1. 조건을 만족하는 수 출력
"""

"""
<풀이>
 1. 에라토스테네스의 체로 모든 소수 구해놓고 팰린드롬 확인
 2. 최대값이 1,000,000 을 초과할 수 있음(이것은 N값이기 때문)
 3. 1000000 보다 큰 값: 1003001을 최댓값으로 하여 계산하기
 4. N이 1일 때를 고려하기
"""


# 에라토스테네스의 체
def era(N):
    # 백만보다 큰 값으로 설정
    prime_numbers = [True] * 1003002
    
    # 소수 구하기
    for i in range(2, 1003002):
        if prime_numbers[i]:
            j = 2
            while i * j <= 1003001:
                prime_numbers[i * j] = False
                j += 1
    
    # 팰린드롬 확인
    palindrome(prime_numbers)


# 팰린드롬 확인
def palindrome(prime_numbers):
    # 1이 아닐 때는 소수 구하기
    if N != 1:
        for i in range(N, 1003002):
            if prime_numbers[i]:
                # 문자열 맨 앞과 맨 뒤를 하나씩 늘리고 줄여가며 확인
                for s in range(len(str(i))):
                    if str(i)[s] != str(i)[len(str(i)) - 1 - s]:
                        break
                # 팰린드롬이라면 i 출력 후 종료
                else:
                    print(i)
                    exit()
    # 1일 때는 가장 작은 소수는 2 출력 후 종료
    else:
        print(2)
        exit()


# N
N = int(input())

era(N)