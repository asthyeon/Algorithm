import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 1학년 (5557)
 1. 마지막 두 숫자 사이에 '=', 나머지 숫자 사이에 '+' 또는 '-' 넣기
 2. 음수, 20을 넘는 수는 제외하기
[입력]
 1. N: 숫자의 개수
[출력]
 1. 만들 수 있는 올바른 등식의 개수 출력
"""

"""
<풀이>
 1. dp
"""


def dynamic_programming(numbers):
    # 마지막 줄은 결과값이므로 N - 1개의 줄만 연산
    dp = [[0] * 21 for _ in range(N - 1)]

    # 첫 번째 값 지정
    dp[0][numbers[0]] = 1
    # 각 숫자들에 대한 차례
    for turn in range(1, N - 1):
        # 값을 만들 수 있는 범위 0 ~ 20
        for value in range(21):
            # 이전 값 찾기
            if dp[turn - 1][value] > 0:
                # 더하기 범위 안에 들 경우
                plus = value + numbers[turn]
                if 0 <= plus <= 20:
                    dp[turn][plus] += dp[turn - 1][value]
                # 빼기 범위 안에 들 경우
                minus = value - numbers[turn]
                if 0 <= minus <= 20:
                    dp[turn][minus] += dp[turn - 1][value]

    return dp[-1][numbers[-1]]


N = int(input())
numbers = list(map(int, input().split()))

print(dynamic_programming(numbers))