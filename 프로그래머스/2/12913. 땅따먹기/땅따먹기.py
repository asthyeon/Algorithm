"""
[문제] 땅따먹기
1. 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟아야 함
2. 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 계속해서 밟을 수 없음

[풀이]
1. dp
 1  2  3  5
 7  9 12 11
13 15 13 13
"""


def solution(land):
    answer = 0

    
    def dynamic_programming():
        dp = land[:]
        
        # 첫 행 값 부여
        dp[0] = land[0]
        for i in range(1, len(land)):
            # 첫 번째
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][3]) + land[i][0]
            # 두 번째
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][2], dp[i - 1][3]) + land[i][1]
            # 세 번째
            dp[i][2] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][3]) + land[i][2]
            # 네 번째
            dp[i][3] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) + land[i][3]
        
        return max(dp[-1])
    
    answer = dynamic_programming()
    return answer