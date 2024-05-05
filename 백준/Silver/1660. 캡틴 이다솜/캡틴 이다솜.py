import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 캡틴 이다솜 (1660)
 1. 대포알을 사면체 모양으로 쌓아놓기
 2. 사면체를 만드는 방법은
  - 길이가 N인 정삼각형 모양 만들기
  - 그 위에 길이가 N-1인 정삼각형 모양을 얹고 그 위에 계속 얹어서 1 크기의 정삼각형 모양 얹기
[입력]
 1. N: 대포알 수
[출력]
 1. 만들 수 있는 사면체 개수의 최솟값 출력
"""

"""
<풀이>
 1. dp
 2. 1 - 3 -  6 - 10 - 15
 3. 1 - 4 - 10 - 20 - 35
 4. 역순으로 큰 것부터 만들어야 최소 개수를 만들 수 있음
"""


# dp
def dynamic_programming(N):
    dp = [10e9] * (N + 1)

    # 총 포탄 수 리스트
    shell_list = []
    # 이번에 필요한 총 포탄 수
    shell = 1
    # 새로운 사면체를 만들 때 추가되는 한 줄
    one_line = 2
    # 새로운 사면체를 만들 때 추가되는 포탄 수
    one_tetrahedron = 1

    # 포탄 수가 N보다 작을 때 리스트에 추가
    while shell <= N:
        # 포탄 수 append
        shell_list.append(shell)
        # 새 사면체 한 줄 추가
        one_tetrahedron += one_line
        # 포탄 수에 새 사면체 수 추가
        shell += one_tetrahedron
        # 새 사면체에 추가할 한 줄 +1
        one_line += 1
    
    # N까지 순회
    for i in range(1, N + 1):
        # 포탄 리스트 순회
        for shell in shell_list:
            # 포탄이 더 크면 넘기기
            if i < shell:
                break
            # 포탄이 딱 맞아 떨어지면 1개로 취급
            if i == shell:
                dp[i] = 1
                break
            # 더 작으면 포탄 수만큼 뺀 거에 +1
            dp[i] = min(dp[i], dp[i - shell] + 1)

    return dp[N]


N = int(input())

print(dynamic_programming(N))