import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제]
# 피보나치 함수 (1003)
1. fibo(3) -> fibo(2), fibo(1)
2. fibo(2) -> fibo(1), fibo(0)
3. fibo(1) -> 1
4. fibo(0) -> 0
5. fibo(N) 호출시 0과 1이 각각 몇 번 출력되는지?
[조건]
1. 테스트 케이스의 개수 T가 주어짐
2. 0 출력, 1 출력 횟수를 공백으로 구분
3. 마지막 40에 대한 값도 출력해야함
[풀이]
1. dp 이용 (모든 tc 체크)
2. 경우의 수 구하기
 0: 1 0
 1: 0 1
 2: 1 1
 3: 1 2
 4: 2 3
 5: 3 5
 6: 5 8
 - 이전의 수를 더한 값이 나옴
"""


def dynamic_programming():
    # 초기값 설정
    dp[0] = [1, 0]
    dp[1] = [0, 1]

    # 전전값 + 전값
    for i in range(2, 41):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]


# [0 출력 횟수, 1 출력 횟수]
dp = [[0, 0] for _ in range(41)]
dynamic_programming()

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    print(*dp[N])