import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 알약 (4811)
 0. 약이 N개 담긴 병 안에서
 1. 첫 날 약 하나는 반을 쪼개서 먹고, 다른 조각은 다시 병에 넣음
 2. 다음 날부터 종수의 행동: 병에서 약 하나를 꺼냄
  - 약이 반 조각일 때: 그 약을 먹음(H 보내기)
  - 약이 한 조각일 때: 반을 쪼개서 한 조각을 먹고 다른 조각은 다시 병에 넣음(W 보내기)
 3. 손녀는 받은 문자를 기록하여 총 2N일이 지나면 길이가 2N인 문자열을 만들 수 있음
[입력]
 1. 각 테스트 케이스마다 N: 약의 개수
 2. 입력의 마지막 줄에는 0이 하나 주어짐
[출력]
 1. 각 테스트 케이스에 대해서 가능한 문자열의 개수 출력
"""

"""
<풀이>
 1. dp
- 1: WH
- 2: WHWH, WWHH
- 3: WWWHHH, WWHWHH, WWHHWH, WHWWHH, WHWHWH
  H 0 1 2 3
W    
0   0 0 0 0
1   1 1 0 0
2   1 2 2 0
3   1 3 5 5
"""

# dp 미리 구현
dp = [[0] * 31 for _ in range(31)]
for W in range(1, 31):
    for H in range(31):
        # 첫 시작은 W 1개
        if H == 0:
            dp[W][H] = 1
        else:
            # H가 W 이하일 때
            if H <= W:
                # 왼쪽과 위의 합
                dp[W][H] = dp[W][H - 1] + dp[W - 1][H]

while True:
    N = int(input())

    # 종료 조건
    if N == 0:
        break

    print(dp[N][N])