import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 2의 멱수의 합
1. 어떤 자연수 N을 2의 멱수의 합으로 나타내는 경우의 수를 구하기
 - 2의 멱수: 2^k로 표현되는 자연수
* 입력
- 첫째 줄: 자연수 N
[출력: 경우의 수를 1,000,000,000으로 나눈 나머지 출력] 
"""

"""
@ 풀이
(1) 예시 찾아보기
1: 1가지
1
2: 2가지
11
2
3: 2가지
111
12
4: 4가지
1111
112
22
4
5: 4가지
11111
1112
122
14
6: 6가지
111111
11112
1122
114
222
24
7: 6가지
8: 10가지
9: 10가지
10: 14가지
12: 20가지
1111 1111 1111
1111 1111 112
1111 1111 22
1111 1111 4
1111 1122 2
1111 1124
1111 2222
1111 224
1111 44
1111 8
1122 222
1122 24
1124 4
1128
2222 22
2222 4
2244
228
444
48

2 - 4 - 6 - 8  - 10 - 12
2 - 4 - 6 - 10 - 14 - 20
홀수: 짝수항과 같음
짝수: 
2: 1 + 1 (dp[1] + dp[1])
4: 2 + 2 (dp[3] + dp[2])
6: 4 + 2 (dp[5] + dp[2])
8: 6 + 4 (dp[7] + dp[4])
10: 8 + 4 (dp[9] + dp[4])
12: 14 + 6 (dp[11] + dp[6])
dp[i] = dp[i - 1] + dp[i // 2]
(2) dp 이용
"""
# 나눌 값
REST = 1000000000


# dp
def dynamic_programming(N):
    dp = [0] * (N + 1)
    # 초기값 설정
    dp[1] = 1

    # 2 이상일 때
    if N >= 2:
        for i in range(2, N + 1):
            # 짝수일 때
            if i % 2 == 0:
                dp[i] = (dp[i - 1] + dp[i // 2]) % REST
            # 홀수일 때
            else:
                dp[i] = dp[i - 1] % REST

    return dp[N]


# 자연수 N
N = int(input())

print(dynamic_programming(N))