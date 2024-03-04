import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# BOJ 거리(12026)
 1. 스타트(1번)가 링크(N번)를 만나는데 필요한 에너지 양의 최솟값 구하기
 2. 각 보도블록 B, O, J 중에 하나가 쓰여 있음, 1번은 반드시 B
 3. 스타트는 점프로 이동하는데 i번 점프 -> i+1번 ~ N번까지 점프 가능
 4. 한 번 k칸 만큼 점프시 필요한 에너지 양 k * k
 5. 스타트는 Bm Om J 순서로 보도블록을 밟으면서 점프함
[입력]
 1. N: 보도블록 길이
 2. 둘째 줄: 보도블록 정보
[출력]
 1. 스타트가 링크를 만나는데 필요한 에너지 양의 최솟값 출력
 2. 스타트가 링크를 만날 수 없는 경우 -1 출력
"""

"""
<풀이>
 1. dp 이용
 2. 문자별로 그 뒤의 경우의 수 다 구해보기
"""
# 문자 치환용
dicts = {'B': 'O', 'O': 'J', 'J': 'B'}


# dp
def dynamic_programming(N):
    dp = [10e9] * N

    # 시작값 초기화
    dp[0] = 0

    # 모든 문자 순회
    for start in range(N):
        # 이번 문자 선언
        char = blocks[start]
        # 이번 문자의 다음 지역에 에너지 더하기
        for s in range(start + 1, N):
            # 이번 문자의 다음 문자라면 에너지 더한 값과 그 이전 값중 작은 값으로 하기
            if blocks[s] == dicts[char]:
                dp[s] = min(dp[s], dp[start] + ((s - start) ** 2))

    # 도달하지 못한다면 -1 출력
    if dp[-1] == 10e9:
        return -1
    # 도달하면 값 출력
    else:
        return dp[-1]


# 보도블록 길이 N
N = int(input())
# 보도블록 정보
blocks = list(input())

print(dynamic_programming(N))