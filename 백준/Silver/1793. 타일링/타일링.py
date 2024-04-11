import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 타일링 (1973)
 1. 2xn 직사각형을 2x1과 2x2 타일로 채우는 방법의 수를 구하기
[입력]
 1. n: 직사각형 가로 길이
[출력]
 1. 입력으로 주어지는 각각의 n마다 2xn 직사각형을 채우는 방법의 수 출력
"""

"""
<풀이>
 1. dp
0: 1 -> 2x0 직사각형을 채우는 방법의 수 1가지 (아무 것도 안쓰면 됨)
1: 1 (2x1)
2: 3 -> (dp[0]에 2x2 타일 붙이기 and 2x1 타일 가로로 붙이기) + (dp[1]에 2x1 타일 세로로 붙이기) 
3: 5 -> (dp[1]에 2x2 타일 붙이기 and 2x1 타일 가로로 붙이기) + (dp[2]에 2x1 타일 세로로 붙이기)
4: 11
5: 21
6: 43
7: 85
8: 171
 2. 미리 만들어놓기
"""

# dp
dp = [0] * 251
dp[0] = 1
dp[1] = 1
for i in range(2, 251):
    dp[i] = dp[i - 2] * 2 + dp[i - 1]

# 입력 받기
while True:
    try:
        n = int(input())
        print(dp[n])
    except:
        break