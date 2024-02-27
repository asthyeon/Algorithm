import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 1, 2, 3 더하기 5(15990)
 1. 정수 4를 1, 2, 3의 합으로 나타내기
 2. 단 같은 수를 두 번 이상 연속해서 사용하면 X
 3. 정수 n이 주어졌을 때 n을 1, 2, 3의 합으로 나타내는 방법의 수 구하기
[입력]
 1. T: 테스트 케이스 수
 2. n: 정수 n
[출력]
 1. n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지 출력
"""

"""
<풀이>
 0. 수의 순서를 바꿔도 됨 
 1. dp의 냄새가 솔솔
 2. 예시
  1 - [1] (1가지)
  2 - [2] (1가지)
  3 - [1 + 2], [2 + 1], [3] (3가지)
  4 - [1 + 2 + 1], [1 + 3], [3 + 1] (3가지)
  5 - [1 + 3 + 1], [2 + 1 + 2], [2 + 3], [3 + 2] (4가지)
  6 - [1 + 2 + 1 + 2], [1 + 2 + 3], [1 + 3 + 2], [2 + 1 + 2 + 1], 
      [2 + 1 + 3], [2 + 3 + 1], [3 + 1 + 2], [3 + 2 + 1] (8가지)
 3. 경우의 수가 1, 2, 3으로 끝나는 경우의 수를 구하기 -> 시간초과
 4. 가장 큰 값으로 dp를 만들고 각 수에 해당하는 값을 추출해보기
"""
REST = 1000000009


# dp
def dynamic_programming(n):
    dp = [[0] * 4 for _ in range(n + 1)]

    # 1, 2, 3 의 경우의 수 구하기
    dp[1][1] = 1
    if n >= 2:
        dp[2][2] = 1
    if n >= 3:
        dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1

    # 그 이후의 경우의 수
    if n >= 4:
        for i in range(4, n + 1):
            dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % REST
            dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % REST
            dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % REST

    # 숫자 리스트 출력
    for number in numbers:
        print(sum(dp[number]) % REST)


T = int(input())
# 숫자 리스트 받기
numbers = []
for tc in range(1, T + 1):
    n = int(input())
    numbers.append(n)

dynamic_programming(max(numbers))

