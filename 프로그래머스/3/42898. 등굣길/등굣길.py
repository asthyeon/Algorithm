"""
[문제] 등굣길
1. 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수
2. 1,000,000,007로 나눈 나머지 return

[풀이]
1. dp

   1  2  3  4
1  1  1  1  1 
2  1 -1  1  2
3  1  1  2  4
"""


def solution(m, n, puddles):
    answer = 0
    
    
    def dynamic_programming():
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # 물이 잠긴 지역 
        for px, py in puddles:
            dp[py][px] = -1
        
        for x in range(1, n + 1):
            for y in range(1, m + 1):
                # 시작점 초기화
                if x == 1 and y == 1:
                    dp[x][y] = 1
                    continue
                    
                # 물이 아니라면
                if dp[x][y] != -1:
                    # 위에서 올 때(물인 경우는 제외)
                    up = max(0, dp[x - 1][y])
                    # 왼쪽에서 올 때(물인 경우는 제외)
                    left = max(0, dp[x][y - 1])
                    # 값 더하기
                    dp[x][y] = up + left
                
        
        for _ in range(n + 1):
            print(dp[_])
        
        # 나머지로 나누기
        return dp[n][m] % 1000000007
    
    answer = dynamic_programming()
    return answer