import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 카드 구매하기
1. 카드 N개가 포함된 카드팩과 같이 총 N가지 존재
2. 최대한 많은 돈으로 카드 N개 구매하기
 - 카드 i개가 포함된 카드팩 가격: Pi원
* 입력
- 첫째 줄: 카드의 개수 N
- 둘째 줄: 카드 정보 P
[출력: 카드 N개를 갖기 위해 지불해야 하는 금액의 최댓값 출력]
"""

"""
@ 풀이
(1) dp로 풀기
dp[1] = 1 P[1]
dp[2] = 5 P[2]
dp[3] = 6 P[3] or (dp[2] + dp[1])
dp[4] = 10 P[2]
(2) 나누어 떨어지지 않을 때를 고려해야함
(3) 서로 다른 종류로 3개 이상을 살 수도 있음 -> 카드 개수 나머지의 최대값 더하기
cards = [1 1 6 8 11 1 1 1 1 1 1 1]
dp[1] = 1 cards[1]
dp[2] = 2 cards[2]
dp[3] = 6 cards[3]
dp[4] = 8 cards[4]
dp[5] = 11 cards[5]
dp[6] = 12 (cards[5] + dp[1]) or (cards[3] + dp[3])
dp[7] = 14 (cards[4] + dp[3]) or (cards[3] + dp[4])
dp[8] = 17 (cards[5] + dp[3])
dp[i] = max(dp[i], cards[card] + dp[i - card])
"""


# dp
def dynamic_programming(cards):
    dp = [0] * (N + 1)
    
    # 각 카드 순회
    for card in range(1, N + 1):
        # 각 dp 값 할당
        for i in range(card, N + 1):
            # dp의 값은 이전에 설정된 값과 한 카드를 사용했을 때 나머지의 최대값
            dp[i] = max(dp[i], cards[card] + dp[i - card])
    
    return dp[N]


# 카드의 개수 N
N = int(input())
# 카드 정보
cards = [0] + list(map(int, input().split()))

print(dynamic_programming(cards))

