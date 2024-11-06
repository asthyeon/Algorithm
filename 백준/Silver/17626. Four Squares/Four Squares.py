import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# Four Squares (17626)
 1. 모든 자연수는 넷 혹은 그이하의 제곱수의 합으로 표현 가능
 2. 자연수 n 이 주어질 때 n 을 최소 개수의 제곱 수의 합으로 표현
[입력]
 1. n
[출력]
 1. 합이 n과 같게 되는 제곱수들의 최소 개수 출력
"""

"""
<풀이>
 1. 수학 -> dp
"""


def dynamic_programming():
    # 0 과 1
    dp = [0, 1]

    for i in range(2, n + 1):
        # 제곱수의 개수 최댓값 4 와 제곱수를 구할 j
        maximum = 4
        j = 1

        # 제곱수가 i 보다 작거나 같을 때
        while j ** 2 <= i:
            # 더 적은 갯수로 표현할 수 있다면 교체 후 j 값 변경
            maximum = min(maximum, dp[i - j ** 2])
            j += 1

        # 해당 수 dp 넣기
        dp.append(maximum + 1)

    return dp[n]


n = int(input())

print(dynamic_programming())