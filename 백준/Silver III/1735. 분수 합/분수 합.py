import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 분수 합
 1. 두 분수가 주어졌을 때, 그 합을 기약분수의 형태로 구하기
[입력]
 1. A: 분자, B: 분모
 2. C: 분자, D: 분모
[출력]
 1. 구하고자 하는 기약분수의 분자와 분모를 뜻하는 두 개의 자연수를 빈 칸을 사이에 두고 출력
"""

"""
<출력>
 1. 일단 풀어보기
"""


# 최대공약수 함수
def GCD(num1, num2):
    # 나누어 떨어질 경우 나눠진 수
    if not num2:
        return num1
    # 나누어 떨어지지 않을 경우 더 잘게 나누기
    else:
        return GCD(num2, num1 % num2)


# 최소공배수 함수
def LCM(num1, num2):
    # 두 수의 곱 / 두 수의 최대공약수 = 두 수의 최소공배수
    return int((num1 * num2) / GCD(num1, num2))


# 분자 A, 분모 B
A, B = map(int, input().split())
# 분자 C, 분모 D
C, D = map(int, input().split())

# 분모의 최소공배수 구하기
lcm = LCM(B, D)
# 분자에도 분모에 곱한 수만큼 곱하기
A *= lcm // B
C *= lcm // D
# 분자 더하기
son = A + C
# 분자와 분모의 최대공약수 구하기
gcd = GCD(son, lcm)
# 분자와 분모를 최대공약수로 나눈 수로 출력
print(son // gcd, lcm // gcd)