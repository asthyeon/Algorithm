import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 히오스 프로게이머 (16564)
 1. 게임이 끝날 때까지, 레벨을 최대 총합 K만큼 올릴 수 있음
 2. 팀 목표레빌 T = min(Xi)
 3. 게임이 끝날 때까지 성권이가 달성할 수 있는 최대 팀 목표레벨 T는?
[입력]
 1. N: 캐릭터의 개수, K: 올릴 수 있는 레벨 총합
 2. N개의 줄: 현재 각 캐릭터의 레벨이 주어짐
[출력]
 1. 가능한 최대 팀 목표레벨 T를 출력
"""

"""
<풀이>
 1. 이분탐색 -> 목표 레벨을 찾기
"""


def binary_search(levels):
    # 가장 작은 레벨이 시작 값
    start = min(levels)
    # 가장 큰 레벨 + K 가 끝 값
    end = max(levels) + K

    T = 0
    while start <= end:
        # 팀 목표 레벨 찾기
        middle = (start + end) // 2
        
        # 총 올린 레벨
        level_up = 0
        for level in levels:
            # 현재 레벨이 중간 값보다 작다면
            if level < middle:
                # 레벨업
                level_up += (middle - level)
        
        # 총 올린 레벨이 K보다 작거나 같다면
        if level_up <= K:
            # 중간 값 올린 후, 정답 교체
            start = middle + 1
            T = middle
        # 총 올린 레벨이 K보다 크다면 중간 값 줄이기
        else:
            end = middle - 1

    return T


N, K = map(int, input().split())
# 각 캐릭터의 레벨을 오름차순으로 정렬 (이분탐색을 위함)
levels = [int(input()) for _ in range(N)]
levels.sort()

print(binary_search(levels))