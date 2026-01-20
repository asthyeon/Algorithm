"""
[문제] 멀리 뛰기
1. 효진이는 한 번에 1칸, 또는 2칸을 뛸 수 있음

[풀이]
1. dp
0 0 0 0
1 1 1 1
1 2   1
1 1   2
  2 1 1
  2   2

1 1 1
1 0 2
0 2 1

1 2 3 5
"""


def solution(n):
    answer = 0
    
    
    def dynamic_programming():
        dp = [0] * n
        
        # n이 1일 때
        if n == 1:
            return 1
        # n이 2일 때
        elif n == 2:
            return 2
        
        # 1, 2 값 넣기
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            # 직전 값 + 직직전 값
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # 나머지 리턴
        return dp[n - 1] % 1234567
    
    
    answer = dynamic_programming()
    return answer