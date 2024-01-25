import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 점프 점프
 1. 1xN 크기의 미로의 i번째 칸에는 A라는 정수가 쓰여 있음
 2. 재환이는 해당 칸의 A 이하만큼 오른쪽으로 떨어진 칸으로 한 번에 점프 가능
 3. 가장 왼쪽에서 가장 오른쪽으로 가려면 최소 몇번 점프?
[입력]
 1. N: 미로의 가로 크기
 2. A: 각 미로 칸의 정수 정보
[출력]
 1. 최소 몇 번 점프하는지 출력(오른쪽 끝으로 갈 수 없을 경우 -1 출력)
"""

"""
@ 풀이
 1. dp 이용
"""


# dp
def dynamic_programming(A):
    dp = [1001] * N
    # 시작점 값 설정
    dp[0] = 0

    # 시작점 순회
    for start in range(N - 1):
        # 도달하지 못한 곳이라면 종료
        if dp[start] == 1001:
            break
        # 해당 시작점에서 점프 할 수 있는 거리 재기
        for jump in range(start + 1, N):
            # 점프 범위를 벗어나면 반복 종료
            if jump > start + A[start]:
                break
            # 이전에 점프해서 도달한 값과 이번에 점프하는 값중 최소값으로 교체
            dp[jump] = min(dp[jump], dp[start] + 1)
    
    # 도달할 수 있다면 그대로 값 출력
    if dp[-1] != 1001:
        return dp[-1]
    # 도달하지 못한다면 -1 출력
    else:
        return -1


# 미로의 가로 크기 N
N = int(input())
# 미로 정보
A = list(map(int, input().split()))

print(dynamic_programming(A))