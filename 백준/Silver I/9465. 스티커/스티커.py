import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 스티커(9465)
    1. 스티커를 떼면 상하좌우 사용 불가
    2. 점수의 합을 최대로 스티커 떼어내기
[입력]
    1. T: 테스트 케이스 수
    2. n: 한 줄의 스티커 수
    3. 2줄 -> 각 스티커 점수
[출력]
    1. 2n개의 스티커 중 두 변을 공유하지 않는 스티커 점수의 최댓값 출력
"""

"""
<풀이>
    1. 위에서 떼면 다음은 아래에서 떼야함
    2. dp 이용
        [1, 2]
        [A, B]
        ㄱ. [1, B]
        ㄴ. [A, 2]
        [1, 2, 3]
        [A, B, C]
        ㄱ. [1] -> [1, B] -> [1, B, 3] or [A, 3]
        ㄴ. [A] -> [A, 2] -> [A, 2, C] or [1, C]
        [1, 2, 3, 4]
        [A, B, C, D]
        ㄱ. [1] -> [1, B] -> [1, B, 3] or [A, 3] -> [1, B, 3, D] or [A, 3, D]
        ㄴ. [A] -> [A, 2] -> [A, 2, C] or [1, C] -> [A, 2, C, 4] or [1, C, 4]
"""


# dp
def dynamic_programming(stickers):
    dp = [[0] * (n + 1) for _ in range(2)]

    for i in range(1, n + 1):
        # 1번째와 2번째는 비교군이 없으므로 그냥 선택
        if i <= 2:
            dp[0][i] = dp[1][i - 1] + stickers[0][i]
            dp[1][i] = dp[0][i - 1] + stickers[1][i]
        # 3번째부터는 다른 방식
        else:
            # (전전값 위 + 전값 아래) vs (전값 위)
            dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + stickers[0][i]
            # (전전값 아래 + 전값 위) vs (전값 아래)
            dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + stickers[1][i]

    # 가장 큰값 반환
    answer = max(dp[0][n], dp[1][n])
    return answer


T = int(input())
for tc in range(1, T + 1):
    # 한 줄의 스티커 수 n
    n = int(input())
    # 스티커 정보(용이한 계산을 위한 0 넣기)
    stickers = [[], []]
    for _ in range(2):
        stickers[_] = [0] + list(map(int, input().split()))

    print(dynamic_programming(stickers))