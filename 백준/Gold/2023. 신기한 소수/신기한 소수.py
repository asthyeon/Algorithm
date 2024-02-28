import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 신기한 소수(2023)
 1. 신기한 소수: 왼쪽부터 1자리, 2자리, 3자리, ..., N자리 모두 소수인 소수
 2. N자리의 숫자 중 어떤 수들이 신기한 소수인지?
[입력]
 1. N: 자리 수
[출력]
 1. N자리 수 중에서 신기한 소수를 오름차순으로 정렬해서 한 줄에 하나씩 출력
"""

"""
<풀이>
 1. 에라토스테네스의 체 이용 -> 메모리 초과
 2. 리스트로 선언하지말고 바로 소수인지 아닌지 판별해보기
"""


# 소수 판별
def check(num):
    # 에라토스테네스의 체
    for i in range(2, int(num ** 0.5) + 1):
        # 이번 수가 소수가 아니라면
        if num % i == 0:
            return False
    # 전부 다 통과하면 소수
    else:
        return True


# 신기한 소수 찾기
def unbelievable(idx, number):
    if idx == N:
        print(number)
        return

    # 수가 아예 없으면 2부터 시작
    if not number:
        for i in range(2, 10):
            if check(i):
                unbelievable(idx + 1, number + str(i))

    # 할당된 수가 있으면 1부터 시작
    else:
        for i in range(1, 10):
            if check(int(number + str(i))):
                unbelievable(idx + 1, number + str(i))


# N
N = int(input())

unbelievable(0, '')