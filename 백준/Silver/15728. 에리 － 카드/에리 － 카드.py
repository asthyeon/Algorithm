import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 에리 - 카드(15728)
 1. N 장의 '공유 숫자카드', N 장의 팀 숫자카드
 2. 상대 팀은 우리 팀의 '팀 숫자카드' K 장 견제 가능, 견제된 카드는 낼 수 없음
 3. 모든 견제가 마친 후 우리 팀은 '공유 숫자카드' 한 장 x '팀 숫자카드' 한 장 곱하여 점수
 4. 상대 팀은 최선의 방법으로 견제할 때 우리 팀이 얻을 수 있는 최대 점수 출력
[입력]
 1. N: 카드 수, K: 견제 가능 카드 수
 2. 둘째 줄: 공유 숫자카드
 3. 셋째 줄: 팀 숫자카드
[출력]
 1. 우리 팀이 얻을 수 있는 최대 점수 출력
"""

"""
<풀이>
 1. 정렬 이용
 2. 모든 경우의 수 구하기 -> 음수끼리 곱하게 되면 견제는 음수를 하게 됨
 3. 진짜로 모든 경우의 수 구하기
"""


# 카드 수 N, 견제 가능 카드 수 K
N, K = map(int, input().split())
# 공유 숫자카드
share_cards = list(map(int, input().split()))
# 팀 숫자카드
team_cards = list(map(int, input().split()))

# 견제 가능 횟수만큼 가장 큰 경우의 수가 나오는 두 번의 팀 숫자카드 제거하기
for _ in range(K):
    # 가장 작은 수로 값 선언
    max_card = -10000 * 10000 - 1
    # 제거해야할 카드
    card = team_cards[0]
    for share_card in share_cards:
        for team_card in team_cards:
            if max_card < share_card * team_card:
                max_card = share_card * team_card
                card = team_card
    # 가장 큰 경우의 수가 되는 팀 카드 제거
    team_cards.remove(card)

# 가장 큰 경우 구하기
max_card = -10000 * 10000 - 1
for share_card in share_cards:
    for team_card in team_cards:
        if max_card < share_card * team_card:
            max_card = share_card * team_card

print(max_card)
